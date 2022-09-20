class Grid:
    def __init__(self, n, m=n):
        self.height = n
        self.width = m
        self.matrix = [[0 for i in range(m)] for j in range(n)]

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def getSquare(self, i, j):
        return self.matrix[i][j]

	def fillSquare(self, i, j, new):
		self.matrix[i][j] = new

