import pika
import psycopg2

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbit'))
channel = connection.channel()

channel.queue_declare(queue='hello')

db_connection = psycopg2.connect("dbname=db user=db password=db host=db port=5432")


def callback(ch, method, properties, body):
    str_body = (body.decode())
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO queue VALUES (DEFAULT, %s)", (recieved,))
    db_connection.commit()
    cursor.close()

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
db_connection.close()
connection.close()
