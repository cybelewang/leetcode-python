import unittest
from random import randrange
class Sort:
    def quicksort(self, nums):
        def partition(nums, start, end):
            """
            partition the list nums with the last element nums[end] as the pivot, 
            and return the position p for the pivot after partition, 
            so elements at start to p-1 are all smaller than nums[p], 
            and elements at p + 1 to end are all not smaller than nums[p]
            """
            pivot = nums[end]
            i = start
            for j in range(start, end):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1   # before swap, nums[i] >= pivot, so after swap, there is no need to process nums[j] again
            nums[i], nums[end] = nums[end], nums[i]
            return i
        
        def _quicksort(nums, start, end):
            if start < end:
                p = partition(nums, start, end)
                _quicksort(nums, start, p - 1)
                _quicksort(nums, p+1, end)
        
        # main
        _quicksort(nums, 0, len(nums)-1)

    # merge from small to large
    def mergesort(self, nums):
        def helper(nums, s, e):
            # merge and sort nums[s:e+1]
            if s >= e: return
            m = (s + e)//2
            # sort left half and right half
            helper(nums, s, m)
            helper(nums, m+1, e)
            # merge left half and right half
            temp = nums[s:e+1]
            j, k = m+1, 0
            for i in range(s, m+1):
                # put right half elements to sorted array as much as possible
                while j <= e and nums[i] >= nums[j]:
                    temp[k] = nums[j]
                    k += 1
                    j += 1
                temp[k] = nums[i]
                k += 1
            nums[s:e+1] = temp
 
        helper(nums, 0, len(nums)-1)
    
    # merge from large to small
    def mergesort2(self, nums):
        def sort(arr):
            n = len(arr)
            if n < 2: return arr
            left, right = sort(arr[:n//2]), sort(arr[n//2:])
            for i in range(n-1, -1, -1):
                if not right or left and left[-1] > right[-1]:
                    arr[i] = left.pop()
                else:
                    arr[i] = right.pop()
            return arr
        
        sort(nums)

class Test(unittest.TestCase):
    def test_1(self):
        obj = Sort()
        input = []
        obj.mergesort(input)
        self.assertEqual(input, [])
        obj.quicksort(input)
        self.assertEqual(input, [])

    def test_2(self):
        obj = Sort()
        input = [1, 2, 1, 2, 1]
        obj.mergesort(input)
        self.assertEqual(input, [1, 1, 1, 2, 2])
        input = [1, 2, 1, 2, 1]
        obj.quicksort(input)
        self.assertEqual(input, [1, 1, 1, 2, 2])

    def test_3(self):
        obj = Sort()
        input = []
        for _ in range(100):
            input.append(randrange(100))
        sort = sorted(input)
        obj.mergesort(input)
        self.assertEqual(input, sort)
    
    def test_4(self):
        obj = Sort()
        input = []
        for _ in range(100):
            input.append(randrange(100))
        sort = sorted(input)
        obj.quicksort(input)
        self.assertEqual(input, sort)

    def test_5(self):
        obj = Sort()
        input = []
        for _ in range(100):
            input.append(randrange(100))
        sort = sorted(input)
        obj.mergesort2(input)
        self.assertEqual(input, sort)

if __name__ == "__main__":
    unittest.main(exit = False)