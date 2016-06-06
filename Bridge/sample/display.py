class Display(object):
	def __init__(self, impl):
		self.__impl = impl
	def open(self):
		self.__impl.rawOpen()
	def printRaw(self):
		self.__impl.rawPrint()
	def closeRaw(self):
		self.__impl.rawClose()
	def display(self):
		self.open()
		self.printRaw()
		self.closeRaw()