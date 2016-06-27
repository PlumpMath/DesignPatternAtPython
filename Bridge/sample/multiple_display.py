from display import Display

class MultipleDisplay(Display):
	def __init__(self, impl):
		super(MultipleDisplay, self).__init__(impl)
		self.__impl = impl
	def multipleDisplay(self, times, multiple):
		multiple_count = 0
		for i in xrange(0, times):
			self.open()
			for j in xrange(0, multiple_count):
				self.printRaw()
			self.closeRaw()
			multiple_count += multiple 
