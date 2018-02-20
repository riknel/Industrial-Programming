#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
data = input()
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=data.encode())
connection.close()
:
