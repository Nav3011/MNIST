import numpy as np
def sign(result):
	if result>=0:
		return 1
	else:
		return -1
class Perceptron:
	def __init__(self):
		# initialise weights array of size 2
		self.weights = [0]*2
		for i in range(len(self.weights)):
			# setting random weights between 1 and -1
			self.weights[i] = np.random.uniform(-1,1)
	def guess(self, inputs):
		res = 0.0
		for i in range(len(self.weights)):
			res = res + inputs[i]*self.weights[i]
		output = sign(res)
		return output