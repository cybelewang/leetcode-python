"""
In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring", and use the dial to spell a specific keyword in order to open the door.

Given a string ring, which represents the code engraved on the outer ring and another string key, which represents the keyword needs to be spelled. You need to find the minimum number of steps in order to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at 12:00 direction. You need to spell all the characters in the string key one by one by rotating the ring clockwise or anticlockwise to make each character of the string key aligned at 12:00 direction and then by pressing the center button. 
At the stage of rotating the ring to spell the key character key[i]:
You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. The final purpose of the rotation is to align one of the string ring's characters at the 12:00 direction, where this character must equal to the character key[i].
If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell, which also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage), otherwise, you've finished all the spelling.
Example:


Input: ring = "godding", key = "gd"
Output: 4
Explanation:
 For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
 For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
 Also, we need 1 more step for spelling.
 So the final output is 4.
Note:
Length of both ring and key will be in range 1 to 100.
There are only lowercase letters in both strings and might be some duplcate characters in both strings.
It's guaranteed that string key could always be spelled by rotating the string ring.
"""
from collections import defaultdict
class Solution:
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        m, n = len(key), len(ring)
        dp = [[0]*n for _ in range(m+1)]    # dp[i][j] is the min step from key[i] to ring[j], not including the steps to "spell". dp[m][0] is the start condition
        for i in range(m-1, -1, -1):
            for j in range(n):
                dp[i][j] = 2**31 - 1
                for k in range(n):
                    if ring[k] == key[i]:
                        diff = abs(j - k)
                        step = min(diff, n-diff)
                        dp[i][j] = min(dp[i][j], step + dp[i+1][k])

        return dp[0][0] + m # "m" are the "spell" steps

    # my own solution
    # use a intermediate list to keep a particular character's all possible (previous steps, index i in ring)
    # for the next character's each index j in ring, find out min steps between i and j and add this min steps to previous steps 
    # improvement: previously used a findMinStep(i, j, N) to calculate the min step between i and j, then improved to min(abs(i-j), N-abs(i-j))
    def findRotateSteps2(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        N = len(ring)
        mem = defaultdict(list)
        for i, c in enumerate(ring):
            mem[c].append(i)
        
        prev = [(0, 0)] # start tuple (steps, index)

        for c in key:
            c_indices = mem[c]  # get all indices of current character c in key
            cur = []    # this will hold all possible steps after processing character c
            for j in c_indices:
                p = (2**31-1, j)    # tuple (steps, index)
                for steps, i in prev:   # iterate all previous (steps, index) and add steps to rotate from previous character index i to current character index j, as well as 1 step to push the character
                    p = min(p, (steps + min(abs(i-j), N-abs(i-j)) + 1, j))
                cur.append(p)
            prev = cur

        return min(prev)[0]    
            
obj = Solution()
ring = "godding"
key = "gg"
print(obj.findRotateSteps(ring, key))