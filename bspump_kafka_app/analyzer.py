from bspump.analyzer import SessionAnalyzer, TimeWindowAnalyzer
import bspump.random

import logging
import time

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

		start_time = time.time()
		title = event["title"]
		if title not in self.Sessions.N2IMap:
			self.Sessions.add_row(title)


	def analyze(self):
		graph = {}
		#self.Sessions.close_row('user_1')
		sessions_snapshot = self.Sessions.Array
		for i in range(0, sessions_snapshot.shape[0]):
			if i in self.Sessions.ClosedRows:
				continue

			user_from = self.Sessions.I2NMap[i]
			user_to = sessions_snapshot[i]['user_link']
			link_weight = sessions_snapshot[i]['duration']
			edge = tuple([user_to, link_weight])
			rev_edge = tuple([user_from, link_weight])
#			print(f"link_weight {link_weight}, user_from {user_from}, user_to {user_to}")

			if user_from not in graph:
				graph[user_from] = [edge]
			else:
				graph[user_from].append(edge)

			if user_to not in graph:
				graph[user_to] = [rev_edge]
			else:
				graph[user_to].append(rev_edge)
			print(f"edge {edge}, rev_edge{rev_edge}, id {user_to}")
#			self.Sessions.close_row(user_from)

		self.Sessions.flush()
		L.warning("Graph is {}".format(graph))
