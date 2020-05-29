from matrix import *

def double(x):
	return x*2

m1 = Matrix(2,2)
m1.randomize()
print(m1.data)
m1.map(double)
print(m1.data)