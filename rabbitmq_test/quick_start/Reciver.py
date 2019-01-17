# -*- encoding: utf-8 -*-
import pika

if __name__ == '__main__':
    credentials = pika.PlainCredentials('guest', 'guest')
    # 链接rabbit
    connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.199.157', 5672, '/', credentials))
    # 创建频道
    channel = connection.channel()
    # 如果生产者没有运行创建队列，那么消费者创建队列
    channel.queue_declare(queue='hello')


    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        import time
        time.sleep(10)
        print('ok ack')
        ch.basic_ack(delivery_tag=method.delivery_tag)  # 主要使用此代码


    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=False)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
