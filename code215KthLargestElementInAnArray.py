"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
class Solution:
    # QuickSort partition method, average time complexity O(n)
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(nums, s, e):
            """
            Part of the Quicksort algorithm
            Partition the array with last element nums[e] as the pivot
            s: start index
            e: end index
            """
            i = s   # i is the candidate's index to be replaced by a number which is smaller than pivot
            for j in range(s, e):   # should not include the pivot, nums[e]
                if nums[j] < nums[e]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            # switch pivot (nums[e]) with nums[i]
            nums[i], nums[e] = nums[e], nums[i]
            # i is the position of pivot
            return i

        n = len(nums)
        s, e = 0, n-1
        while s <= e:
            i = partition(nums, s, e)
            if n-i == k:
                # we found it
                return nums[i]
            elif n-i < k:
                # kth element must be in left partition, drop the right patrtion part after pivot
                k -= e - i + 1  # bug fixed: calculated k wrong (forgot the 1)
                e = i - 1
                n = e - s + 1   # bug fixed: forgot to update n
            else:
                # n-i > k, kth element must be in right partition, drop the left partition part before pivot
                s = i + 1
                n = e - s + 1   # bug fixed: forgot to update n
        
test_case = [-1, 2, 0]
obj = Solution()
print(obj.findKthLargest(test_case, 3))