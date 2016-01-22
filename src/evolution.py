### Rules of adding nodes: to choose the parent and child for a new node, either:
### let the parent be one of the input nodes, the child be one of the output nodes,
### or the parent and child be a ancestor and decendant of some particular node in the network
### -- This should have the effect of somewhat modularizing the neural network
import random
import pudb
from node import HiddenNode, BiasNode
from arc import Arc
from node import InputNode, OutputNode, getGlobalBiasNode
from neuralnetwork import NNet

def getAncestor(node):
	if type(node) is InputNode:
		return node
	else:
		arc = random.choice(fix_arc_list(node.incoming))
		return __getAncestor(arc.parent)

def __getAncestor(node, collection=[]):
	collection.append(node)

	if type(node) is InputNode:
		choice = random.choice(collection)
		return choice

	arc = random.choice(fix_arc_list(node.incoming))
	return __getAncestor(arc.parent, collection)

def fix_arc_list(arc_collection):
	arcs = []
	for arc in arc_collection:
		if type(arc.parent) != BiasNode:
			arcs.append(arc)
	return arcs

def getDescendant(node):
	if type(node) is OutputNode:
		return node
	else:
		arc = random.choice(node.outgoing)
		return __getDescendant(arc.child)

def __getDescendant(node, collection=[]):
	collection.append(node)

	if type(node) is OutputNode:
		choice = random.choice(collection)
		return choice

	arc = random.choice(node.outgoing)
	return __getDescendant(arc.child, collection)

def addNode(node_collection):
	source_node = random.choice(node_collection)
	parent = getAncestor(source_node)
	child = getDescendant(source_node)
	new_node = HiddenNode()
	Arc(parent, new_node)
	Arc(new_node, child)
	return new_node

def splitArc(node_collection):
	node = random.choice(node_collection)
	arc = random.choice(node.incoming + node.outgoing)
	new_node = HiddenNode()
	Arc(arc.parent, new_node)
	Arc(new_node, arc.child)
	del arc
	return new_node

def copy(nnet):
	nodes = [node.copy() for node in nnet.nodes]
	nodes_with_bias = nodes + [getGlobalBiasNode()]
	arcs = []
	for arc in getArcs(nnet):
		parent = getMember(arc.parent, nodes_with_bias)
		child = getMember(arc.child, nodes_with_bias)
		arc.copy(parent, child)
	return NNet(nodes)

def getMember(obj, collection):
	for item in collection:
		if obj == item:
			return item
	assert False, str(obj) + ' is not in ' + str(collection)

def getArcs(nnet):
	arcs = []
	for node in nnet.nodes:
		for arc in node.incoming:
			arcs.append(arc)
	return arcs