from NeuralNetwork import *
import random
def main():
	NN = NeuralNetwork(4,5,3,2)
	inputs = [1,1,1,1]
	outputs= [1,1]
	NN.train(inputs, outputs)
if __name__ == '__main__':
	main()