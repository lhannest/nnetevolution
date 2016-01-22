import neuralnetwork
from evolution import getAncestor, getDescendant, addNode, splitArc, copy
import networkx as nx
import matplotlib.pyplot as plt
import pylab

import pudb

def makeTuple(arc):
	return (str(arc.parent.innovation_number), str(arc.child.innovation_number))

nnet = neuralnetwork.makeNNet(2, 2, 1)

for i in range(1):
	n = addNode(nnet.input_layer + nnet.hidden_layer + nnet.output_layer)
	nnet.hidden_layer.append(n)
# 	n = splitArc(nnet.input_layer + nnet.hidden_layer + nnet.output_layer)
# 	nnet.hidden_layer.append(n)

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

def truthtable (n):
	if n < 1:
		return [[]]
	subtable = truthtable(n-1)
	return [ row + [v] for row in subtable for v in [0,1] ]

inputs = truthtable(2)
targets = [((x or y) and not (x and y))*1 for x, y in inputs]
for i in range(1000):
	for x, t in zip(inputs, targets):
		# pudb.set_trace()
		nnet.learn(x, t)

for x, t in zip(inputs, targets):
	print x, nnet.feedForward(x), t