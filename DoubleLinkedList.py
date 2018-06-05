"""
Doubly Linked List Class, modified from problem 146 LRU Cache
"""

# definition of the double linked list node
class ListNode(object):
    
    def __init__(self, x):
        """
        :type x: tuple
        we need tuple because 
        """
        self.val = x
        self.prev = None
        self.next = None

# definition of the double linked list
class DoubleLinkedList(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self._len = 0

    def __len__(self):
        return self._len

    def isempty(self):
        return self._len == 0
    
    def append_head(self, node):
        """
        append node to head
        :type node: ListNode
        :rtype: void
        """
        if node is None:
            return

        node.next = self.head   # connect node to the head

        if self.head is None:
            self.tail = node    # don't forget to update tail if this is the first node in the linked list
        else:
            self.head.prev = node

        self.head = node

        # increase the length
        self._len += 1

    def append(self, node):
        """
        append node to tail
        :type node: ListNode
        :rtype: void
        """
        if node is None:
            return

        node.prev = self.tail    # connect node to the tail

        if self.tail is None:
            self.head = node    # don't forget to update head if this is the first node in the linked list
        else:
            self.tail.next = node

        self.tail = node

        # increase the length
        self._len += 1

    def remove(self, node):
        """
        remove a node from the linked list
        :type node: ListNode
        :rtype: void
        """
        if node is None:
            return

        # save the prev and next for node
        prev = node.prev
        next = node.next

        # disconnect node
        node.prev = None
        node.next = None

        # process the left to right link
        if prev is None:
            self.head = next
        else:
            prev.next = next

        # process the right to left link
        if next is None:
            self.tail = prev
        else:
            next.prev = prev

        # decrease the length
        self._len -= 1

    def insert_before(self, reference, node):
        """
        insert a node to the linked list, just before the reference
        :type reference: ListNode
        :type node: ListNode
        :rtype: void
        """
        if node is None:
            return

        if reference is None:
            # insert node to an empty linked list
            self.append_head(node)
            return

        # save the prev of reference
        prev = reference.prev

        # process the left to right link
        node.next = reference
        if prev is None:
            self.head = node
        else:
            prev.next = node

        # process the right to left link
        node.prev = prev
        reference.prev = node

        # increase the length
        self._len += 1

    def insert_after(self, reference, node):
        """
        insert a node to the linked list, just after the reference
        :type reference: ListNode
        :type node: ListNode
        :rtype: void
        """
        if node is None:
            return

        if reference is None:
            # insert node to an empty linked list
            self.append(node)
            return

        # save the next of reference
        next = reference.next

        # process the left to right link
        reference.next = node
        node.next = next

        # process the right to left link
        node.prev = reference
        if next is None:
            self.tail = node
        else:
            next.prev = node

        # increase the length
        self._len += 1
