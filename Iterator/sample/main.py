# -*- coding: utf-8 -*-

from bookShelf import BookShelf
from book import Book

if __name__ == '__main__':
	bookShelf = BookShelf(1)
	bookShelf.appendBox(Book("addd"))
	# print t_class.__arg