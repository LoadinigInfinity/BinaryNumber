# LListCursor.py
#
# by David M. Reed and John Zelle
# from Data Structures and Algorithms Using Python and C++
# downloaded from publisher's website:
# https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c
# on July 23, 2014

from ListNode import ListNode

class LListCursor(object):

    #------------------------------------------------------------

    def __init__(self, llist):
        self.lst = llist

        # create a dummy node at the front of the list
        self.header = ListNode("**DUMMY HEADER NODE**", llist.head)

        # point prev to just before the first actual ListNode
        self.prev = self.header

    #------------------------------------------------------------

    def done(self):

        """post: True if cursor has advanced past the last item
        of the sequence, false otherwise"""
      
        return self.prev.link is None

    #------------------------------------------------------------

    def getItem(self):

        """ pre: not self.done()
        post: Returns the item at the current cursor position"""

        return self.prev.link.item

    #------------------------------------------------------------

    def replaceItem(self, value):

        """ pre: not self.done()
           post: The current item in the sequence is value"""

        # exercise for reader
        pass

    #------------------------------------------------------------

    def advance(self):

        """ post: cursor has advanced to the next position in the
        sequence. Advancing from the last item causes
        self.done() to be True"""

        self.prev = self.prev.link

    #------------------------------------------------------------

    def deleteItem(self):
        
        """ pre: not self.done()
        post: The item that cursor was pointing to is removed
        from the sequence and the cursor now points to 
        the following item
        
        note: removing the last item in the sequence causes
        self.done() to be True"""

        self.prev.link = self.prev.link.link

        # first listnode _may_ have changed, update list head
        self.lst.head = self.header.link

    #------------------------------------------------------------

    def insertItem(self, value):

         """ post: value is added to the sequence at the position of
                  cursor. 
                  
            note: If self.done() holds before the call, value will be
                  added to the end of the sequence. In other cases, 
                  the item that was at current position becomes the
                  next item."""

         # exercise for reader
         pass
