import maxflow


class Graph():
	def __init__(self, nbnodes, nbarcs):
		self.graph = maxflow.Graph[int](nbnodes, nbarcs)
		self.grEnergy = 0

	def add_binvar(self,ws,wt):
		node= self.graph.add_nodes(1)[0]
		self.graph.add_tedge(node,wt,ws)
		return node
	
	def energyEdge1(self,node,ws,wt):
		self.graph.add_tedge(node,wt,ws)
	
	def energyEdge2(self,node1,node2,E00,E01,E10,E11):
		self.graph.add_tedge(node1,E11,E01)
		self.graph.add_tedge(node2,0,E00-E01)
		self.graph.add_edge(node1,node2,0,E01+E10-E00-E11)
	
	def maxweight(self, node1, node2, occ):
		self.graph.add_edge(node1, node2, occ, 0)

	def minimize(self):
		returnval = self.grEnergy+ self.graph.maxflow()
		print("HI ITS YA BOY MAXFLOW AND I AM RETURNING: ",returnval)
		print(self.graph.get_edge_count())
		return returnval
	
	def get_var(self,node):
		return self.graph.get_segment(node)

