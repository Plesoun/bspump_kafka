import bspump
import bspump.kafka
import bspump.mongodb
from bspump_kafka_app.pipeline import KafkaPipeline


class BlankAppApplication(bspump.BSPumpApplication):

    def __init__(self):
        super().__init__()
        svc = self.get_service("bspump.PumpService")

        svc.add_connection(
            bspump.kafka.KafkaConnection(self, "KafkaConnection")
        )
        svc.add_connection(
            bspump.mongodb.MongoDBConnection(self, "MongoDBConnection",{'host': 'mongodb://ples:test@alb-shard'
                                                                                '-00-00-kalae.mongodb.net:27017,'
                                                                                'alb-shard-00-01-kalae.mongodb.net'
                                                                                ':27017,'
                                                                                'alb-shard-00-02-kalae.mongodb.net'
                                                                                ':27017/test?ssl=true&replicaSet=alb'
                                                                                '-shard-0&authSource=admin'
                                                                                '&retryWrites=true&w=majority',
                                                                        "username": "ples",
                                                                        "password": "test",
                                                              "database": "database"}),)

        svc.add_pipeline(
            KafkaPipeline(self, "KafkaPipeline")
        )
