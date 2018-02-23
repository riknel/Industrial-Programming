#!/usr/bin/env python
import pika
import psycopg2

connection = pika.BlockingConnection(pika.ConnectionParameters('queue', port=5672))
channel = connection.channel()
channel.queue_declare(queue='messages')

db_connection = psycopg2.connect("dbname=db user=db password=db host=db port=5432 ")

def callback(ch, method, properties, body):
    str_body = body.decode()
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO received(body) VALUES ('{str_body}')")
    db_connection.commit()
    cursor.close()
    print(f'Push {str_body}')

#creating db
cursor = db_connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS received (body TEXT)")
db_connection.commit()

channel.basic_consume(callback,
                      queue='messages',
                      no_ack=True,
                      )

channel.start_consuming()

db_connection.close()
connection.close()
