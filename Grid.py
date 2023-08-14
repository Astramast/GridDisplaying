from Matrix import Matrix

class Grid(Matrix):
	def __init__(self, height, width):
		super().__init__(height, width)

	def fillSquare(self, i, j, new):
		if self.matrix[i][j] != 0:
			return False
		self.matrix[i][j] = new
		return True

	def changeSquare(self, i, j, new):
		old = self.matrix[i][j] = new
		return old

