from ListNode import *
"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

# OJ best solution
    def reorderList(self, head):
        if not head: return
        # ensure the first part has the same or one more node
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half
        cur, pre = slow.next, None
        slow.next = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        # combine head part and node part
        p = head
        while pre:
            tmp = pre.next
            pre.next = p.next
            p.next = pre
            p = p.next.next
            pre = tmp


# second trial, use existing functions
    # reverse the right half part
    def reverse(self, head):
        if head is None:
            return head
        node = head.next
        head.next = None    # break the link between head and the second node
        while node:
            temp = node.next
            node.next = head
            head = node
            node = temp
        
        return head

    # merge the left and right halves
    def merge(self, left, right):
        pre = ListNode(0)   # assistant head
        node = pre
        while left is not None and right is not None:            
            node.next = left
            left = left.next
            node = node.next

            node.next = right
            right = right.next
            node = node.next

        if left is None:
            node.next = right
        else:
            node.next = left
        
        return pre.next

    def reorderList2(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # get the length of the linked list
        node, n = head, 0
        while node:
            node = node.next
            n += 1

        # iterate to the left half's tail
        node = head
        for i in range((n-1)//2):
            node = node.next
        
        # get the right half's head
        right = node.next
        # break the connection between left half and right half
        node.next = None

        # reverse the right half
        left, right = head, self.reverse(right)

        # merge the left and right half
        self.merge(left, right)

# fist trial, awkward
    def reorderList3(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        # two pointers to get the head of the right half
        # after this while loop, slow will be in the 1st element of right half (length: left >= right)
        fast, slow = head, head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next

            if fast is None:    # break the connection between left half and right half
                temp = slow.next
                slow.next = None
                slow = temp 
            else:
                slow = slow.next

        # reverse the right half part
        def reverse(head):
            if head is None:
                return head
            node = head.next
            head.next = None    # break the link between head and the second node
            while node:
                temp = node.next
                node.next = head
                head = node
                node = temp
            
            return head
        
        left = head
        right = reverse(slow)

        # Now merge the two linked lists
        while right:    # bug fixed: should not use "while left != slow" because length: left >= right
            tempL, tempR = left.next, right.next
            left.next = right
            right.next = tempL

            left = tempL
            right = tempR

obj = Solution()
l1 = ListNode(0)
l1.fromList([0, 1, 2, 3])
PrintLinkedList(l1)
print(obj.reorderList2(l1))
PrintLinkedList(l1)