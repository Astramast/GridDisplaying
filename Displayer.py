from turtle import Turtle

# Standalone version

class Displayer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
		self.base = 0
		self.bases = self.giveBases()
		self.drawer = Turtle()

	def getBase(self):
		return self.base

	def switchBase(self):
		self.base+=1
		self.base%=len(self.bases)
		return self.base

	def squared(self, edge_size, coord_x, coord_y):
		self.drawer.up()
		self.drawer.goto(coord_x-(edge_size/2), coord_y-(edge_size/2))
		self.drawer.down()
		

	def giveBases(self):
		return [self.squared, self.hexagonal, self.circles]
