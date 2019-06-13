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

    def mergesort(self, nums):
        def merge(nums, helper, low, middle, high):
            """
            merge two sorted subarrays, with middle as the dividing point
            """
            helper[low:high+1] = nums[low:high+1]   # copy nums[low:high+1] to helper list
            left, right = low, middle+1 # initialize left and right iterator
            # merge two halves, always take the smaller one
            for i in range(low, high+1):
                if left > middle:
                    nums[i] = helper[right]
                    right += 1
                elif right > high:
                    nums[i] = helper[left]
                    left += 1
                else:
                    if helper[left] < helper[right]:
                        nums[i] = helper[left]
                        left += 1
                    else:
                        nums[i] = helper[right]
                        right += 1

        def _mergesort(nums, helper, low, high):
            if low < high:
                middle = (low + high)//2    # dividing point
                _mergesort(nums, helper, low, middle)   # recursively process left half
                _mergesort(nums, helper, middle + 1, high)  # recursively process right half
                merge(nums, helper, low, middle, high)  # merge left and right half
        
        # main
        helper = nums[:]
        _mergesort(nums, helper, 0, len(nums)-1)

if __name__ == "__main__":
    obj = Sort()
    test_input = [[], [1, 2, 1, 2, 1], [3, 0, 8, 2], [5, 4, 3, 6, 1]]
    for nums in test_input:
        obj.mergesort(nums)
        print(nums)