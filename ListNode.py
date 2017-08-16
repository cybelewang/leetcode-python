# Definition for singly-linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def fromList(self, values):
        """
        :type values: list
        """
        if len(values) == 0:
            return
        self.val = values[0]
        self.next = None
        node = self        
        for i in range(1, len(values)):
            temp = ListNode(values[i])
            node.next = temp
            node = node.next

    def printAll(self):
        """
        Print the whole Linked List starting with this Node
        """
        current = self
        while current != None:
            print("{0}->".format(current.val), end='')
            current = current.next
