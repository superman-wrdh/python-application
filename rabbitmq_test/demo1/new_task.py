import pika

credentials = pika.PlainCredentials('user', 'hc123456')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='111.231.132.132', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue')

messages = ['python new_task.py First message.',
            'python new_task.py Second message..',
            'python new_task.py Third message...',
            'python new_task.py Fourth message....',
            'python new_task.py Fifth message.....',
            'python new_task.py Sixth message......']
for m in messages:
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=m,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))
    print(" [x] Sent %r" % m)

connection.close()
