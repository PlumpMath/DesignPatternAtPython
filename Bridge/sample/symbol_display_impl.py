import sys
from display_impl import DisplayImpl

class SymbolDisplayImpl(DisplayImpl):
	def __init__(self, decoration_first, symbol, decoration_end):
		super(SymbolDisplayImpl, self).__init__()
		self.__symbol = symbol
		self.__decoration_first = decoration_first
		self.__decoration_end = decoration_end
	def rawOpen(self):
		sys.stdout.write(self.__decoration_first)
	def rawPrint(self):
		sys.stdout.write(self.__symbol)
	def rawClose(self):
		print self.__decoration_end

