from node import Node
from arc import Arc
from nnet import NNet
from evolution import getAncestor, getDescendant, addNode

import pudb

nodes = []
for i in range(3): nodes.append(Node())
for p, c in zip(nodes[:-1], nodes[1:]): Arc(p, c)

nnet = NNet(nodes)
a = addNode(nnet.input_layer + nnet.hidden_layer + nnet.output_layer)
b = addNode(nnet.input_layer + nnet.hidden_layer + nnet.output_layer)
c = addNode(nnet.input_layer + nnet.hidden_layer + nnet.output_layer)
d = addNode(nnet.input_layer + nnet.hidden_layer + nnet.output_layer)
e = addNode(nnet.input_layer + nnet.hidden_layer + nnet.output_layer)

nnet.hidden_layer.append(a)
nnet.hidden_layer.append(b)
nnet.hidden_layer.append(c)
nnet.hidden_layer.append(d)
nnet.hidden_layer.append(e)

print len(nnet.input_layer)
print len(nnet.hidden_layer)
print len(nnet.output_layer)