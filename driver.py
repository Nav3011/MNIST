from NeuralNetwork import *
def main():
	NN = NeuralNetwork(2,2,1)
	input_data = list((1,0))
	output = NN.feedforward(input_data)
	print(output)
if __name__ == '__main__':
	main()