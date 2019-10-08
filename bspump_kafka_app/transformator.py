import bspump.common
import bspump


class Transformator(bspump.common.MappingTransformator):

	def build(self, app):
		return {
			'title': self.category,
		}


	def category(self, key, value):
		return key, value.upper()


class ProcessorExample(bspump.Processor):

	def __init__(self, app, pipeline, id=None, config=None):
		super().__init__(app, pipeline, id, config)

	def process(self, context, event):
		event["foo"] = "bar"
		event["fest"] = "test"
		return event  # Pass event to the following processor