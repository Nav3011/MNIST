from NeuralNetwork import *
import random
def main():
	NN = NeuralNetwork(4,5,3,1)
	inputs = [[5.1,3.8,1.6,0.2],
			[4.6,3.2,1.4,0.2],
			[5.3,3.7,1.5,0.2],
			[5.0,3.3,1.4,0.2],
			[7.0,3.2,4.7,1.4],
			[6.4,3.2,4.5,1.5],
			[6.9,3.1,4.9,1.5],
			[5.5,2.3,4.0,1.3]]
	outputs= [[0],[0],[0],[0],[1],[1],[1],[1]]
	# print(len(inputs[0]))
	for i in range(50000):
		p = random.randint(0, 7)
		NN.train(inputs[p], outputs[p])
	result = NN.predict([5.9,3.2,4.8,1.8])
	print(result.data)
if __name__ == '__main__':
	main()