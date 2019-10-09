import bspump.common
import bspump
import pandas as pd


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
		df = pd.DataFrame.from_dict({"cast": event["cast"]})
		df.iloc[-1] = "The Someone else"
		event["pandas"] = df["cast"]
		if event["title"] == "JURASSIC PARK":
			event["cast"].append("The Stunt")
		return event  # Pass event to the following processor