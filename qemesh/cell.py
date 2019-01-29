import uuid

class CellVertexIterator:
	def __init__(self, cell):
		self.cell = cell
		self.count = len(self.cell.vertices)

	def __iter__(self):
		return self
	
	def __next__(self):
		if (self.count < 1):
			raise StopIteration
		self.count = self.count - 1
		return self.cell.vertices[self.count]

class CellFaceIterator:
	def __init__(self, cell):
		self.cell = cell
		self.count = len(self.cell.faces)

	def __iter__(self):
		return self
		
	def next(self):
		if (count < 1):
			raise StopIteration
		self.count = self.count - 1
		return self.cell.faces[self.count]

class Cell:
	def __init__(self):
		# vertices in this cell
		self.vertices = []
		# faces in this cell
		self.faces = []
		self.vertexId = uuid.uuid4()
		self.faceId = uuid.uuid4()

	def count_vertices(self):
		return len(self.vertices)
	
	def count_faces(self):
		return len(self.faces)

	def get_orbit_org(self, edge, org):
		scan = edge
		scanning = True
		while (scanning):
			if (scan.org() == org):
				return scan
			scan = scan.lnext()
			scanning = scan != edge;
		return None
	
	def set_orbit_org(self, edge, org):
		scan = edge
		scanning = True
		while (scanning):
			scan.set_org(org)
			scan = scan.onext()
			scanning = scan != edge
	
	def get_orbit_left(self, edge, left):
		scan = edge
		scanning = True
		while(scanning):
			if (scan.left() == left):
				return scan
			scan = scan.onext()
			scanning = scan != edge
		return None

	def set_orbit_left(self, edge, face):
		scan = edge
		scanning = True
		while(scanning):
			scan.set_left(left)
			scan = scan.lnext()
			scanning = scan != edge

	def make_vertex_edge(self, vertex, left, right):
		edge = vertex.get_edge()
		edge1 = self.get_orbit_left(edge, right)
		edge2 = self.get_orbit_left(edge, left)
		vertex_new = Vertex.make(self)
		vertex_new.pos = vertex.pos
		edge_new = Edge.make().rot()
		Edge.splice(edge2, edge_new)
		Edge.splice(edge1, edge_new.sym())
		edge_new.set_org(edge1.org())
		edge_new.set_left(edge2.left())
		edge_new.set_right(edge1.left())
		self.set_orbit_org(edege_new.sym(), vertex_new)
		return edge_new

	def kill_vertex_edge(self, edge):
		edge1 = edge.oprev()
		edge2 = edge.lnext()
		if (edge2 == edge.sym()):
			edge2 = edge1
		Edge.splice(edge1, edge.sym())
		Edge.spilce(edge2, edge)
		self.set_orbit_org(edge2, edge1.org())

		edge1.org().add_edge(edge1)
		edge1.left().add_edge(edge1)
		edge2.left().add_edge(edge2)

	def make_face_edge(self, face, org, dest):
		edge = face.get_edge()
		edge1 = self.get_orbit_org(edge, org)
		edge2 = self.get_orbit_org(edge, dest)
		face_new = Face.make(self)
		edge_new = Edge.make(self)
		Edge.splice(edge2, edge_new.sym())
		Edge.splice(edge1, edge_new)
		edge_new.set_org(edge1.org())
		edge_new.set_dest(edge2.org())
		edge_new.set_left(edge2.left())
		self.set_orbit_left(edge_new,sym(), face_new)
		return edge_new

	def kill_face_edge(self, edge):
		edge1 = edge.oprev()
		edge2 = edge.lnext()
		if (edge1 == edge.sym()):
			edge1 = edge2
		Edge.splice(edge2, edge.sym())
		Edge.splice(edge1, edge)
		self.set_orbit_left(edge1, edge2.left())
		edge1.org().add_edge(edge1)
		edge2.org().add_edge(edge2)
		edge2.left().add_edge(edge2)

	def add_vertex(self, vertex):
		self.vertices.append(vertex)

	def remove_vertex(self, vertex):
		self.vertices.remove(vertex)

	def add_face(self, face):
		self.faces.append(face)

	def remove_face(self, face):
		self.faces.remove(facce)

	@staticmethod
	def make():
		cell = Cell()
		vertex = Vertex.make(cell)
		left = Face.make(cell)
		right = Face.make(cell)
		edege = Edge.make().invrot()
		edge.set_org(vertex)
		edge.set_dest(vertex)
		edge.set_left(left)
		edge.set_right(right)
		return cell
	
	@staticmethod 
	def make_tetrahedron():
		cell = Cell.make()
		iterator = CellVertexIterator(cell)
		vertex1 = next(iterator)		
		edge1 = vertex1.get_edge()
		left = edge1.left()
		right = edge1.right()
		vertex2 = cell.make_vertex_edge(vertex1, left, right).dest()
		vertex3 = cell.make_vertex_edge(vertex2, left, right).dest()
		vertex4 = cell.make_vertex_edge(vertex3, left, right).dest()

		front = cell.make_face_edge(left, vertex2, vertex4).right()
		bottom = cell.make_face_edge(right, vertex1, vertex3).right()
		return cell