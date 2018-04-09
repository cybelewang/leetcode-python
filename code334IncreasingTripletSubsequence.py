"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
"""
# related to problem 300
class Solution:
    # https://leetcode.com/problems/increasing-triplet-subsequence/discuss/78993/Clean-and-short-with-comments-C++
    """
    before coding I also thought about this solution and I did’t think that will work, as it appears to be very naïve and greedy: find first smallest, then find second smallest, then find the third and bingo. I argued myself it cannot pass the case like [1,2,0,3] since c1 is changed.
    But when I take a closer look, it does [1,2,0,3] very well. And I realize that c1 and c2 are indeed having the meaning of:
    c1 = so far best candidate of end element of a one-cell subsequence to form a triplet subsequence
    c2 = so far best candidate of end element of a two-cell subsequence to form a triplet subsequence
    So c1 and c2 are the perfect summary of history.
    """
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c1, c2 = 2**31 - 1, 2**31 -1
        for num in nums:
            if num <= c1:
                c1 = num
            elif num <= c2:
                c2 = num
            else:
                return True

        return False

test_case = [1, 2, 0, 0, 3]
obj = Solution()
print(obj.increasingTriplet(test_case))