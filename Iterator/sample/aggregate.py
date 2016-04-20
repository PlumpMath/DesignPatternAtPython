# -*- coding: utf-8 -*-

from zope.interface import Interface
from abc import abstractmethod

class Aggregate(Interface):
	"""docstring for Aggregate"""
	@abstractmethod
	def iterator():
		pass
	@abstractmethod
	def next():
		pass