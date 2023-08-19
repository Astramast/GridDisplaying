class Matrix:
	def __init__(self, lines_amount, columns_amount, matrix=None):
		if matrix == None:
			matrix=[[0 for _ in range(columns_amount)] for __ in range(lines_amount)]
		self.l = lines_amount
		self.c = columns_amount
		self.matrix = matrix

	def __imul__(self, other):
		self.checkMultiplicity(other)
		c = other.getColumnsAmount()
		for line_number in range(self.l):
			newline = [0 for _ in range(c)]
			for column_number in range(c):
				submults = [0 for _ in range(self.c)]
				for mult in range(self.c):
					submults[mult] = self.matrix[line_number][mult]*other.get(mult, column_number)
				newline[column_number] = sum(submults)
			self.matrix[line_number] = newline

	def __mul__(self, other):
		self.checkMultiplicity(other)
		c = other.getColumnsAmount()
		newmatrix = [[0 for _ in range(c)] for __ in range(self.l)]
		for line_number in range(self.l):
			newline = [0 for _ in range(c)]
			for column_number in range(c):
				submults = [0 for _ in range(self.c)]
				for mult in range(self.c):
					submults[mult] = self.matrix[line_number][mult]*other.get(mult, column_number)
				newline[column_number] = sum(submults)
			newmatrix[line_number] = newline
		return Matrix(self.l, c, newmatrix)

	def __iadd__(self, other):
		self.checkSameDims(other)
		for line in range(self.l):
			for column in range(self.c):
				self.matrix[line][column] += other.get(line, column)

	def __add__(self, other):
		self.checkSameDims(other)
		newmatrix = [[0 for _ in range(self.c)] for __ in range(self.l)]
		for line in range(self.l):
			for column in range(self.c):
				newmatrix[line][column] = self.matrix[line][column] + other.get(line, column)
		return Matrix(self.l, self.c, newmatrix)

	def __sub__(self, other):
		self.checkSameDims(other)
		for line in range(self.l):
			for column in range(self.c):
				self.matrix[line][column] -= other.get(line, column)

	def __isub__(self, other):
		self.checkSameDims(other)
		newmatrix = [[0 for _ in range(self.c)] for __ in range(self.l)]
		for line in range(self.l):
			for column in range(self.c):
				newmatrix[line][column] = self.matrix[line][column] - other.get(line, column)
		return Matrix(self.l, self.c, newmatrix)

	def __repr__(self):
		return str(self.matrix)

	def checkSameDims(self, other):
		if self.l != other.getLinesAmount() or self.c != other.getColumnsAmount():
			raise ValueError("Trying to add/substract matrices with different dimensions")

	def checkMultiplicity(self, other):
		if self.c != other.getLinesAmount():
			raise ValueError("Number of columns not equal to number of lines in matricial multiplication.")

	def getLinesAmount(self):
		return self.l

	def getColumnsAmount(self):
		return self.c

	def getLine(self, line_number):
		return self.matrix(line_number)

	def getColumn(self, column_number):
		column = [matrix[i][column_number] for i in range(self.l)]
		return column

	def get(self, i, j):
		return self.matrix[i][j]

if __name__ == "__main__":
	m = Matrix()

