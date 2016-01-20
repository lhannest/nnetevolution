from tools.uniquelist import UniqueList
from arc import Arc

INNOVATION_NUMBER = 0

def getNextInnovation():
	global INNOVATION_NUMBER
	INNOVATION_NUMBER += 1
	return INNOVATION_NUMBER

class Node(object):
	def __init__(self):
		self.innovation_number = getNextInnovation()

		self.incoming = UniqueList()
		self.outgoing = UniqueList()

	def copy(self):
		node = Node()
		node.innovation_number = self.innovation_number
		return node

	@property
	def isInput(self):
		return len(self.incoming) == 0

	@property
	def isOutput(self):
		return len(self.outgoing) == 0

	def __eq__(self, other):
		if isinstance(other, Node):
			return self.innovation_number == other.innovation_number

	def __repr__(self):
		return 'Node[' + str(self.innovation_number) + ']'

class BiasNode(Node):
	def __init__(self):
		Node.__init__(self)
		self.innovation_number = 0
		self.incoming = tuple()
		self.outgoing = UniqueList()
		self.isInput = True
		self.isOutput = False
	def __repr__(self):
		return 'BiasNode[' + self.innovation_number + ']'