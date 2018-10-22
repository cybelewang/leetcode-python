"""
838 Push Dominoes

There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Note:

0 <= N <= 10^5
String dominoes contains only 'L', 'R' and '.'
"""
from collections import deque
class Solution:
    # my own solution using a trick to append "L" at head and "R" at tail
    # then save all letters (not '.') and their positions into a queue
    # 
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        dominoes = 'L' + dominoes + 'R'
        q = deque([(d, i) for i, d in enumerate(dominoes) if d != '.'])
        
        left = q.popleft()
        a = [left[0]]
        while q:    # left already filled, need to fill until right
            right = q.popleft()
            n = right[1] - left[1]
            if left[0] == right[0]: # either "L.....L" or "R......R", we just fill with the same letters
                a.extend([left[0]]*n)
            elif left[0] == 'R':    # "R.....L", we need to fill left half with "R" and right half with "L"
                a.extend(['R']*((n-1)//2))
                if n & 1 == 0:
                    a.append('.')
                a.extend(['L']*((n+1)//2))
            else:   # "L.........R", just fill with "."
                a.extend(['.']*(n-1))
                a.append('R')

            left = right
        
        return ''.join(a[1:-1])

#dominoes = ".L.R...LR..L.."
dominoes = "RR.L"
#dominoes = "......"
print(Solution().pushDominoes(dominoes))
