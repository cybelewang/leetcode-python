"""
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. 
Since it has limited resources, it can only finish at most k distinct projects before the IPO. 
Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given several projects. For each project i, it has a pure profit Pi and a minimum capital of Ci is needed to start the corresponding project. 
Initially, you have W capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

To sum up, pick a list of at most k distinct projects from given projects to maximize your final capital, and output your final maximized capital.

Example 1:
Input: k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].

Output: 4

Explanation: Since your initial capital is 0, you can only start the project indexed 0.
             After finishing it you will obtain profit 1 and your capital becomes 1.
             With capital 1, you can either start the project indexed 1 or the project indexed 2.
             Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
             Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Note:
You may assume all numbers in the input are non-negative integers.
The length of Profits array and Capital array will not exceed 50,000.
The answer is guaranteed to fit in a 32-bit signed integer.
"""
# Note the question asks for the final capital, not the profit
from heapq import heappush, heappop
class Solution:
    # my own solution: sort the tuple (capital, profit), then add all tuple (profit, capital) into MaxHeap if capital <= current
    # loop k times, each time pick up a max tuple (profit, capital), update the current W, then add all all tuple (profit, capital) into MaxHeap if capital <= W
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        t = sorted(zip(map(lambda x: -x, Profits), Capital), key = lambda x: x[1])  # heapq is a MinHeap, so we use negative profit values
        heap = []
        i = 0
        # initially add all tuples into MaxHeap if capital <= W
        while i < len(t) and t[i][1] <= W:
            heappush(heap, t[i])
            i += 1
        
        # loop k times
        for _ in range(k):
            if heap:
                p, _ = heappop(heap)    # max profit with capital <= W
                W += -p
                # similarily add all tuples into MaxHeap if capital <= W
                while i < len(t) and t[i][1] <= W:
                    heappush(heap, t[i])
                    i += 1
            else:
                break
        
        return W

Profits=[1,2,3]
Capital=[1, 1, 2]
k=1
W=2
print(Solution().findMaximizedCapital(k, W, Profits, Capital))