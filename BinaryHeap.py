class MinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.size = 0
    
    def insert(self, element):
        """
        Insert an element into the min heap
        Step 1: put the new element into the end of heap list
        Step 2: check if the new element's parent is smaller than it. If not, swap the parent and child. Keep doing this until new element reaches the root
        """
        self.heaplist.append(element)
        self.size += 1
        child, parent = self.size, self.size//2
        # if parent is larger than child, swap parent and child until reaching the root
        while (parent > 0) and (self.heaplist[child] < self.heaplist[parent]):
            self.heaplist[child], self.heaplist[parent] = self.heaplist[parent], self.heaplist[child]
            child = parent
            parent = child//2   # For binary heap, left child's index is 2*parent, and right child's index is 2*parent + 1
        
    def delMin(self):
        """
        Remove the minimum node from the root, then rebalance the binary heap
        Step 1: put the last node to the root, and reduce the size of the the heap list by 1
        Step 2: keep swapping the parent node and its smallest child (why smallest child? because after swapping, the new parent must be smaller than both children)
        """
        if self.size < 1:
            return None
        else:
            result = self.heaplist[1]
            self.heaplist[1] = self.heaplist[self.size]
            self.heaplist.pop()
            self.size -= 1            

            parent = 1            
            while parent <= self.size//2:
                left, right = 2*parent, 2*parent + 1
                child = left
                if (right <= self.size) and (self.heaplist[right] < self.heaplist[left]):
                    child = right
                if self.heaplist[child] < self.heaplist[parent]:
                    self.heaplist[child], self.heaplist[parent] = self.heaplist[parent], self.heaplist[child]                 
                    parent = child
                else:
                    break

            return result