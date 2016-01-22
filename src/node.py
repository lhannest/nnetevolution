from tools.uniquelist import UniqueList
from arc import Arc
import activationfunction as actf

INNOVATION_NUMBER = 0

def getNextInnovation():
	global INNOVATION_NUMBER
	INNOVATION_NUMBER += 1
	return INNOVATION_NUMBER

class _BaseNode(object):
	def __init__(self, innovation_number=None, activation_function=None):
		if innovation_number is None:
			self.innovation_number = getNextInnovation()
		else:
			self.innovation_number = innovation_number

		if activation_function == None:
			self.activationFunction = actf.sigmoid
		else:
			self.activationFunction = activation_function

		self.last_visited = False
		self.output = 0
		self.incoming = UniqueList()
		self.outgoing = UniqueList()
	def __repr__(self):
		return type(self).__name__ + '[' + str(self.innovation_number) + ']'
	def __eq__(self, other):
		if isinstance(other, _BaseNode):
			return self.innovation_number == other.innovation_number
	def connect(self, *others):
		for other in others:
			Arc(self, other)
	def copy(self):
		copy = self.__class__()
		copy.innovation_number = self.innovation_number
		return copy

class BiasNode(_BaseNode):
	def __init__(self):
		_BaseNode.__init__(self, 0)
		self.incoming = tuple()
		self.outgoing = UniqueList()
		self.output = 1

BIAS_NODE = BiasNode()

class InputNode(_BaseNode):
	def __init__(self):
		_BaseNode.__init__(self)
	
	# Since the input node ouputs whatever has been inputted. This is
	# needed only for calculating the error of an output, which is
	# needed only if we're backpropegating the error beyond a single
	# neural network.
	@property
	def derivative(self):
		return 1

class HiddenNode(_BaseNode):
	def __init__(self, activation_function=None):
		_BaseNode.__init__(self, activation_function=activation_function)
		global BIAS_NODE
		Arc(BIAS_NODE, self)

class OutputNode(_BaseNode):
	def __init__(self, activation_function=None):
		_BaseNode.__init__(self, activation_function=activation_function)
		global BIAS_NODE
		Arc(BIAS_NODE, self)

def getGlobalBiasNode():
	global BIAS_NODE
	return BIAS_NODE