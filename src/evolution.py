### Rules of adding nodes: to choose the parent and child for a new node, either:
### let the parent be one of the input nodes, the child be one of the output nodes,
### or the parent and child be a ancestor and decendant of some particular node in the network
### -- This should have the effect of somewhat modularizing the neural network
import random
import pudb
from node import Node
from arc import Arc

def getAncestor(node):
	if node.isInput:
		return node
	else:
		arc = random.choice(node.incoming)
		return __getAncestor(arc.parent)

def __getAncestor(node, collection=[]):
	collection.append(node)

	if node.isInput:
		choice = random.choice(collection)
		return choice

	arc = random.choice(node.incoming)
	return __getAncestor(arc.parent, collection)

def getDescendant(node):
	if node.isOutput:
		return node
	else:
		arc = random.choice(node.outgoing)
		return __getDescendant(arc.child)

def __getDescendant(node, collection=[]):
	collection.append(node)

	if node.isOutput:
		choice = random.choice(collection)
		return choice

	arc = random.choice(node.outgoing)
	return __getDescendant(arc.child, collection)

def addNode(node_collection):
	source_node = random.choice(node_collection)
	parent = getAncestor(source_node)
	child = getDescendant(source_node)
	new_node = Node()
	Arc(parent, new_node)
	Arc(new_node, child)
	return new_node