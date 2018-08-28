"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. 
For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note: 
You may assume that nums' length ≥ k-1 and k ≥ 1.

"""
from heapq import heapify, heappushpop
class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        nums.sort()
        self.heap = nums[-k:]
        heapify(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        top = self.heap[0]
        if top < val:
            heappushpop(self.heap, val)
            
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

arr, k = [4,5,8,2], 3
obj = KthLargest(k, arr)
print(obj.add(3))   # returns 4
print(obj.add(5))   # returns 5
print(obj.add(10))  # returns 5
print(obj.add(9))   # returns 8
print(obj.add(4))   # returns 8