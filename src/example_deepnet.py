import evolution as evo
import activationfunction as act
import neuralnetwork

import time
import pudb

def xor(row):
	truth_count = 0
	for p in row:
		if p :
			truth_count += 1
	return 1 * (truth_count == 1)

def truthtable (n):
	if n < 1:
		return [[]]
	subtable = truthtable(n-1)
	return [ row + [v] for row in subtable for v in [0,1] ]

def interpret(v):
	if v[0] > v[1]:
		return 1
	else:
		return 0

a = neuralnetwork.makeNNet(3, 3, 3, act.relu, act.relu)
b = neuralnetwork.makeNNet(3, 2, 1, act.relu, act.relu)

deepnet = neuralnetwork.DeepNet([a, b])

inputs = truthtable(3)
targets = [xor(x) for x in inputs]
for i in range(3000):
	for x, t in zip(inputs, targets):
		deepnet.learn(x, t, 0.01)

for x, t in zip(inputs, targets):
	print t, x, deepnet.feedForward(x)