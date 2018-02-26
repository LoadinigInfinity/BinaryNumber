# LinkedCursorList.py
#
# by David M. Reed and John Zelle
# from Data Structures and Algorithms Using Python and C++
# downloaded from publisher's website:
# https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c
# on July 23, 2014

from LList import LList
from LListCursor import LListCursor

class LinkedCursorList(LList):

    def getCursor(self):
        return LListCursor(self)
