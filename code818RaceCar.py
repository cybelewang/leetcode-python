"""
818 Race Car

Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following: position += speed, speed *= 2.

When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)

For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.

Now for some target position, say the length of the shortest sequence of instructions to get there.

Example 1:
Input: 
target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0->1->3.
Example 2:
Input: 
target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0->1->3->7->7->6.
"""
from collections import deque
class Solution:
    # DP solution
    # dp[t] represents the min instructions to achieve t
    # for 2**k - 1 position, the result is k
    # for t between 2**(k-1) - 1 and 2**k - 1, we have two options
    # option 1 - reset start position - after we achieved position 2**(k-1) - 1, now we reverse, then accelerate j steps, and we achieved another position pos = 2**(k-1) - 1 - (2**j - 1)
    # we reverse again and treat this pos as new start position, just like starting from 0, so the problem of t reduces to problem of t - pos, with additional steps (k - 1)(A) + 1(R) + j(A) + 1R
    # option 2 - cross and reverse - we passed t to position 2**k - 1, then we reverse and try to achieve t in reversed direction. Due to symmetric, we know the problem t reduces to problem of 2**k-1-t
    # the additional steps are k(A) + 1(R)
    def racecar_DP(self, target):
        LIMIT = 2**(target.bit_length()) - 1
        dp = [0, 1, 4] + [float('INF')]*(LIMIT-2)
        for t in range(3, target+1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t] = k
                continue
            # not cross t, but first reverse to position t - 2**(k-1) + 2**j, then reverse and accelerate to t
            for j in range(k-1):
                dp[t] = min(dp[t], dp[t - 2**(k-1) + 2**j] + k + j + 1)
            # first cross t to 2**k - 1, then reverse to t
            dp[t] = min(dp[t], k + 1 + dp[2**k - 1 - t])
        
        return dp[target]    
    # BFS solution with restrictions
    def racecar_BFS(self, target):
        if target == 0:
            return 0        
        # BFS solution
        level = 0
        q = deque([(0, 1)]) # tuple of (pos, speed)
        visited = {(0, 1),}
        while q:
            length = len(q)
            for _ in range(length):
                p, s = q.popleft()
                # use A
                new_p, new_s = p + s, 2*s
                if new_p == target:
                    return level + 1
                if 0 < new_p < 2* target and (new_p, new_s) not in visited:
                    visited.add((new_p, new_s))
                    q.append((new_p, new_s))
                # use R
                new_p, new_s = p, -s//abs(s)
                if 0 < new_p < 2* target and (new_p, new_s) not in visited:
                    visited.add((new_p, new_s))
                    q.append((new_p, new_s))
            level += 1
        return -1