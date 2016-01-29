import activationfunction as act
import neuralnetwork
import data.mnist as mnist
import pudb

path = "/home/lance/git/nnetevolution/src/data"
inputs = []
targets = []
# Images are 28x28 pixels. Reshapen, they are 784x1
for label, image in mnist.read(path=path):
	targets.append(label)
	inputs.append(image.reshape(784) / 255.0)

a = neuralnetwork.makeSquareConvolution(2, 14)
b = neuralnetwork.makeSquareConvolution(2, 7)

nnet = neuralnetwork.makeNNet(49, 50, 10)

for x, t in zip(inputs, targets):
	nnet.learn