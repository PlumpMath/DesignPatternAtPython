
from zope.interface import Interface
from abc import abstractmethod

class PrintInterface(Interface):
	"""docstring for Print"""
	@abstractmethod
	def printWeak():
		pass
	@abstractmethod
	def printStrong():
		pass
