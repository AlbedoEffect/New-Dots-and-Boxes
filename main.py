from board import *
from player import *
board = game_board(4,4)
player = Ai_Player()
turn = 0
while(not board.is_full()):
	move = player.perform_move(board)
	if(not board.is_valid_move(move[0],move[1],move[2],-1)):
		print('Illegal move!')
		break
	else:
		print('Played move!')
		board.play_move(move[0],move[1],move[2],1)
