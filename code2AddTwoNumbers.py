from ListNode import *

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carrier = 0 # carrier
        head = node = ListNode(0) # head of the result linked list
        while l1 or l2 or carrier:
            num1 = num2 = 0
            if l1 != None:
                num1 = l1.val
                l1 = l1.next
            if l2 != None:
                num2 = l2.val
                l2 = l2.next
            (carrier, val) = divmod(num1 + num2 + carrier, 10)
            node.next = ListNode(val)
            node = node.next
        return head.next