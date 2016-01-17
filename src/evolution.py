### Rules of adding nodes: to choose the parent and child for a new node, either:
### let the parent be one of the input nodes, the child be one of the output nodes,
### or the parent and child be a ancestor and decendant of some particular node in the network
### -- This should have the effect of somewhat modularizing the neural network
import random

def getParent(source_node):
	return __getParent(source_node, 0)

def __getParent(source_node, num_steps):
	# recursively chooses an ansestor of source_node and returns it
	if source_node.isInput:
		return random.uniform(1, num_steps + 1)

	arc = random.choice(source_node.incoming)
	next_step = num_steps + 1
	choice = getParent(arc.parent, next_step)

	if choice == num_steps:
		return source_node
	else:
		return choice

def addNode(node_collection):
	source_node = random.choice(node_collection)
	parent = getParent(source_node)