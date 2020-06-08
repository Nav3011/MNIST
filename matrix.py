from random import random
# from random import seed
# seed(1)
class Matrix():
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.data = list()

		for i in range(self.rows):
			self.data.append(list())
			for j in range(self.cols):
				self.data[i].append(0)

	@staticmethod
	def fromArray(arr):
		res = Matrix(len(arr),1)
		for i in range(len(arr)):
			res.data[i][0] = arr[i]
		return res

	@staticmethod
	def dot(m1, m2):
		res = Matrix(m1.rows, m2.cols)
		result = list() 
		if m1.cols == m2.rows:
			for i in range(m1.rows):
				dt=list()
				for j in range(m2.cols):
					sum_ = 0
					for k in range(m1.cols):
						sum_ = sum_ + m1.data[i][k] * m2.data[k][j]
					dt.append(sum_)
				result.append(dt)
			for i in range(m1.rows):
				for j in range(m2.cols):
					res.data[i][j] = result[i][j]
			return res
		else:
			print("Columns of m1 must be equal to the rows of m2.")

	def multiply(self, n):
		if isinstance(n, Matrix):
			for i in range(n.rows):
				for j in range(n.cols):
					self.data[i][j] = self.data[i][j]*n.data[i][j]
		else:
			for i in range(self.rows):
				for j in range(self.cols):
					self.data[i][j] = self.data[i][j]*n

	def add(self, n):
		if isinstance(n, Matrix):
			for i in range(self.rows):
				for j in range(self.cols):
					self.data[i][j] = self.data[i][j]+n.data[i][j]
		else:
			for i in range(self.rows):
				for j in range(self.cols):
					self.data[i][j] = self.data[i][j]+n

	@staticmethod
	def subtract(m1, m2):
		result = Matrix(m1.rows, m1.cols)
		for i in range(m1.rows):
			for j in range(m1.cols):
				result.data[i][j] = m1.data[i][j] - m2.data[i][j]
		return result

	def randomize(self):
		for i in range(self.rows):
			for j in range(self.cols):
				self.data[i][j] = random()*2 - 1

	def show(self):
		for i in range(self.rows):
			for j in range(self.cols):
				print(self.data[i][j])

	@staticmethod
	def transpose(m):
		result = Matrix(m.cols, m.rows)
		for i in range(m.rows):
			for j in range(m.cols):
				result.data[j][i] = m.data[i][j]
		return result

	@staticmethod
	def map(m, func):
		result = Matrix(m.rows, m.cols)
		for i in range(m.rows):
			for j in range(m.cols):
				val = m.data[i][j]
				result.data[i][j] = func(val)
		return result