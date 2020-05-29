from matrix import *
import math

def sigmoid(x):
	return 1 / (1 + math.exp(-x))

class NeuralNetwork:
	def __init__(self, Input, Hidden, Output):
		self.input_nodes = Input
		self.hidden_nodes = Hidden
		self.output_nodes = Output

		self.weights_IH = Matrix(self.hidden_nodes, self.input_nodes)
		self.weights_HO = Matrix(self.output_nodes, self.hidden_nodes)
		self.weights_IH.randomize()
		self.weights_HO.randomize()

		self.biases_H = Matrix(self.hidden_nodes, 1)
		self.biases_O = Matrix(self.output_nodes, 1)
		self.biases_H.randomize()
		self.biases_O.randomize()
	
	def feedforward(self, data):
		inputs = Matrix.fromArray(data)
		hidden = Matrix.dot(self.weights_IH, inputs)
		hidden.add(self.biases_H)
		hidden.map(sigmoid)

		output = Matrix.dot(self.weights_HO, hidden)
		output.add(self.biases_O)
		output.map(sigmoid)
		return output.data
