from ListNode import ListNode
from BinaryHeap import MinHeap

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
def mergeKLists(lists):
    """
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
l4 = mergeKLists([l2, l1, l3])
l4.printAll()