#!/usr/bin/env python3
import bspump
import bspump.common
import bspump.kafka
from bspump_kafka_app.transformator import Transformator


class KafkaPipeline(bspump.Pipeline):

    def __init__(self, app, pipeline_id):
        super().__init__(app, pipeline_id)
        self.build(
            bspump.kafka.KafkaSource(app, self, "KafkaConnection", config={'topic': 'test'}),
            bspump.common.BytesToStringParser(app, self),
            bspump.common.PPrintProcessor(app, self),
            Transformator(app, self),
#            bspump.common.MappingItemsProcessor(app, self),
            bspump.common.PPrintSink(app, self),
            bspump.kafka.KafkaSink(app, self, "KafkaConnection", config={'topic': 'messages'}),
        )
