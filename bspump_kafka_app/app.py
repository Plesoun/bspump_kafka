import bspump
import bspump.kafka
from bspump_kafka_app.pipeline import KafkaPipeline

"""Tady ta hlavni trida je divna, pokud je tam 'async def main(self) tak to nejak castecne ignoruje to co je pod tim,
kdyz tam dam misto 'main' initialize, tak to zase nemuze najit 'PumpService', funguje to, pokud to co je ted
zakomentovane presunu do 'bspump_kafka.py'"""

class BlankAppApplication(bspump.BSPumpApplication):

    async def main(self):
        svc = self.get_service("bspump.PumpService")

#        svc.add_connection(
#            bspump.kafka.KafkaConnection(self, "KafkaConnection")
#        )

#        svc.add_pipeline(
#            KafkaPipeline(self, "KafkaPipeline")
#        )

