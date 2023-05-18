import pika

# connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq.cuiqingcai.com', port=5672, credentials=credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')


#  on_message_callback(channel, method, properties, body)
#   - channel: BlockingChannel
#   - method: spec.Basic.Deliver
#   - properties: spec.BasicProperties
#   - body: bytes
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()