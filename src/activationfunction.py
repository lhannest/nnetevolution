import math

### Recipy for making an activation function:
###
### def function_name(x):
###		return f(x), f'(x)
###
### where f(x) is the function you are trying to implement, and f'(x) is the derivative of f(x).

def relu(x):
	return max(0, x), (x > 0) * 1

def linear(x):
	return x, 1

# Avoid overflow error with exp(-x) when x is very large or small. Warning: the f' is zero when f is 1.
def sigmoid(x):
	if x > 100:
		return 1, 0
	elif x < -100:
		return 0, 0
	else:
		s = 1 / (1 + math.exp(-x))
		return s, s * (1 - s)