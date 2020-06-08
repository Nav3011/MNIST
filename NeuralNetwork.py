from matrix import *
import math

def sigmoid(x):
	return 1 / (1 + math.exp(-x))
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