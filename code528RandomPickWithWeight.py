"""
528 Random Pick with Weight

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""
from random import randrange
from bisect import bisect_right
class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.board = []
        self.upper = 0
        for val in w:
            self.upper += val
            self.board.append(self.upper)

    def pickIndex(self):
        """
        :rtype: int
        """
        i = randrange(0, self.upper)    # randrange(a, b) will generate integer in range [a, b), excluding b
        return bisect_right(self.board, i)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
obj = Solution([1, 3, 2])
probability = [0, 0, 0]
for i in range(10000):
    probability[obj.pickIndex()] += 1
print(probability)