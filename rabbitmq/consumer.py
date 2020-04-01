import ast

try:
    import pika
except Exception as e:
    print("Some modules are missings {}.".format_map(e))

class MetaClass(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__( *args, **kwargs)
            return cls._instance[cls]

class RabbitMqServerConfigure(metaclass=MetaClass):
    def __init__(self, host='localhost', queue= 'hello'):
        self.host = host
        self.queue = queue

class rabbitmqServer():
    def __init__(self, server):
        self.server = server
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))
        self._channel = self._connection.channel()
        self._tem = self._channel.queue_declare(queue=self.server.queue)

    @staticmethod
    def callback(ch, method, properties, body):
        Payload = body.decode('utf-8')
        Payload = ast.literal_eval(Payload)
        print("Data received: {}".format(Payload))
        print(" [x] Received %r" % body)

    def startserver(self):
        self._channel.basic_consume(queue=self.server.queue,
                                    on_message_callback=self.callback,
                                    auto_ack=True)
        self._channel.start_consuming()

if __name__ == '__main__':
    serverconfigure = RabbitMqServerConfigure(host='localhost',
                                              queue= 'hello')
    server = rabbitmqServer(server= serverconfigure)
    server.startserver()