"""
179 Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not any(nums):   # bug fixed: forgot corner case [0, 0]
            return '0'
        # convert x and y to list of digits, then compare new list [x:y] and [y:x]
        def compare(x, y):
            a, b =[x%10], [y%10]
            x //= 10
            y //= 10
            while x > 0:
                a.append(x%10)
                x //= 10
            while y > 0:
                b.append(y%10)
                y //=10
            d1, d2 = a[::-1], b[::-1]
            d1.extend(b[::-1])
            d2.extend(a[::-1])
            for i in range(len(d1)):
                if d1[i] > d2[i]:
                    return -1
                elif d1[i] < d2[i]:
                    return 1
            
            return 0
        
        # Python3 removed cmp, but we can use cmp_to_key in functools to get the key
        # https://py.checkio.org/blog/how-did-python3-lose-cmd-sorted/
        return ''.join(map(str, sorted(nums, key = cmp_to_key(lambda x, y: compare(x, y)))))

    # 2nd round solution on 1/28/2019 with simplified compare function
    def largestNumber2(self, nums):
        if not any(nums):
            return '0'
        
        def compare(x, y):
            xy, yx = str(x)+str(y), str(y)+str(x)
            if xy < yx:
                return 1
            elif xy > yx:
                return -1   # we want bigger element comes first
            else:
                return 0
        
        return ''.join(map(str, sorted(nums, key=cmp_to_key(lambda x, y: compare(x, y)))))

obj = Solution()
test_cases = [[0],[0, 0], [1, 0], [1], [0, 10, 100, 1000], [19, 199], [39, 3], [33, 3], [32, 3], [31, 311], [3, 30, 34, 5, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
for case in test_cases:
    print(obj.largestNumber2(case))