# -*- coding: shift-jis -*-
import sys
from display_impl import DisplayImpl

class StringTextDisplayImpl(DisplayImpl):
	def __init__(self, file_name):
		super(StringTextDisplayImpl, self).__init__()
		self.__file_name = file_name
	def rawOpen(self):
		self.f = open(self.__file_name, "r")
		print
	def rawPrint(self):
		for row in self.f:
			sys.stdout.write(row)
	def rawClose(self):
		self.f.close()
		print