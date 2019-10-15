from bspump import Sink
import asyncio
import typing
import logging


L = logging.getLogger(__name__)


class MongoSink(Sink):

    def __init__(self, app, pipeline, connection, id=None, config=None):
        super().__init__(app, pipeline, id, config)

        self.Connection = pipeline.locate_connection(app, connection)

    def process(self, context, event: typing.Union[dict, str, bytes]):
        if type(event) == list:
            pass
        elif type  (event) == dict:

            print(event)
            print(context)
            asyncio.create_task(self.insert_item(events=event))
        else:
            return ValueError

    async def insert_item(self, events):

        db = self.Connection.Client["item_city"]

        await db.test_collection.insert_one(events)
