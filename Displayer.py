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

	def exitOnClick(self):
		self.screen.exitonclick()

	def drawLine(self, start, end):
		self.drawer.goto(start.get(0,0), start.get(0,1))
		self.drawer.down()
		self.drawer.goto(end.get(0,0), end.get(0,1))
		self.drawer.up()

	def pave(self, grid):
		y = grid.getLinesAmount()
		x = grid.getColumnsAmount()
		for i in range(grid.getLinesAmount()+1):
			self.drawLine(Matrix(1,2,[[0,i]])*self.bases[self.base_id], Matrix(1,2,[[x,i]])*self.bases[self.base_id])
		for j in range(grid.getColumnsAmount()+1):
			self.drawLine(Matrix(1,2,[[j,0]])*self.bases[self.base_id], Matrix(1,2,[[j,y]])*self.bases[self.base_id])
			

	def getBases(self):
		return self.bases
	
	def getScreen(self):
		return self.screen
	
	def getDrawer(self):
		return self.drawer
	
	def getBase(self):
		return self.bases[self.base_id]
	
