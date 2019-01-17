import pika
import time

credentials = pika.PlainCredentials('user', 'hc123456')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='111.231.132.132', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode('utf8'))
    time.sleep(body.count(b'.'))
    print(" [x] Done")


channel.basic_consume(callback,
                      queue='task_queue',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
