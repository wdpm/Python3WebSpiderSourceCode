def send_message(message):
    # 生成消息ID
    message_id = generate_message_id()

    # 发送消息到 RabbitMQ
    channel.basic_publish(exchange='', routing_key='my_queue', properties=pika.BasicProperties(message_id=message_id),
                          body=message)
