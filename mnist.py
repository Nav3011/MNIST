from NeuralNetwork import *
from plot import *
import csv
from matrix import *

X_train = []
Y_train = []

def load_dataset():
	file = "../Datasets/MNIST/mnist_train.csv"
	with open(file,'r') as f:
		data = csv.reader(f)
		for row in data:
			y = list(row[0])
			x = list(row[1:])
			X_train.append(x)
			Y_train.append(y) 
	# digit = Plot()
	# digit.visualize_digit(X_train[0])

# def normalize_X_train():
# 	print(len(X_train))
def main():
	load_dataset()
	normalize_X_train()
if __name__ == '__main__':
	main()

