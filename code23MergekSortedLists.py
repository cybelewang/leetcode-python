"""
23 Merge K Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
from ListNode import *
from BinaryHeap import MinHeap

def mergeKLists(lists):
    """
    Divide and Conquer solution
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    r = len(lists) - 1
    if r < 0:       # bug fixed, for empty list
        return None
    while r > 0:
        # for odd number subarray, r//2 doesn't have a paired element, so decrease m by 1
        if r % 2 == 0:
            m = r//2 - 1
        else:
            m = r//2

        offset = r//2 + 1 # offset between paired elements' index, which is the lenth from 0 to r//2
        for i in range(m+1):
            lists[i] = mergeTwoLists(lists[i], lists[i + offset])

        r = r//2 # reduce the array size by a factor of 2

    return lists[0]
        

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = ListNode(0)
    node = head
    while l1 or l2:
        if not l1:
            node.next = l2
            break
        elif not l2:
            node.next = l1
            break
        else:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
                node = node.next
            else:
                node.next = l2
                l2 = l2.next
                node = node.next

    return head.next

def mergeKListsMinHeap(lists):
    """
    Solution with MinHeap
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    mh = MinHeap()
    for node in lists:
        if node:
            mh.insert(node)
    
    head = ListNode(0)
    node = head
    while mh.size > 0:
        minNode = mh.delMin()        
        nextNode = minNode.next
        if nextNode:
            mh.insert(nextNode)
        node.next = minNode
        node = node.next

    return head.next

# Use Python queue package's PriorityQueue, heapq cannot compare ListNode
# PriorityQueue's useful methods: empty(), put(item), get(item)
# Since we can't modify the given ListNode directly, we use a Wrapper
class Wrapper():
    def __init__(self, node):
        self.node = node
        
    def __lt__(self, other):
        return self.node.val < other.node.val
from queue import PriorityQueue    
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = PriorityQueue()
        for head in lists:
            if head:
                q.put(Wrapper(head))
        
        pseudoHead = ListNode(0)
        pre = pseudoHead
        
        while not q.empty():
            top = q.get().node
            pre.next = top
            pre = pre.next
            if top.next:
                q.put(Wrapper(top.next))
                
        return pseudoHead.next

l1, l2, l3 = ListNode(0), ListNode(0), ListNode(0)
l1.fromList([1, 3, 5, 7, 9])
l2.fromList([2, 4, 6, 8])
l3.fromList([0, 2, 3, 17])
l4 = mergeKLists([l1, l2, l3])
PrintLinkedList(l4)
