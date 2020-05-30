from matrix import *
import math

def sigmoid(x):
	return 1 / (1 + math.exp(-x))

def sigmoidD(x):
	return x * (1 - x)

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
		self.learning_rate = 0.1

	def feedforward(self, inputs):
		input_data = Matrix.fromArray(inputs)

		hidden = Matrix.dot(self.weights_IH, input_data)
		hidden.add(self.biases_H)
		hidden = Matrix.map(hidden, sigmoid)

		output = Matrix.dot(self.weights_HO, hidden)
		output.add(self.biases_O)
		output = Matrix.map(output, sigmoid)
		return output
	def train(self, inputs, targets):
		self.inputs = Matrix.fromArray(inputs)

		self.hidden = Matrix.dot(self.weights_IH, self.inputs)
		self.hidden.add(self.biases_H)
		self.hidden = Matrix.map(self.hidden, sigmoid)

		self.output = Matrix.dot(self.weights_HO, self.hidden)
		self.output.add(self.biases_O)
		self.output = Matrix.map(self.output, sigmoid)
		# self.inputs = Matrix.fromArray(inputs)
		self.targets = Matrix.fromArray(targets)
		# self.outputs = self.feedforward(self.inputs)

		self.output_error = Matrix.subtract(self.targets, self.output)
		# self.weights_HO_transpose = Matrix.transpose(self.weights_HO)
		# self.hidden_errors = Matrix.dot(self.weights_HO_transpose, self.error)
		self.output_gradient = Matrix.map(self.output, sigmoidD)
		self.output_gradient.multiply(self.output_error)
		self.output_gradient.multiply(self.learning_rate)
		self.hidden_transpose = Matrix.transpose(self.hidden)
		self.weights_HO_delta = Matrix.dot(self.output_gradient, self.hidden_transpose)
		self.weights_HO.add(self.weights_HO_delta)
		self.biases_O.add(self.output_gradient)
		# print(self.inputs.data)
		
		self.weights_HO_transpose = Matrix.transpose(self.weights_HO)
		self.hidden_error = Matrix.dot(self.weights_HO_transpose, self.output_error)
		self.hidden_gradient = Matrix.map(self.hidden, sigmoidD)
		self.hidden_gradient.multiply(self.hidden_error)
		self.hidden_gradient.multiply(self.learning_rate)
		self.input_transpose = Matrix.transpose(self.inputs)
		self.weights_IH_transpose = Matrix.transpose(self.inputs)
		self.weights_IH_deltas = Matrix.dot(self.hidden_gradient, self.input_transpose)
		self.weights_IH.add(self.weights_IH_deltas)
		self.biases_H.add(self.hidden_gradient)