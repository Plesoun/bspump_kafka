import bspump
import bspump.kafka
from bspump_kafka_app.pipeline import KafkaPipeline


class BlankAppApplication(bspump.BSPumpApplication):

    def __init__(self):
        super().__init__()
        svc = self.get_service("bspump.PumpService")

        svc.add_connection(
            bspump.kafka.KafkaConnection(self, "KafkaConnection")
        )

        svc.add_pipeline(
            KafkaPipeline(self, "KafkaPipeline")
        )
