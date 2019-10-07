#!/usr/bin/env python3
from bspump_kafka_app.app import BlankAppApplication
from bspump_kafka_app.pipeline import KafkaPipeline
import bspump.kafka

if __name__ == '__main__':
    app = BlankAppApplication()

    svc = app.get_service("bspump.PumpService")

    svc.add_connection(
        bspump.kafka.KafkaConnection(app, "KafkaConnection")
    )

    svc.add_pipeline(
        KafkaPipeline(app, "KafkaPipeline")
    )


    app.run()
