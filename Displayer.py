from turtle import Turtle, Screen

# Standalone version

class Displayer:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.base = 0
		self.bases = self.giveBases()
		self.drawer = Turtle()
		self.screen = Screen()
		self.screen.tracer(0)
		self.drawer.up()
		self.drawer.ht()
	
	def getScreen(self):
		return self.screen
	
	def getDrawer(self):
		return self.drawer
	
	def getBase(self):
		return self.base
	
	def switchBase(self):
		self.base+=1
		self.base%=len(self.bases)
		return self.base
	
	def squared(self, edge, coord_x, coord_y):
		self.drawer.goto(coord_x-(edge/2), coord_y-(edge/2))
		self.drawer.down()
		x=self.drawer.xcor()
		y=self.drawer.ycor()
		self.drawer.goto(x+edge,y)
		self.drawer.goto(x+edge,y+edge)
		self.drawer.goto(x,y+edge)
		self.drawer.goto(x,y)
		self.drawer.up()
		
	def giveBases(self):
		return [self.squared]
	
	def draw(self, grid):
		edge_size = min(self.width/grid.getWidth(), self.height/grid.getHeight())
		for y in range(grid.getHeight()):
			for x in range(grid.getWidth()):
				self.squared(edge_size, x*edge_size, y*edge_size)
		self.screen.exitonclick()
