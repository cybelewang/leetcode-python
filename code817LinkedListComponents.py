"""
817 Linked List Components

We are given head, the head node of a linked list containing unique integer values.

We are also given the list G, a subset of the values in the linked list.

Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

Example 1:

Input: 
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation: 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
Example 2:

Input: 
head: 0->1->2->3->4
G = [0, 3, 1, 4]
Output: 2
Explanation: 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
Note:

If N is the length of the linked list given by head, 1 <= N <= 10000.
The value of each node in the linked list will be in the range [0, N - 1].
1 <= G.length <= 10000.
G is a subset of all values in the linked list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import *
class Solution:
    # my own solution
    # only when there was no previous connection and current node value is in G, then we increase the count
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        S, res = set(G), 0
        pre = False # previous connection in G
        while head:
            if head.val in S:
                if not pre:
                    res += 1
                    pre = True
            else:
                pre = False

            head = head.next

        return res

a = [0, 1, 2, 3]
G = [0, 1, 3]   # expected 2
#a = [1,2,0,4,3]
#G = [3,4,0,2,1] # expected 1
head = CreateLinkedList(a)
print(Solution().numComponents(head, G))