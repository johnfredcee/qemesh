import uuid
import euclid
from euclid import Vector3

class Vertex:
	def __init__(self, cell):
		self.id = uuid.uuid4()
		self.pos = Vector3(0,0,0)
		self.cell = cell
		self.edge = 0
		self.cell.add_vertex(self)

	def add_edge(self, edge):
		self.edge = edge
	
	def remove_edge(self, edge):
		next = edge.onext()
		self.edge = next if next != None else 0
	
	def kill(self):
		self.cell.remove_vertex()

	@staticmethod
	def make(cell):
		return Vertex(cell)