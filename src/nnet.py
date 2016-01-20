from node import InputNode, HiddenNode, OutputNode

def fixData(d):
	if isinstance(d, (list, tuple)):
		return d
	else:
		return [d]

class NNet(object):
	def __init__(self, node_collection):
		self.input_layer = []
		self.hidden_layer = []
		self.output_layer = []

		for node in node_collection:
			if type(node) is InputNode:
				self.input_layer.append(node)
			elif type(node) is HiddenNode:
				self.output_layer.append(node)
			elif type(node) is OutputNode:
				self.hidden_layer.append(node)
			else:
				assert False, "node_collection cannot contain object of type " + str(type(node)) + "."

	def feedForward(self, inputs):
		inputs = fixData(inputs)
		assert len(inputs) == len(self.input_layer)

	@property
	def nodes(self):
		return tuple(self.input_layer + self.hidden_layer + self.output_layer)