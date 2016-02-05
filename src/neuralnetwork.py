from node import InputNode, HiddenNode, OutputNode, BiasNode
from arc import Arc
from activationfunction import sigmoid, linear
import pudb

def makeSquareConvolution(cluster_size, output_count, fn=sigmoid):
	input_grid = [[InputNode() for i in range(cluster_size*output_count)] for j in range(cluster_size*output_count)]
	output_grid = [[OutputNode(fn) for i in range(output_count)] for j in range(output_count)]

	for i, row in enumerate(input_grid):
		for j, _ in enumerate(row):
			parent = input_grid[i][j]
			child = output_grid[i/cluster_size][j/cluster_size]
			parent.connect(child)

	input_layer = []
	output_layer = []
	for row in input_grid:
		input_layer = input_layer + row
	for row in output_grid:
		output_layer = output_layer + row

	return NNet(input_layer + output_layer)

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

class DeepNet(object):
	def __init__(self, sub_nets):
		self.sub_nets = []

		for i, nnet in enumerate(sub_nets):
			assert type(nnet) == NNet, "type of sub_nets[" + str(i) + "] is " + str(type(nnet)) + ", must be " + str(NNet)
			if i != 0:
				error_message = "sub_nets[" + str(i) + " does not have as many inputs as its predecessor has outputs"
				assert len(nnet.input_layer) == len(sub_nets[i-1].output_layer), error_message
			self.sub_nets.append(nnet)

	def feedForward(self, inputs):
		for nnet in self.sub_nets:
			inputs = nnet.feedForward(inputs)
		return inputs

	def learn(self, inputs, targets, step_size=1):
		inputs = fixData(inputs)
		targets = fixData(targets)

		outputs = self.feedForward(inputs)
		errors = [y - t for y, t in zip(outputs, targets)]
		sqr_error = [e**2 for e in errors]

		for nnet in reversed(self.sub_nets):
			errors = nnet.backpropError(errors)

		for nnet in self.sub_nets:
			nnet.updateWeights(step_size)

		return sqr_error



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

		return [_recursively_get_output(node, True) for node in self.output_layer]

	def learn(self, inputs, targets, step_size=1):
		targets = fixData(targets)
		error_message = "len(targets) is " + str(len(targets)) + ", expected " + str(len(self.output_layer)) + "."
		assert len(targets) == len(self.output_layer), error_message

		pudb.set_trace()
		outputs = self.feedForward(inputs)

		sqr_error = 0
		errors = [y - t for y, t in zip(outputs, targets)]
		for err in errors:
			sqr_error += err**2

		pudb.set_trace()

		self.backpropError(errors)
		self.updateWeights(step_size)

		return sqr_error/2

	def backpropError(self, errors):
		# pudb.set_trace()
		for node in self.nodes:
			node.last_visited = True

		for i, node in enumerate(self.output_layer):
			node.error = errors[i]

		for node in self.input_layer:
			_recursively_set_error(node, False)

		return [node.error for node in self.input_layer]

	def updateWeights(self, step_size=1):
		for node in self.hidden_layer + self.output_layer:
			for arc in node.incoming:
				arc.weight -= step_size * arc.parent.output * arc.child.error

	@property
	def nodes(self):
		return tuple(self.input_layer + self.hidden_layer + self.output_layer)

def _recursively_get_output(node, time):
	if type(node) == InputNode or type(node) == BiasNode or node.last_visited == time:
		node.last_visited = time
		return node.output
	else:
		node.last_visited = time
		weighted_sum = 0
		for arc in node.incoming:
			weighted_sum += _recursively_get_output(arc.parent, time) * arc.weight
		node.output, node.derivative = node.activationFunction(weighted_sum)
		return node.output

def _recursively_set_error(node, time):
	if type(node) == OutputNode or node.last_visited == time:
		node.last_visited = time
		return node.error
	else:
		node.last_visited = time
		weighted_sum = 0
		for arc in node.outgoing:
			weighted_sum += _recursively_set_error(arc.child, time) * arc.weight
		node.error = weighted_sum * node.derivative
		return node.error

def fixData(d):
	if isinstance(d, (list, tuple)):
		return d
	else:
		return [d]