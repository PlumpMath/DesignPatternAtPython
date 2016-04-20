# -*- coding: utf-8 -*-

from zope.interface import implements
from iterator import Iterator

class BookShelfIterator:
	"""docstring for BookShelfIterator"""
	# Iteratorクラスを継承
	implements(Iterator)

	def __init__(self, bookShelf):
		self.__bookShelf = bookShelf
		self.__index = 0
	def hasNext(self):
		if self.__index < self.__bookShelf.getLength:
			return True
		else:
			return False
	def next(self):
		book = self.__bookShelf.getBookAt(self.__index)
		self.__index += 1
		return book
