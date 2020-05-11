class Matrix():
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.matrix = list()

		for i in range(self.rows):
			self.matrix.append(list())
			for j in range(self.cols):
				self.matrix[i].append(0)

	def Multiply(self, n):
		if isinstance(n, Matrix):
			for i in range(self.rows):
				for j in range(self.cols):
					self.matrix[i][j] = self.matrix[i][j]*n.matrix[i][j]
		else:
			for i in range(self.rows):
				for j in range(self.cols):
					self.matrix[i][j] = self.matrix[i][j]*n

	def Add(self, n):
		if isinstance(n, Matrix):
			for i in range(self.rows):
				for j in range(self.cols):
					self.matrix[i][j] = self.matrix[i][j]+n.matrix[i][j]
		else:
			for i in range(self.rows):
				for j in range(self.cols):
					self.matrix[i][j] = self.matrix[i][j]+n

	def show(self):
		for i in range(self.rows):
			for j in range(self.cols):
				print(self.matrix[i][j])