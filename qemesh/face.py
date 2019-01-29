import uuid

class Face:
	def __init__(self, cell):
		self.id = uuid.uuid4()
		self.cell = cell
		self.edge = 0
		self.cell.add_face(self)

	def add_edge(self, edge):
		self.edge = edge

	def remove_edge(self, edge):
		next = edge.onext()
		self.edge = next if next != None else next
	
	@staticmethod
	def make(cell):
		return Face(cell)