import evolution as evo
import activationfunction as act
import neuralnetwork

import time
import pudb

nnet = neuralnetwork.makeNNet(6, 1, 1, act.s_linear, act.s_linear)

def xor(row):
	truth_count = 0
	for a in row:
		if a == 1:
			truth_count += 1
	return truth_count == 1 or truth_count == 3 or truth_count == 5

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

inputs = truthtable(6)
targets = [xor(x) for x in inputs]
previous_error = 0
wait_till = 0
tm = time.time()
for i in range(10000):
	for x, t in zip(inputs, targets):
		this_error = nnet.learn(x, t*1)

		if abs(this_error-previous_error) < 0.001 and time.time() - tm > 5:
			nnet.hidden_layer.append(evo.addNode(nnet.nodes))
			print str(time.time() - tm) + "\r";
			tm = time.time()
		previous_error = this_error

for x, t in zip(inputs, targets):
	ans =  interpret(nnet.feedForward(x))
	print x, ans, ans == xor(x)
