from ListNode import *
"""
147 Insertion Sort List

Sort a linked list using insertion sort.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# different from array insertion sort, which searches from right side of the already-sorted partial array. 
# Here we need to search from left and insert the node to the correct position.
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)

        right = head
        while right is not None:
            temp = right.next   # temp saves the next node of right
            right.next = None   # disconnect "right" with the next

            # search from pre, and 'left" will stop at the node before the correct insertion position
            left = pre
            while left.next is not None and left.next.val < right.val:
                left = left.next
            
            # insert the 'right' node
            next = left.next
            left.next = right
            right.next = next
            
            # advance the 'right' iterator
            right = temp
        
        return pre.next

obj = Solution()
l1 = ListNode(0)
l1.fromList([8, 1, 5, 6, 7, 2, 4, 3])
PrintLinkedList(l1)
l2 = obj.insertionSortList(l1)
PrintLinkedList(l2)