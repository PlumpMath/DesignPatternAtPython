from count_display import CountDisplay
import random

class RandomDisplay(CountDisplay):
	def __init__(self, impl):
		super(RandomDisplay, self).__init__(impl)
		self.__impl = impl
	def randomMultiDisplay(self):
		self.multiDisplay(random.randint(1, 10))
