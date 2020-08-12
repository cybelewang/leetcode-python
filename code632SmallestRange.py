"""
632 Smallest Range Covering Elements from K Lists

You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Note:
The given list may contain duplicates, so ascending order means >= here.
1 <= k <= 3500
-10^5 <= value of elements <= 10^5.
For Java users, please note that the input type has been changed to List<List<Integer>>. And after you reset the code template, you'll see this point.
"""
# similar problems: 76 Minimum Window Substring
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/7200016.html
    # initially thinking of merge sort, but cannot keep all candidate numbers for boarders after merging
    # key is to use a large list to hold all the numbers and its corresponding array's id
    # then we need to find a minimum window to hold at least a number from each array
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        k = len(nums)
        # change nums from numbers to tuples (value, index of array)
        for i in range(k):
            nums[i] = list(zip(nums[i], [i]*len(nums[i])))
        
        a = sorted(sum(nums, []))
        #print(a)
        
        # find the min window to hold at least one number from each array
        count = {}  # key - the array index, value - count of numbers in that array
        required, i = k, 0
        res= []

        # sliding window algorithm, similar to problem 76
        for j in range(len(a)):
            rvalue, rindex = a[j]
            if required > 0:
                count[rindex] = 1 + count.get(rindex, 0)
                if count[rindex] == 1:
                    required -= 1                

            # we should not use else statement below because required may be 0 after above statement
            while required == 0:
                lvalue, lindex = a[i]
                delta = rvalue - lvalue
                # update final result
                if not res or delta < res[1] - res[0] or (delta == res[1] - res[0] and lvalue < res[0]):
                    res = [lvalue, rvalue]
                    #print(delta, res)

                count[lindex] -= 1
                if count[lindex] == 0:
                    required += 1
                i += 1

        return res

    # 8/10/2020
    # rewrite code according to count-based sliding window style, see OneNote
    def smallestRange(self, nums: List[List[int]]) -> List[int]:       
        for i, num in enumerate(nums):
            nums[i] = list(zip(num, [i]*len(num)))
        arr = sorted(sum(nums, []))
        req = len(nums)
        diff = [1]*len(nums)
        i = 0
        s, e = 0, -1
        for j in range(len(arr)):
            # add arr[j] to window
            right, k = arr[j]
            diff[k] -= 1
            if diff[k] >= 0:
                req -= 1
            # only update result when condition is met
            if req == 0:
                # shrink window until condition is not met
                while i <=j and req == 0:
                    left, p = arr[i]
                    diff[p] += 1
                    if diff[p] > 0:
                        req += 1
                    i += 1
                # update result accordingly
                if s > e:
                    s, e = arr[i-1][0], arr[j][0]                    
                elif e - s > arr[j][0] - arr[i-1][0] or (e-s == arr[j][0] - arr[i-1][0] and arr[i-1][0] < s):
                    s, e = arr[i-1][0], arr[j][0]
                    
        return [s, e]

nums = [[1]]
#nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
print(Solution().smallestRange(nums))