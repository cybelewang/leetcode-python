"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    lists = list(filter((lambda x: x != None), lists))
    lists.sort(key = lambda node: node.val)
    