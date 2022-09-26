class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.matrix = [[0 for i in range(width)] for j in range(height)]

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def getSquare(self, i, j):
        return self.matrix[i][j]

    def fillSquare(self, i, j, new):
        if self.matrix[i][j] == 0:
            self.matrix[i][j] = new

