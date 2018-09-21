"""
216 Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""
class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # quickly resolve corner cases
        if k > n or k > 9 or n > 45:
            return []

        def combination(res, build, s, k, n):
            """
            s: start number
            k: remaining numbers
            n: remaing sum
            """
            if k == 0:
                if n == 0:
                    res.append(build[:])
                return
            elif n <= 0:
                return
            else:                
                for i in range(s, min(10, n+1)):
                    build.append(i)
                    combination(res, build, i+1, k-1, n-i)
                    build.pop()

        res, build = [], []
        combination(res, build, 1, k, n)

        return res

obj = Solution()
print(obj.combinationSum3(9, 45))    
