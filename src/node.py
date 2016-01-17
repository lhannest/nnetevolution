from tools.uniquelist import UniqueList

INNOVATION_NUMBER = 0

def getNextInnovation():
	global INNOVATION_NUMBER
	INNOVATION_NUMBER += 1
	return INNOVATION_NUMBER

class Node(object):
	def __init__(self):
		# This number will be unique for every node if left untouched
		self.innovation_number = getNextInnovation()

		self.incoming = UniqueList()
		self.outgoing = UniqueList()

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