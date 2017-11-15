from graphics import *
import board
class graphic_display:
	def __init__(self,rows,cols):
		self.win = GraphWin()
		lin_len = 20
		line_width = 5
		self.squaresState = []
		self.linesState = [[[0 for x in range(cols)]for y in range(rows+1)],[[x for y in range(rows)] for y in range(cols+1)]]
		self.base_pt = Point(50,50)

		for x in range(rows*cols):
			self.pt.x = self.base_pt.x + (x%cols)*(line_len+line_width)
			self.pt.y = self.base_pt.y + (x // cols)*(line_len+line.width)
			self.squaresState.append(Rectangle(self.pt,Point(self.pt.x+line_len,self.pt.y+line_len)))
			self.squaresState[i].draw(self.win)


		for x in range(rows+1):
			self.pt = Point(self.base_pt.x, self.base_pt.y + y*(line_len + line_width))	
			for y in range(cols):				
				self.linesState[0][x][y] = (Rectangle(self.pt,Point(self.pt.x+line_len,self.pt.y+line_width)))
				self.linesStates[0][x][y].draw(self.win)
				self.pt.y += line_len + line_width
		
		for x in range(cols+1):
			for y in range(rows):
				self.linesState[1][x][y] = (Rectangle(self.pt,Point(self.pt.x+line_width,self.pt.y+line_len)))
				self.linesStates[1][x][y].draw(self.win)
				self.pt.x += line_len + line_width
		
			
