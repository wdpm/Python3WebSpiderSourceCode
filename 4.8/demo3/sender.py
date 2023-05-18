import pika

MAX_PRIORITY = 100
QUEUE_NAME = 'scrape'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)

while True:
    # input阻塞，控制生产者生产速率
    data = input()
    channel.basic_publish(exchange='',
                          routing_key=QUEUE_NAME,
                          body=data)
    print(f'Put {data}')
