"""
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

"""
from collections import deque
class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        stack = deque(range(min(9, n), 0, -1))   # initialize queue with 9 to 0
        res = []
        while len(stack) > 0:
            num = stack.pop()
            stack.extend(filter(lambda x: x<=n, range(num*10+9, num*10-1, -1)))           
            res.append(num)
        
        return res

    # recursive solution
    def lexicalOrder2(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 1:
            return []       
        
        def addNums(res, num, n):
            """
            subfunction to add numbers into result
            the given num has trailing zeros but > 0, such as 110
            """
            for i in range(10):
                if num + i <= n:
                    res.append(num+i)   # first, add this number
                    addNums(res, (num+i)*10, n) # second, x10 and recursively call addNums
                else:
                    break
        
        res = []
        for j in range(1, 10):  # addNums starts from x10, but we do not start from 0, so we need to explicitly give the start "seeds"
            if j <= n:
                res.append(j)
                addNums(res, j*10, n)

        return res

obj = Solution()
print(obj.lexicalOrder(33))
            