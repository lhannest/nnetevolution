from node import InputNode, HiddenNode, OutputNode, BiasNode
from arc import Arc
from activationfunction import sigmoid, linear
import pudb

def fixData(d):
	if isinstance(d, (list, tuple)):
		return d
	else:
		return [d]

def makeNNet(input_size, hidden_size, output_size, f1=sigmoid, f2=linear):
	assert input_size >= 1 and hidden_size >= 1 and output_size >= 1

	inputs, hidden, outputs = [], [], []

	for i in range(input_size):
		inputs.append(InputNode())
	for i in range(hidden_size):
		hidden.append(HiddenNode(f1))
	for i in range(output_size):
		outputs.append(OutputNode(f2))

	for p in inputs:
		for c in hidden:
			Arc(p, c)
	for p in hidden:
		for c in outputs:
			Arc(p, c)

	return NNet(inputs + hidden + outputs)


class NNet(object):
	def __init__(self, node_collection):
		self.input_layer = []
		self.hidden_layer = []
		self.output_layer = []

		self.time = False

		for node in node_collection:
			if type(node) is InputNode:
				self.input_layer.append(node)
			elif type(node) is HiddenNode:
				self.hidden_layer.append(node)
			elif type(node) is OutputNode:
				self.output_layer.append(node)
			else:
				assert False, "node_collection cannot contain object of type " + str(type(node)) + "."

	def feedForward(self, inputs):
		inputs = fixData(inputs)
		error_message = "len(inputs) is " + str(len(inputs)) + ", expected " + str(len(self.input_layer)) + "."
		assert len(inputs) == len(self.input_layer), error_message

		for node in self.nodes:
			node.last_visited = False

		for i, node in enumerate(self.input_layer):
			node.output = inputs[i]

		return [output(node, True) for node in self.output_layer]

	def learn(self, inputs, targets, step_size=1):
		targets = fixData(targets)
		error_message = "len(targets) is " + str(len(targets)) + ", expected " + str(len(self.output_layer)) + "."
		assert len(targets) == len(self.output_layer), error_message

		outputs = self.feedForward(inputs)

		sqr_error = 0

		for i, node in enumerate(self.output_layer):
			node.error = outputs[i] - targets[i]
			sqr_error += node.error**2

		for node in self.input_layer:
			error(node, False)

		for node in self.hidden_layer + self.output_layer:
			for arc in node.incoming:
				arc.weight -= step_size * arc.parent.output * arc.child.error

		return sqr_error/2

	@property
	def nodes(self):
		return tuple(self.input_layer + self.hidden_layer + self.output_layer)

def output(node, time):
	if type(node) == InputNode or type(node) == BiasNode or node.last_visited == time:
		node.last_visited = time
		return node.output
	else:
		node.last_visited = time
		weighted_sum = 0
		for arc in node.incoming:
			weighted_sum += output(arc.parent, time) * arc.weight
		node.output, node.derivative = node.activationFunction(weighted_sum)
		return node.output

def error(node, time):
	if type(node) == OutputNode or node.last_visited == time:
		node.last_visited = time
		return node.error
	else:
		node.last_visited = time
		weighted_sum = 0
		for arc in node.outgoing:
			weighted_sum += error(arc.child, time) * arc.weight
		node.error = weighted_sum * node.derivative
		return node.error