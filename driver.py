from NeuralNetwork import *
import random
def main():
	NN = NeuralNetwork(2,2,1)
	input_data = [[1,0],[0,1],[1,1],[0,0]]
	targets = [[1],[1],[0],[0]]
	# print(random.randint(0, len(input_data)-1))
	for i in range(100000):
		data = random.randint(0, len(input_data)-1)
		output = NN.train(input_data[data], targets[data])
	guess = NN.feedforward([0,0])
	print(guess.data)
	guess = NN.feedforward([1,0])
	print(guess.data)
	guess = NN.feedforward([0,1])
	print(guess.data)
	guess = NN.feedforward([1,1])
	print(guess.data)
	# print(output)
if __name__ == '__main__':
	main()