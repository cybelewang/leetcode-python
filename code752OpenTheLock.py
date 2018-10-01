"""
752 Open the Lock

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:
Input: deadends = ["0000"], target = "8888"
Output: -1
Note:
The length of deadends will be in the range [1, 500].
target will not be in the list deadends.
Every string in deadends and the string target will be a string of 4 digits from the 10,000 possibilities '0000' to '9999'.
"""
from functools import reduce
from collections import deque
class Solution_OJBest:
    def successors(self, src):
        res = []
        for i, ch in enumerate(src):
            num = int(ch)
            res.append(src[:i] + str((num - 1) % 10) + src[i+1:])
            res.append(src[:i] + str((num + 1) % 10) + src[i+1:])
        return res
    
    def num_moves(self, target):     
        ans = 0
        for c in target:
            d = int(c)
            ans += min(d, (10-d))
        return ans
    
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if '0000' in deadends:
            return -1
        
        endpoints = self.successors(target)
        min_moves = self.num_moves(target)
        impossible = True
        
        for p in endpoints:
            if p not in deadends:
                impossible = False
                potential = self.num_moves(p)
                if potential < min_moves:
                    return min_moves
        
        return -1 if impossible else min_moves + 2

# my own BFS solution
class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def encode(s):
            """
            encode string represented number to a 4-digit integer
            """
            return reduce(lambda x, y: 10*x + y, map(lambda c: ord(c) - ord('0'), s))
        
        def getneighbors(num):
            """
            get a list of neighboring numbers with only one digit has a difference of 1
            """
            res, factor = [], 1000
            for _ in range(4):
                digit = num%(factor*10)//factor
                remain = num - digit*factor

                res.append(((digit + 1)%10)*factor + remain)
                res.append(((digit - 1 + 10)%10)*factor + remain)

                factor //= 10

            return res

        # main
        deadnums = set(map(encode, deadends))
        end = encode(target)
        if 0 in deadnums:
            return -1

        visited = [False]*10000
        q, turns = deque([0]), 0
        visited[0]= True
        while q:
            #print(q)
            n = len(q)
            turns += 1
            for _ in range(n):
                start = q.popleft()
                for neighbor in getneighbors(start):
                    if neighbor == end:
                        return turns
                    if neighbor in deadnums or visited[neighbor]:
                        continue
                    q.append(neighbor)
                    visited[neighbor] = True
        
        return -1

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
#deadends = ["0000"]
#target = "8888"
obj = Solution()
print(obj.openLock(deadends, target))            
