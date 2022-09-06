import logging
from common.constants import LOG_FORMAT
import pika

logging.basicConfig(format=LOG_FORMAT)
log = logging.getLogger(__name__)


class WorkMQService:
    def __init__(self) -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

    def publish_task(self, queue:str, durable:bool , routing_key:str,  message:str):
        self.channel.queue_declare(queue=queue, durable=durable)
        
        self.channel.basic_publish(
            exchange='',
            routing_key=routing_key,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        log.info(" [x] Sent %r" % message)
        self.connection.close()

    def consume_task(self, queue:str, durable:bool , routing_key:str,  callback:function):
        self.channel.queue_declare(queue=queue, durable=durable)
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=queue, auto_ack = True,on_message_callback=callback)
        self.channel.start_consuming()
