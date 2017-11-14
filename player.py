from abc import ABCMeta
import board

class Player:
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def perform_Move(self,boardState):
		return [-1,-1]
