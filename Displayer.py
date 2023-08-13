from turtle import Turtle, Screen
from Matrix import Matrix

# Standalone version

class Displayer:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.base_id = 0
		self.bases = [Matrix(2,2,[[1,0],[0,1]])]
		self.drawer = Turtle()
		self.screen = Screen()
		self.screen.tracer(0)
		self.drawer.up()
		#self.drawer.hideturtle()
	
	def getScreen(self):
		return self.screen
	
	def getDrawer(self):
		return self.drawer
	
	def getBase(self):
		return self.bases[self.base_id]
	
	def switchBase(self):
		self.base_id += 1
		self.base_id %= len(self.bases)
		return self.base_id
	
	def drawSquare(self, edge, coord_x, coord_y):
		self.drawer.goto(coord_x-(edge/2), coord_y-(edge/2))
		self.drawer.down()
		x=self.drawer.xcor()
		y=self.drawer.ycor()
		self.drawer.goto(x+edge,y)
		self.drawer.goto(x+edge,y+edge)
		self.drawer.goto(x,y+edge)
		self.drawer.goto(x,y)
		self.drawer.up()
		
	def getBases(self):
		return self.bases
	
	def draw(self, grid):
		edge_size = min(self.width/grid.getWidth(), self.height/grid.getHeight())
		for y in range(grid.getHeight()):
			for x in range(grid.getWidth()):
				self.squared(edge_size, x*edge_size, y*edge_size)
		self.screen.exitonclick()

	#TODO^
