import pika

MAX_PRIORITY = 100
QUEUE_NAME = 'scrape'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


while True:
    # input 是为了模拟阻塞，控制消费者消耗速率
    input()
    method_frame, header, body = channel.basic_get(
        queue=QUEUE_NAME, auto_ack=True)
    if body:
        print(f'Get {body}')
