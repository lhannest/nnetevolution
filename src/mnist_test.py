import activationfunction as act
import neuralnetwork
import data.mnist as mnist
import pudb
import printing

def mux(number):
	result = [0 for i in range(10)]
	result[number] = 1
	return result

def demux(numbers):
	max_index = 0
	for i, n in enumerate(numbers):
		if n > numbers[max_index]:
			max_index = i
	return max_index

path = "/home/lance/git/nnetevolution/src/data"
# Images are 28x28 pixels. Reshapen, they are 784x1
training = [(mux(label), image.reshape(784)/255.0) for label, image in mnist.read(path=path, dataset="training")]
testing = [(mux(label), image.reshape(784)/255.0) for label, image in mnist.read(path=path, dataset="testing")]


a = neuralnetwork.makeSquareConvolution(2, 14)
# pudb.set_trace()
b = neuralnetwork.makeSquareConvolution(2, 7)
nnet = neuralnetwork.makeNNet(49, 10, 10, act.sigmoid, act.relu)
deepnet = neuralnetwork.DeepNet([a, b, nnet])

l = len(training)
k = 1
p = printing.printer(1)
for t, x in training:
	deepnet.learn(x, t)
	p.reprint("iteration: " + str(k) + "/" + str(l))
	k += 1
print
print "finished..."

count = 0
for t, x in testing:
	y = demux(deepnet.feedForward(x))
	if y == demux(t):
		count += 1

print
print count, len(testing)