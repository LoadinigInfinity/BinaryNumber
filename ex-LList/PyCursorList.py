# PyCursorList.py
#
# by David M. Reed and John Zelle
# from Data Structures and Algorithms Using Python and C++
# downloaded from publisher's website:
# https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c
# on July 23, 2014

from PyListCursor import PyListCursor

class PyCursorList(list):

    def getCursor(self):
        return PyListCursor(self)
