import logging

import pika
import redis

# 连接 Redis
redis_client = redis.Redis(host='localhost', port=6379)


def process_message(body):
    pass


def callback(ch, method, properties, body):
    message_id = properties.message_id

    # 判断 Redis 中是否已经消费
    if redis_client.get(message_id) is not None:
        ch.basic_ack(delivery_tag=method.delivery_tag)
        return

    # Redis pipeline 中添加消息 ID
    pipeline = redis_client.pipeline()

    try:
        # value值不关心
        pipeline.set(message_id, 1)

        # 处理消息 (易错的源头)
        process_message(body)

        # 执行 Redis pipeline，将消息 ID 存储到 Redis 中
        pipeline.execute()

        # 消息处理成功，发送确认消息
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        # 如果 Redis 中已经记录了消息的消费记录，则删除
        if redis_client.get(message_id) is not None:
            redis_client.delete(message_id)

        # 处理消息时发生异常，不发送确认消息，让消息重新入队
        logging.error(f"Failed to process message with ID {message_id}: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

        #  很好，在except块中，先后撤销redis的数据更改，然后mq消息重新入列。但是又发生了一个问题。
        #  但是，万一except块中的撤销操作存在部分失败，或者全部失败了呢？此时如何处理，难道一致try-except死循坏吗？
        #  如果在撤销操作中部分失败，可以进行重试操作。可以在except块中加入重试逻辑，通过一些策略来控制重试次数和时间间隔，比如指数退避算法等。
        #  如果重试之后，撤销操作如果依旧存在部分失败呢？=> 报警监测，人工介入，这种一般是非常极端的情况



# 建立 RabbitMQ 连接和信道
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 设置消息消费者并开启消费
channel.basic_consume(queue='my_queue', on_message_callback=callback)
channel.start_consuming()
