import pika

MAX_PRIORITY = 100
QUEUE_NAME = 'scrape'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME, arguments={
    'x-max-priority': MAX_PRIORITY
}, durable=True)

# durable=True 表示的是队列的持久化，mq重启后queue会重建，此时msg是否还在取决于channel发布msg的delivery_mode
while True:
    data, priority = input().split()
    channel.basic_publish(exchange='',
                          routing_key=QUEUE_NAME,
                          properties=pika.BasicProperties(
                              priority=int(priority),
                              delivery_mode=2,
                          ),
                          # delivery_mode=2  指的是msg的持久化
                          body=data)
    print(f'Put {data}')
