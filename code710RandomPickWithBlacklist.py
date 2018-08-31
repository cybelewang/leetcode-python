"""
Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer from [0, N) which is NOT in B.

Optimize it such that it minimizes the call to system’s Math.random().

Note:

1 <= N <= 1000000000
0 <= B.length < min(100000, N)
[0, N) does NOT include N. See interval notation.
Example 1:

Input: 
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
Output: [null,0,0,0]
Example 2:

Input: 
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
Output: [null,1,1,1]
Example 3:

Input: 
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]
Example 4:

Input: 
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, N and the blacklist B. 
pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.

"""
# similar problems: 528 Random Pick with Weight
from random import randint
# help from https://my.oschina.net/yysue/blog/1846164
# map the number in blacklist to other numbers not in blacklist
class Solution:

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.M = N - len(blacklist)
        self.map = {b:-1 for b in blacklist}

        for b in blacklist:
            if b < self.M:
                while N-1 in self.map:
                    N -= 1
                self.map[b] = N - 1
                N -= 1
            
        print(self.map)

    def pick(self):
        """
        :rtype: int
        """
        p = randint(0, self.M-1)
        return self.map[p] if p in self.map else p


N, blacklist = 11, [2,3,5,8]
obj = Solution(N, blacklist)
print(obj.pick())

# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()