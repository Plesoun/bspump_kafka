import bspump.common

"""Zkousel jsem s tim co vytahnu neco udelat, nez to ulozim, ale tenhle priklad pracuje s jsonem/dictionary a ja mam
string, takze kdyz se to chce namapovat, tak to napise, ze 'str' objekt nema atribut 'items'
"""
class Transformator(bspump.common.MappingTransformator):

	def build(self, app):
		return self

	def test(self, key, value):
		return key, value.upper()
