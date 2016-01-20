from node import Node, BiasNode
from arc import Arc

def fixData(d):
	if isinstance(d, (list, tuple)):
		return d
	else:
		return [d]

class NNet(object):
	def __init__(self, nodes):
		self.input_layer = []
		self.hidden_layer = []
		self.output_layer = []

		for node in nodes:
			if node.isInput:
				self.input_layer.append(node)
			elif node.isOutput:
				self.output_layer.append(node)
			else:
				self.hidden_layer.append(node)

	def feedForward(self, inputs):
		inputs = fixData(inputs)
		assert len(inputs) == len(self.input_layer)

	@property
	def nodes(self):
		return tuple(self.input_layer + self.hidden_layer + self.output_layer)