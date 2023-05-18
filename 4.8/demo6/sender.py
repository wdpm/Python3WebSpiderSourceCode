import pickle

import pika
import requests

MAX_PRIORITY = 100
TOTAL = 100
QUEUE_NAME = 'scrape3'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME, durable=True)

# def handle_return(channel, method, properties, body):
#     print(f"Message {method.routing_key} was returned: {body}")

# 当消息被发送到不存在的队列或者被标记为 mandatory 但无法被路由到时，会触发 Basic.Return 命令，
# 这时就会回调 handle_return 函数。需要注意的是，这个回调只有在将 mandatory 标志设置为 True 时才会触发
# channel.add_on_return_callback(handle_return)

# refer: https://www.rabbitmq.com/confirms.html
channel.confirm_delivery()

# 将请求往持久化queue中存放，一个msg对应一个独立的请求
for i in range(1, TOTAL + 1):
    url = f'https://ssr1.scrape.center/detail/{i}'
    request = requests.Request('GET', url)
    print('re', request)
    # 上述代码中增加了 mandatory=True 参数，
    # - 正常投递：返回None
    # - 当消息无法路由到队列时，将引发一个 Basic.Return 消息，并使得 channel.basic_publish() 返回值不为 None
    publish_result = channel.basic_publish(exchange='', routing_key=QUEUE_NAME,
                                    properties=pika.BasicProperties(delivery_mode=2, ), mandatory=True,
                                    body=pickle.dumps(request))
    if not publish_result:
        print(f"Put request of {url} successfully")
    else:
        print(f"Failed to put request of {url}")

    # 第二种策略：自身限流。避免消息发送过快，导致部分消息丢失，无法持久化到queue
    # time.sleep(random.random())

# 问题2：如何避免重复存放任务到mq中，如何建立端到端的唯一ID机制
