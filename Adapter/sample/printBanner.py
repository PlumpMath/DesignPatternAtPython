
from zope.interface import implements
from banner import Banner
from printInterface import PrintInterface

class PrintBanner(Banner):
	"""docstring for PrintBanner"""
	implements(PrintInterface)

	def __init__(self, string):
		super(PrintBanner, self).__init__(string)
		self.__string = string
	def printWeak(self):
		self.showWithParen()
	def printStrong(self):
		self.showWithAster()