from Grid import Grid
from Matrix import Matrix
from Displayer import Displayer

a = Matrix(1,2,[[0,2]])
b = Matrix(2,2,[[1,0],[0,1]])
c = a*b
print(a)
print(b)
print(c)
grid = Grid(80, 80)
displayer = Displayer(400,400)
displayer.pave(grid)
displayer.exitOnClick()
