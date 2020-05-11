from matrix import *
m1 = Matrix(2,3)
m1.randomize()
print(m1.matrix)
m2 = Matrix(3,2)
m2.randomize()
print(m2.matrix)
Matrix.dot(m1,m2)



# 2 5 7		3 1
# 7 7 1		4 7
# 			4 4


# 00 * 00 + 01 * 10 + 02 * 20		00 * 01 + 01 * 11 + 02 * 21 
# 10 * 00 + 11 * 10 + 12 * 20		10 * 01 + 11 * 11 + 12 * 21	