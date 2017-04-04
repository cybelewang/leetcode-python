# Definition for singly-linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def printAll(self):
        """
        Print the whole Linked List starting with this Node 
        """
        current = self
        while current != None:
            print("{0}->".format(current.val), end='')
            current = current.next;       
