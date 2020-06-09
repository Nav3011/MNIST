from matrix import *
import math

def sigmoid(x):
	return 1 / (1 + math.exp(-x))

def sigmoidD(x):
	return sigmoid(x) * (1-sigmoid(x))

class NeuralNetwork:

	def __init__(self, inputLayer, hiddenLayer1, hiddenLayer2, outputLayer):
		print("[INFO] Network with entered architecture created")
		self.input_nodes = inputLayer
		self.hidden1_nodes = hiddenLayer1
		self.hidden2_nodes = hiddenLayer2
		self.output_nodes = outputLayer
		
		# weight matrices have shape (nodes in layer L+1) * (nodes in layer L)
		print("[INFO] Weight matrices created")
		self.weights_1 = Matrix(self.hidden1_nodes, self.input_nodes)
		self.weights_2 = Matrix(self.hidden2_nodes, self.hidden1_nodes)
		self.weights_3 = Matrix(self.output_nodes, self.hidden2_nodes)

		print("[INFO] Weight matrices initialised")
		self.weights_1.randomize()
		self.weights_2.randomize()
		self.weights_3.randomize()

		# bias matrices have shape (nodes in layer L) * 1 -> column matrices 
		print("[INFO] Bias matrices created")
		self.biases_1 = Matrix(self.hidden1_nodes, 1)
		self.biases_2 = Matrix(self.hidden2_nodes, 1)
		self.biases_3 = Matrix(self.output_nodes, 1)
		
		print("[INFO] Bias matrices initialised")
		self.biases_1.randomize()
		self.biases_2.randomize()
		self.biases_3.randomize()

	def train(self, inputs, outputs):
		#inputs and outputs are list. Convert to Matrix object
		#Feed forward
		self.Input = Matrix.fromArray(inputs)
		self.Output = Matrix.fromArray(outputs)

		self.z1 = Matrix.dot(self.weights_1, self.Input)
		self.z1.add(self.biases_1)
		self.a1 = Matrix.map(self.z1, sigmoid)

		self.z2 = Matrix.dot(self.weights_2, self.a1)
		self.z2.add(self.biases_2)
		self.a2 = Matrix.map(self.z2, sigmoid)		

		self.z3 = Matrix.dot(self.weights_3, self.a2)
		self.z3.add(self.biases_3)
		self.a3 = Matrix.map(self.z3, sigmoid)

		self.loss = Matrix.subtract(self.a3, self.Output)
		self.loss = Matrix.multiply(self.loss, self.loss)
		self.loss = Matrix.multiply(self.loss, 0.5)

		#Back propagation
		
		#W3 and bias3 gradient calculation 
		self.sigmoidD3 = Matrix.map(self.z3, sigmoidD)
		self.delta3 = Matrix.subtract(self.a3, self.Output)
		self.delta3 = Matrix.multiply(self.delta3, self.sigmoidD3)
		self.a2_transpose = Matrix.transpose(self.a2)
		self.weight3_gradient = Matrix.dot(self.delta3, self.a2_transpose)
		
		#W2 and bias gradient calculation
		self.sigmoidD2 = Matrix.map(self.z2, sigmoidD)
		self.weight3_transpose = Matrix.transpose(self.weights_3)
		self.delta2 = Matrix.dot(self.weight3_transpose, self.delta3)
		self.delta2 = Matrix.multiply(self.delta2, self.sigmoidD2)
		self.a1_transpose = Matrix.transpose(self.a1)
		self.weight2_gradient = Matrix.dot(self.delta2, self.a1_transpose)
		# print(self.weight2_gradient.data)

		self.sigmoidD1 = Matrix.map(self.z1, sigmoidD)
		self.weight2_transpose = Matrix.transpose(self.weights_2)
		self.delta1 = Matrix.dot(self.weight2_transpose, self.delta2)
		self.delta1 = Matrix.multiply(self.delta1, self.sigmoidD1)
		self.input_transpose = Matrix.transpose(self.Input)
		self.weight1_gradient = Matrix.dot(self.delta1, self.input_transpose)
		# print(self.weight1_gradient.data)		





