from abc import ABCMeta, abstractmethod
from board import *
import board

class Player:
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def perform_move(self,board):
		return [-1,-1,0]

class Ai_Player(Player):
	def perform_move(self,board):
		return [0,0,1]

