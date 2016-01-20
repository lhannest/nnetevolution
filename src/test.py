from node import InputNode, HiddenNode, OutputNode
from arc import Arc
from nnet import NNet
from evolution import getAncestor, getDescendant, addNode, splitArc, copy
import networkx as nx
import matplotlib.pyplot as plt
import pylab

import pudb

def makeTuple(arc):
	return (str(arc.parent.innovation_number), str(arc.child.innovation_number))


a = InputNode()
b = HiddenNode()
c = OutputNode()
Arc(a, b)
Arc(b, c)

print a.__repr__(), b.__repr__(), c.__repr__()

nnet = NNet([a, b, c])

for i in range(1):
	n = addNode(nnet.input_layer + nnet.hidden_layer + nnet.output_layer)
	nnet.hidden_layer.append(n)
	n = splitArc(nnet.input_layer + nnet.hidden_layer + nnet.output_layer)
	nnet.hidden_layer.append(n)

G = nx.DiGraph()

arcs = []
for n in nnet.nodes:
	for a in n.incoming:
		arcs.append(makeTuple(a))
G.add_edges_from(arcs)

pos = nx.spring_layout(G)
nx.draw(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()

nnet = copy(nnet)

G = nx.DiGraph()

arcs = []
for n in nnet.nodes:
	for a in n.incoming:
		arcs.append(makeTuple(a))
G.add_edges_from(arcs)

pos = nx.spring_layout(G)
nx.draw(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()