from abc import ABCMeta, abstractmethod

class DisplayImpl(object):
	__metaclass__ = ABCMeta	#abstractclass

	@abstractmethod
	def rawOpen():
		pass
	@abstractmethod
	def rawPrint():
		pass
	@abstractmethod
	def rawClose():
		pass
