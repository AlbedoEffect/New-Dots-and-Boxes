from abc import ABCMeta, abstractmethod

class display:
	__metaclass__ = ABCMeta

	@abstractmethod
	def update_line(self,x,y,z,val):
		return 0
	
	@abstractmethod
	def update_square(self,x,val):
		return 0
