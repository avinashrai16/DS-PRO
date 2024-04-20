# Linked list setup:

class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    # method to set the data value
    def setData(self, data):
        self.data = data

    # method to get the data value:
    def getData(self):
        return self.data

    # method to set Next link:
    def setNext(self, next):
        self.next = next

        # method to get the next:
    def getNext(self):
        return self.next

    def traverse_linked_list(self):
        temp = self.Node
        while (temp):
            if (temp.getNext() == None):  # for the tail of linked list, without end
                print(temp.data)  # via property decorator
            else:
                print(temp.getData(), end="->")
            temp = temp.getNext()  # go to the next node