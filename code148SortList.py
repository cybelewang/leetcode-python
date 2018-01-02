from ListNode import *
"""
Sort a linked list in O(n log n) time using constant space complexity.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# similar to merge sort, starting from sorting every two nodes, then every four node, then every 8 nodes... until 2^m >= n
class Solution:
    def mergeSortedList(self, head, n): 
        """
        divide and merge sorted lists
        return the head and tail of the merged sorted list
        |----left half-----|----right half----|----following----|
        """
        # get the tail of the left half list
        node = head
        for i in range(1, n//2):
            if node.next is not None:
                node = node.next
            else:
                return (head, node)
        # get the head of the right half list
        head1 = node.next
        if head1 is None:   # bug fixed: missed this corner case: the head of the right half list is empty
            return (head, node)

        node.next = None    # disconnect left half list and right half list

        # get the head of the following list after this merged list
        node = head1
        for i in range(1, n//2):
            if node.next is not None:
                node = node.next
            
        next_head = node.next

        node.next = None    # disconnect right half list with the following list

        # aux head node
        zero = ListNode(0)
        node = zero
        # merge the two sorted lists
        while head or head1:
            if head is None:
                node.next = head1
                head1 = head1.next
            elif head1 is None:
                node.next = head
                head = head.next
            else:
                if head.val < head1.val:
                    node.next = head
                    head = head.next
                else:
                    node.next = head1
                    head1 = head1.next
            
            node = node.next

        node.next = next_head
        return (zero.next, node)

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        period = 2
        while True:
            (head, tail) = self.mergeSortedList(head, period)
            if tail.next is None:
                break
            while tail.next is not None:
                (new_head, new_tail) = self.mergeSortedList(tail.next, period)
                tail.next = new_head    # bug fixed: we need to connect the previous tail with the new head
                tail = new_tail
            
            period *= 2

        return head

obj = Solution()
l1 = ListNode(0)
l1.fromList([8,1,3])
PrintLinkedList(l1)
l2 = obj.sortList(l1)
PrintLinkedList(l2)