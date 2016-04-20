# -*- coding: utf-8 -*-

from zope.interface import Interface
from abc import abstractmethod

class Iterator(Interface):
	"""docstring for Iterator"""
	@abstractmethod
	def iterator():
		pass