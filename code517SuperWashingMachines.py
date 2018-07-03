"""
You have n super washing machines on a line. Initially, each washing machine has some dresses or is empty.

For each move, you could choose any m (1 ≤ m ≤ n) washing machines, and pass one dress of each washing machine to one of its adjacent washing machines at the same time .

Given an integer array representing the number of dresses in each washing machine from left to right on the line, 
you should find the minimum number of moves to make all the washing machines have the same number of dresses. If it is not possible to do it, return -1.

Example1

Input: [1,0,5]

Output: 3

Explanation: 
1st move:    1     0 <-- 5    =>    1     1     4
2nd move:    1 <-- 1 <-- 4    =>    2     1     3    
3rd move:    2     1 <-- 3    =>    2     2     2   
Example2

Input: [0,3,0]

Output: 2

Explanation: 
1st move:    0 <-- 3     0    =>    1     2     0    
2nd move:    1     2 --> 0    =>    1     1     1     
Example3

Input: [0,2,0]

Output: -1

Explanation: 
It's impossible to make all the three washing machines have the same number of dresses. 
Note:
The range of n is [1, 10000].
The range of dresses number in a super washing machine is [0, 1e5].
"""
class Solution:
    # https://blog.csdn.net/tstsugeg/article/details/62427718
    # better to understand
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        n = len(machines)
        if n < 1:
            return 0

        sum_ = [0]
        for m in machines:
            sum_.append(sum_[-1] + m)

        if sum_[-1] % n != 0:
            return -1

        avg = sum_[-1] // n
        res = 0
        for i in range(n):
            leftCnt = sum_[i] - avg*i   # total dresses from left to right, through machine i
            rightCnt = sum_[-1] - sum_[i+1] - avg*(n - i - 1)   # total dress from right to left, through machine i
            if leftCnt > 0 and rightCnt > 0:
                # machine i needs to receive dress from both neighbors
                res = max(res, max(leftCnt, rightCnt))
            elif leftCnt < 0 and rightCnt < 0:
                # machine i needs to give dresses to both neighbors, this cannot be done at the same time
                res = max(res, -leftCnt - rightCnt)
            else:
                res = max(res, max(abs(leftCnt), abs(rightCnt)))
        
        return res
        

    # http://www.cnblogs.com/grandyang/p/6648557.html
    def findMinMoves2(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        n, sum_ = len(machines), sum(machines)
        if sum_ % n != 0:
            return -1

        res, cnt, avg = 0, 0, sum_//n
        for m in machines:
            cnt += m - avg
            # A machine can receive two dresses from both neighboring machines at the same time, but cannot pass two dresses to both neighbors at the same time
            # abs(cnt) is the net amount of dress need to go to m (or leave m)
            # (m - avg) is the amount of dress that will leave m to neighbors. if m < avg, then (m-avg) < 0 and it will never compete with abs(cnt)
            res = max(res, max(abs(cnt), m-avg)) 
            # consider [3, 6, 3] and [6, 3, 6]

        return res

    # my own wrong solution, due to misunderstanding of the problem.
    # the basic idea is one dress can be passed from any index i to any index j
    def findMinMoves_Wrong(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        n, sum_ = len(machines), sum(machines)
        if sum_ % n != 0:
            return -1

        avg = sum_//n
        return sum(map(lambda x: abs(x-avg), machines))//2  # should not use reduce, why?

obj = Solution()
machines = [4, 0, 0, 4]
print(obj.findMinMoves(machines))
# test case [4, 0, 0, 4], expected 2
# explanation:
# 1st step: 4 --> 0, 0 <-- 4    =>    3, 1, 1, 3
# 2nd step: 3 --> 1, 1 <-- 3    =>    2, 2, 2, 2