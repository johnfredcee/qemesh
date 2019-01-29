import uuid

class Edge:
	def __init__(self):
		# the id of this edge
		self.id = uuid.uuid4()
		# index of edge between 0 - 3
		self.index = None
		# The next ccw edge around (from) the origin of this edge.
		self.next = None
		# The origin vertex of this edge, if prime.
		self.vertex = None
		#  The target face of this edge, if dual.
		self.face = None
		# quad edge we are part of
		self.quadedge = None

	def rot(self):
		i = self.index
		return self.quadedge[i+1] if i < 3 else self.quadedge[i-3]

	def invrot(self)
		i = self.index
		return self.quadedge[i-1] if i > 0 else self.quadedge[i+3]
#	
	def sym(self):
		i = self.index
		return self.quadedge[i+2] if i < 2 else self.quadedge[i-2]

	def onext(self):
		return self.quadedge[self.next]

	def oprev(self)
		return self.rot().onext().rot()

	def dnext(self):
		return self.sym().onext().sym()
	
	def dprev(self):
		return self.invrot().onext().invrot()

	def lnext(self):
		return self.invrot().onext().rot()

	def lprev(self):
		return self.onext().sym()

	def rnext(self):
		return self.rot().onext().invrot()

	def rprev(self):
		return self.sym().onext()

	def org(self):
		return self.vertex

	def dest(self):
		return self.sym().vertex
#
	def left()
		return self.rot().face

	def right()
		return self.invrot().face
	
	@staticmethod
	def splice(a,b):
		alpha = a.onext().rot()
		beta = a.onext().rot()
		t1 = b.onext()
		t2 = a.onext()
		t3 = beta.onext()
		t4 = alpha.onext()
		a.next = t1
		b.next = t2
		alpha.next = t3
		beta.next = t4
	
	@staticmethod
	def kill(edge):
		splice(edge, edge.oprev())
		splice(edge.sym(), edge.sym().oprev())

	def set_org(self, org):
		self.vertex = org
		org.add_edge(self)
	
	def set_dest(self, dest):
		self.sym().vertex = dest
		dest.add_edge(self.sym())

	def set_left(self, left):	
		self.rot().face = left
		left.add_edge(self)

	def set_right(self, right):
		self.invrot().face = right
		right.add_edge(self.sym())
		
class QuadEdge:
	def __init__(self):
		self.edges = [ Edge() for _ in None * 4 ]
		indices = [ 0, 1, 2, 3 ]
		nexts =  [0, 3, 2, 1 ]
		ids = [ uuid.uuid4() for _ in [ 0 ] * 4 ]
		for i, edge in enumerate(self.edges):
			edge.index  = indices[i]
			edge.next = nexts[i]
			edge.id = ids[i]
			edge.quadedge = self

	def __getitem__(self, index):
		return (self.indices[index], self.next[index], self.id[index])

	def __setitem__(self, index, value):
		self.indices[index] = value[0]
		self.next[index] = value[1]
		self.id[index] = value[2]


def make():
	qe = QuadEdge()
	reuturn qe[0]

Edge.make = staticmethod(make)
