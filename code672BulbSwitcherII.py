"""
There is a room with n lights which are turned on initially and 4 buttons on the wall. 
After performing exactly m unknown operations towards buttons, you need to return how many different kinds of status of the n lights could be.

Suppose n lights are labeled as number [1, 2, 3 ..., n], function of these 4 buttons are given below:

Flip all the lights.
Flip lights with even numbers.
Flip lights with odd numbers.
Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...

Example 1:
Input: n = 1, m = 1.
Output: 2
Explanation: Status can be: [on], [off]
Example 2:
Input: n = 2, m = 1.
Output: 3
Explanation: Status can be: [on, off], [off, on], [off, off]
Example 3:
Input: n = 3, m = 1.
Output: 4
Explanation: Status can be: [off, on, off], [on, off, on], [off, off, off], [off, on, on].
Note: n and m both fit in range [0, 1000].

"""
# similar problems: 319 Bulb Switcher
from collections import deque
class Solution:
    # https://discuss.leetcode.com/topic/102395/2-short-lines-simple-formula
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        n = min(n, 3)
        return min(1<<n, 1+m*n)

    # help from http://www.cnblogs.com/grandyang/p/7595595.html
    # 1. repeated pattern every 6 numbers, so we can use an integer to represent the state
    # 2. BFS and use a set to record the state
    def flipLights2(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        def fn1(num, n):
            x = (1<<n) - 1
            return num ^ x

        def fn2(num, n):
            for i in range(0, n, 2):
                num ^= (1<<i)
            return num

        def fn3(num, n):
            for i in range(1, n, 2):
                num ^= (1<<i)
            return num

        def fn4(num, n):
            for i in range(0, n, 3):
                num ^= (1<<i)
            return num

        if n > 6:
            n = n % 6 + 6
        
        start = (1<<n) - 1  # start state
        s, q = set(), deque()
        q.append(start)

        for _ in range(m):
            len_ = len(q)
            s.clear()
            for _ in range(len_):
                num = q.popleft()
                next = [fn1(num, n), fn2(num, n), fn3(num, n), fn4(num, n)]
                for num in next:
                    if num not in s:
                        q.append(num)
                        s.add(num)
        
        return len(s)

n, m = 3, 1
print(Solution().flipLights(n, m))
