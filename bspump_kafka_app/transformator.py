import bspump.common


class Transformator(bspump.common.MappingTransformator):

	def build(self, app):
		return self

	def test(self, key, value):
		return key, value.upper()
