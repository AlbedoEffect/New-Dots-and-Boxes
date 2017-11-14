class board_square:
	def __init__(self):
		self.state = [0,0,0,0]

	def reset(self):
		self.state = [0,0,0,0]


class Board:
	def __init__(self, rows, cols):
		self.boardState = [[[0 for y in range(cols-1)] for x in range(rows)], [[0 for x in range(rows-1)] for y in range(cols)]]
		self.rows = rows
		self.cols = cols
	
	def reset_board(self):
		self.boardState = [[[0 for y in range(cols-1)] for x in range(rows)], [[0 for x in range(rows-1)] for y in range(cols)]]

	def is_full(self):
		for y in range(self.cols):
			for x in range(self.rows-1):
				if boardState[1][y][x] == 0: return false
		
		for x in range(self.rows):
			for y in range(self.cols-1):
				if boardState[0][x][y] == 0: return false

		return true
				
