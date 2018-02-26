#-------------------------------------------------------------------------------
# Name:        LinkedList_driver.py
# Purpose:  Rudimentary driver for the LinkedList class.
#
#-------------------------------------------------------------------------------

from  LList import LList


def main():
    print("Make a linked list -> 1 -> 2 -> 3 -> None")
    mylist = LList(( 1, 2, 3)) # call constructor with the tuple ( 1 , 2 , 3)
    for item in mylist:
        print(str(item)+"->",end='')
    print("None")
    print("mylist[0] is "+ str(mylist[0])) # calls a. __ get item _ (O)
    mylist[0] = 4 # calls a. __ set item _ ( O , 4 )
    print("Change mylist[0]")
    print("mylist[0] is "+ str(mylist[0])) # calls a. __ get item _ (O)
    for item in mylist:
        print(str(item)+"->",end='')
    print("None")

if __name__ == '__main__':
    main()
