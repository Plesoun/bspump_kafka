import bspump.common
import bspump

"""Zkousel jsem s tim co vytahnu neco udelat, nez to ulozim, ale tenhle priklad pracuje s jsonem/dictionary a ja mam
string, takze kdyz se to chce namapovat, tak to napise, ze 'str' objekt nema atribut 'items'
"""


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