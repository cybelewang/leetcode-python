"""
254 Factor Combinations

Numbers can be regarded as product of its factors. For example,
8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.
Note:
You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1: 
Input: 1
Output: []
Example 2: 
Input: 37
Output:[]
Example 3: 
Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4: 
Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]	
"""
class Solution:
    def getFactors(self, n):
        def dfs(start, n): # bug 2: recursively call the getFactors itself is wrong, this may cause duplicate results. We need to define a dfs with restrictions of start number.
            i = start
            res = []
            while i*i <= n: # bug 1: i*i<=n, not i*i<n, think the case 2*2=4
                if n%i == 0:
                    res.append([i, n//i])
                    for f in dfs(i, n//i):
                        res.append([i] + f)
                i += 1
            return res
        
        # main
        if n < 2: return []
        return dfs(2, n)


print(Solution().getFactors(32))