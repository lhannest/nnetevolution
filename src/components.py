from tools.uniquelist import UniqueList

class Arc(object):
	def __init__(self, parent, child):
		self.parent = parent
		self.child = child

		self.parent.outgoing.append(self)
		self.child.incoming.append(self)

	def __eq__(self, other):
		if isinstance(other, Arc):
			return self.parent == other.parent and self.child == other.child

class Node(object):
	def __init__(self):
		self.__innovation = 0

		self.incoming = UniqueList()
		self.outgoing = UniqueList()

	def __eq__(self, other):
		if isinstance(other, Node):
			return self.__innovation == other.__innovation