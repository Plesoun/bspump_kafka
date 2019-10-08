from bspump.analyzer import SessionAnalyzer
import logging

L = logging.getLogger(__name__)


class GraphSessionAnalyzer(SessionAnalyzer):

	def __init__(self, app, pipeline, id=None, config=None):
		super().__init__(app, pipeline, dtype=[('user_link', 'U40'), ('duration', 'i8')], analyze_on_clock=True, id=id,
		                 config=config)

	def predicate(self, context, event):
		if "foo" not in event:
			return False

		if "cast" not in event:
			return False

		if "year" not in event:
			return False

		return True

	def evaluate(self, context, event):

		cast = event["cast"]
		for i in cast:
			if i not in self.Sessions.N2IMap:
				self.Sessions.add_row(i + "." + event["title"].lower())

	def analyze(self):
		graph = {}
		sessions_snapshot = self.Sessions.Array
		for i in range(0, sessions_snapshot.shape[0]):
			if i in self.Sessions.ClosedRows:
				continue

			cast = self.Sessions.I2NMap

			for j in cast:
				if cast[j].split(".")[0][0] == "T":
					#print(cast[j].split(".")[0])
					graph.update({f"{j}": cast[j].split(".")[0]})

		self.Sessions.flush()
		L.warning("Graph is {}".format(graph))
