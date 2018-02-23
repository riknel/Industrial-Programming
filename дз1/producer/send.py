#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('queue', port=5672))

channel = connection.channel()
channel.queue_declare(queue='messages')

with open('input_data') as text:
    for line in text:
        channel.basic_publish(exchange='',
                              routing_key='messages',
                              body=line.encode())
        print(f'Pushed string {line}')

connection.close()
