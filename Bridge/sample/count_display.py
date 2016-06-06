from display import Display

class CountDisplay(Display):
	def __init__(self, impl):
		super(CountDisplay, self).__init__(impl)
		self.__impl = impl
	def multiDisplay(self, times):
		self.open()
		for i in xrange(0, times):
			self.printRaw()
		self.closeRaw()
		