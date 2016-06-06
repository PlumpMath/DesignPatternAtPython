import sys
from display_impl import DisplayImpl

class StringDisplayImpl(DisplayImpl):
	def __init__(self, string):
		super(StringDisplayImpl, self).__init__()
		self.__string = string
		self.__width = len(string.encode())
	def rawOpen(self):
		self.__printLine()
	def rawPrint(self):
		print "|" + self.__string + "|"
	def rawClose(self):
		self.__printLine()
	def __printLine(self):
		sys.stdout.write("+")
		for i in xrange(0, self.__width):
			sys.stdout.write("-")
		print "+"
