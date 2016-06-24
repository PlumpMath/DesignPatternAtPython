from string_display_impl import StringDisplayImpl

class StringTextDisplayImpl2(StringDisplayImpl):
	def __init__(self, file_name):
		for row in open(file_name, "r"):
			string = row
		f.close()
		super(StringTextDisplayImpl2, self).__init__(string)
	def textDisplay(self):
		self.rawOpen()
		self.rawPrint()
		self.rawClose()