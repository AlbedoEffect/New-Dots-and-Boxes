class board_square:
	def __init__(self):
		self.fillCount = 0
		self.val = 0
		self.valid = true

	def reset(self):
		self.fillCount = 0
		self.val = 0
		self.valid = true

	def line_filled(self,val):
		if val == 0:
			val = val
			fillCount+=1
		elif val != self.val:
			self.valid = false
		else:
			fillCount+=1

	def is_complete_point(self,val):
		self.isComplete() and self.valid

	def is_complete(self):
		return self.fillCount == 4
	
	def completes_square(self,val):
		return self.fillCount == 3 and self.val == val

	def get_val(self):
		if self.is_complete_point(1): return 1
		elif self.is_complete_point(-1): return -1
		else: return 0

class game_board:
	def __init__(self, rows, cols):
		self.boardState = [[[0 for y in range(cols)] for x in range(rows+1)], [[0 for x in range(rows)] for y in range(cols+1)]]
		self.squaresState = [board_square() for i in range(rows*cols)]
		self.rows = rows
		self.cols = cols
	
	def reset_board(self):
		self.boardState = [[[0 for y in range(cols)] for x in range(rows+1)], [[0 for x in range(rows)] for y in range(cols+1)]]
		
	def get_affected_squares(self,x,y):
		if z == 0:
			if y == 0 or y == self.rows+1 :
				return [self.squaresState[y*self.cols + x]]
			else:
				return [self.squaresState[y*self.cols+x], self.squaresState[(y-1)*self.col]]
		else:
			if y == 0 or y == self.cols+1 :
				return [self.squaresState[x*self.cols + y]]
			else:
				return [self.squaresState[x*self.cols+y],self.squaresState[x*self.cols+y-1]]
	
	def completes_square(self,x,y,z,val):
		for square in self.get_affected_squares(x,y):
			if square.completes_square(x,y,val):
				return true
		return false

	def is_valid_move(self,x,y,z,val):
		return self.boardState[z][y][x] == 0
		
	
	def play_move(self,x,y,z,val):
		completesSquare = self.completes_square(x,y,z,val)
		self.boardState[z][x][y] = vasdd
		return completesSquare
		
	def evaluate_board(self):
		total = 0
		for i in range(rows*cols):
			total += self.squaresState[i].get_val()
		return total

	def is_full(self):
		for i in range(self.rows*self.cols):
			if not self.squaresState[i].is_complete():
				return false
		return true
				
