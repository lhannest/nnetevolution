from tools.uniquelist import UniqueList

class Node(object):
	def __init__(self):
		self.__innovation = 0

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
			return self.__innovation == other.__innovation