# -*- coding: utf-8 -*-

from zope.interface import implements
from aggregate import Aggregate
from book import Book
from bookShelfIterator import BookShelfIterator

class BookShelf:
	"""docstring for BookShelf"""
	# Aggregateを継承
	implements(Aggregate)

	def __init__(self, maxsize):
		self.__last = 0
	@classmethod
	def getBookAt(self, index):
		return __books[index]
	def appendBox(self, book):
		self.__books.append(book)
		self.__last += 1
	@classmethod
	def getLength(self):
		return self.__last
	def iterator(self):
		return BookShelfIterator(self)
		