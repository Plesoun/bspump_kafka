#!/usr/bin/env python3
import bspump
import bspump.common
import bspump.kafka
from bspump_kafka_app.transformator import Transformator, ProcessorExample
from bspump_kafka_app.analyzer import GraphSessionAnalyzer


class KafkaPipeline(bspump.Pipeline):

    def __init__(self, app, pipeline_id):
        super().__init__(app, pipeline_id)
        self.build(
            bspump.kafka.KafkaSource(app, self, "KafkaConnection", config={'topic': 'message2'}),
            bspump.common.JsonBytesToDictParser(app, self),
#            bspump.common.PPrintProcessor(app, self),
            Transformator(app, self),
            ProcessorExample(app, self),
            GraphSessionAnalyzer(app, self, config={'analyze_period':1}),
#            bspump.common.NullSink(app, self)
            bspump.common.PPrintSink(app, self),
#            bspump.kafka.KafkaSink(app, self, "KafkaConnection", config={'topic': 'messages'}),
        )
