"""
703 Kth Largest Element in a Stream

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
from heapq import heappop, heappush
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.data = []
        self.k = k
        for num in nums:
            heappush(self.data, num)
            if len(self.data) > k:
                heappop(self.data)        

    def add(self, val: int) -> int:
        heappush(self.data, val)
        if len(self.data) > self.k:
            heappop(self.data)
        return self.data[0]

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

"""
["KthLargest","add","add","add","add","add"]
[[1,[]],[-3],[-2],[-4],[0],[4]]
"""