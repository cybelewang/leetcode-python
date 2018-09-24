"""
668 Kth Smallest Number in Multiplication Table

Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?

Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.

Example 1:
Input: m = 3, n = 3, k = 5
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).
Example 2:
Input: m = 2, n = 3, k = 6
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
Note:
The m and n will be in the range [1, 30000].
The k will be in the range [1, m * n]
"""
# similar problems: 378 Kth Smallest Element in a Sorted Matrix; 719 Find K-th Smallest Pair Distance
class Solution:
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        left, right = 1, m*n
        while left < right:
            mid, cnt = (left + right)//2, 0
            # count numbers <= mid
            for i in range(1, m+1):
                cnt += n if mid > n*i else mid//i
            # reset search boundaries
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        
        return right
    # WRONG SOLUTION! test m, n, k = 42, 34, 401, expected 126
    # solution 1 from http://www.cnblogs.com/grandyang/p/8367505.html
    # binary search the result, for each mid, count the numbers <= mid row by row
    def findKthNumber_WRONG(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        left, right = 1, m*n
        while left <= right:
            mid, cnt = (left + right)//2, 0
            # count numbers <= mid
            for i in range(1, m+1):
                cnt += n if mid > n*i else mid//i
            # reset search boundaries
            if cnt == k:
                left = mid
                break
            elif cnt < k:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

    # WRONG SOLUTION! test m, n, k = 42, 34, 401, expected 126
    # solution 2 from http://www.cnblogs.com/grandyang/p/8367505.html
    # binary search the result, for each mid, count the numbers <= mid using the below method:
    # start from the left bottom number (i, j) = (m, 1)
    # if i*j <= mid, count numbers from (1, j) to (i, j), then processed to next column by increasing j
    # if i*j > mid, decrease i
    def findKthNumber2(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        left, right = 1, m*n
        while left <= right:
            mid, cnt = (left + right)//2, 0
            # count numbers <= mid
            i, j = m, 1
            while i >= 1 and j <= n:
                if i*j <= mid:
                    cnt += i
                    j += 1
                else:
                    i -= 1
            # reset search boundaries
            if cnt == k:
                left = mid
                break
            elif cnt < k:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

print(Solution().findKthNumber(42,34,401))