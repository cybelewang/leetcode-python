from ListNode import ListNode
from BinaryHeap import MinHeap

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
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

l1, l2, l3 = ListNode(0), ListNode(0), ListNode(0)
l1.fromList([1, 3, 5, 7, 9])
l2.fromList([2, 4, 6, 8])
l3.fromList([0, 2, 3, 17])
l4 = mergeKLists([l1, l2, l3])
l4.printAll()
