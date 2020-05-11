class Matrix():
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.matrix = list()

		for i in range(self.rows):
			self.matrix.append(list())
			for j in range(self.cols):
				self.matrix[i].append(0)

	# Here m1 and m2 are the matrix objects 
	@staticmethod
	def multiply(m1, m2):
		# size of resulting array is m1.rows x m2.cols
		result = list() 
		if m1.cols == m2.rows:
			for i in range(m1.rows):
				for j in range(m2.cols):
					for k in range(m1.rows):
						d = m1.matrix[i][j+k] + m2.matrix[i+k][j]
						print(d)
		else:
			print("Columns of m1 must be equal to the rows of m2.")
	@classmethod
	def multiply(self, n):
		if isinstance(n, Matrix):
			for i in range(self.rows):
				for j in range(self.cols):
					self.matrix[i][j] = self.matrix[i][j]*n.matrix[i][j]
		else:
			for i in range(self.rows):
				for j in range(self.cols):
					self.matrix[i][j] = self.matrix[i][j]*n

	def add(self, n):
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