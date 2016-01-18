from node import Node
from arc import Arc
from evolution import getAncestor, getDescendant

import pudb

nodes = []

for i in range(10):
	nodes.append(Node())
# 
# pudb.set_trace()
for p, c in zip(nodes[:-1], nodes[1:]):
	Arc(p, c)

choices = [0 for i in range(10)]

for i in range(1000):
	# pudb.set_trace()
	node = getDescendant(nodes[3])
	choices[node.innovation_number-1] += 1

for i in range(10):
	print i, round(choices[i] * 1.0 / 1000, 2)