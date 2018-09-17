class BinarySearch:

    # applied to problems: 349
    def findExact(nums, target):
        """
        input nums is a sorted array
        find the index of target in nums
        if target cannot be found, return -1
        """
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        
        return -1
    
    # applied to problems: Heaters， Arranging Coins， Valid Perfect Square，Max Sum of Rectangle No Larger Than K，Russian Doll Envelopes, Valid Triangle Number
    def lower_bound(nums, target):
        """
        similar to C++'s lower_bound
        input nums is a sorted array
        find the index of a number in nums, which is the first number >= target
        """
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return right

    # applied to problems: Kth Smallest Element in a Sorted Matrix, Sqrt(x)
    def upper_bound(nums, target):
        """
        similar to C++'s upper_bound
        input nums is a sorted array
        find the index of a number in nums, which is the first number > target
        """
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] <= target: # the only difference between upper_bound and lower_bound
                left = mid + 1
            else:
                right = mid
        
        return right

A = list(range(5))
print(A, sep=' ')

def BinarySearch(A, value):
    l = 0
    r = len(A) - 1
    while l <= r:
        mid = (l + r)//2
        if A[mid]==value:
            return mid
        elif A[mid]<value:
            l = mid + 1
        else:
            r = mid - 1
    return -1

print("The index of 1 is {}",BinarySearch(A, 1))