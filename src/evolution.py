### Rules of adding nodes: to choose the parent and child for a new node, either:
### let the parent be one of the input nodes, the child be one of the output nodes,
### or the parent and child be a ancestor and decendant of some particular node in the network
### -- This should have the effect of somewhat modularizing the neural network
import random

def getParent(source_node, num_steps=0):
	# a recurrsive function that counts the number of ancestors of
	# source_node and then randomly chooses one to return
	arc = random.choice(source_node.incoming)


def addNode(node_collection):
	source_node = random.choice(node_collection)
	parent = getParent(source_node)