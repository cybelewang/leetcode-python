class Sort:
    def quicksort(self, nums):
        def partition(nums, start, end):
            """
            partition the list nums with the last element nums[end] as the pivot, and return the position p for the pivot after partition, 
            so elements at start to p-1 are all smaller than nums[p], 
            and elements at p + 1 to end are all not smaller than nums[p]
            """
            pivot = nums[end]
            i = start
            for j in range(start, end):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[end] = nums[end], nums[i]
            return i
        
        def _quicksort(nums, start, end):
            if start < end:
                p = partition(nums, start, end)
                _quicksort(nums, start, p - 1)
                _quicksort(nums, p+1, end)
        
        # main
        _quicksort(nums, 0, len(nums)-1)


if __name__ == "__main__":
    obj = Sort()
    test_input = [[], [1, 2, 1, 2, 1], [3, 0, 8, 2], [5, 4, 3, 6, 1]]
    for nums in test_input:
        obj.quicksort(nums)
        print(nums)