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

class RabitmqConfigure(metaclass=MetaClass):
    def __init__(self, queue= 'hello', host='localhost', routingkey= 'hello', exchange= ''):
        self.queue = queue
        self.host = host
        self.routingkey = routingkey
        self.exchange = exchange

class RabbitMq():

    __slots__ = ["server", "_channel", "_connection"]

    def __init__(self, server):

        self.server = server
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))

        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self.server.queue)

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self._connection.close()


    def publish(self, payload = {}):
        self._channel.basic_publish(exchange=self.server.exchange,
                                    routing_key=self.server.routingkey,
                                    body= str(payload))
        print('Published message: {}'.format(payload))


# localhost:15672
if __name__ == '__main__':
    server = RabitmqConfigure( queue= 'hello',
                               host='localhost',
                               routingkey= 'hello',
                               exchange= '')

    with RabbitMq(server) as rabbitmq:
        rabbitmq.publish(payload= {"Name":"claudia"})

