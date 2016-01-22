import neuralnetwork

nnet = neuralnetwork.makeNNet(2, 20, 1)


def truthtable (n):
	if n < 1:
		return [[]]
	subtable = truthtable(n-1)
	return [ row + [v] for row in subtable for v in [0,1] ]

inputs = truthtable(2)
targets = [((x or y) and not (x and y))*1 for x, y in inputs]
for i in range(10000):
	for x, t in zip(inputs, targets):
		# pudb.set_trace()
		nnet.learn(x, t)

for x, t in zip(inputs, targets):
	print x, nnet.feedForward(x)[0]