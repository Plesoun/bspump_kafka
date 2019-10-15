import motor.motor_asyncio
import asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(
	'mongodb://ples:test@alb-shard-00-00-kalae.mongodb.net:27017,alb-shard-00-01-kalae.mongodb.net:27017,'
	'alb-shard-00-02-kalae.mongodb.net:27017/test?ssl=true&replicaSet=alb-shard-0&authSource=admin&retryWrites=true&w'
	'=majority')
db = client["item_city"]


async def do_insert():
	document = {'key': 'value'}
	await db.test_collection.insert_one(document)
#	print('inserted %d docs' % (len(result.inserted_ids),))


loop = asyncio.get_event_loop()
loop.run_until_complete(do_insert())



from bspump.elasticsearch import ElasticSearchConnection
from bspump.kafka import KafkaSink
from bspump.postgresql import PostgreSQLConnection
from bspump.postgresql import PostgreSQLSink
from bspump.mongodb import MongoDBLookup
