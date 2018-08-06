"""
In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision about a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: 
A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: 
If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and make the decision about the change in the game.
Given a string representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party respectively. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party, you need to predict which party will finally announce the victory and make the change in the Dota2 game. The output should be Radiant or Dire.

Example 1:
Input: "RD"
Output: "Radiant"
Explanation: The first senator comes from Radiant and he can just ban the next senator's right in the round 1. 
And the second senator can't exercise any rights any more since his right has been banned. 
And in the round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
Example 2:
Input: "RDD"
Output: "Dire"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in the round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in the round 1. 
And in the round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
Note:
The length of the given string will in the range [1, 10,000].
"""
from collections import deque
class Solution:
    # don't understand the problem. Compare count('R') and count('D')?
    # help from http://www.cnblogs.com/grandyang/p/7439222.html
    # the result can be determined in the middle of string if there are only 'R' or 'D' left
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)
        q1, q2 = deque(), deque()
        for i, s in enumerate(senate):
            if s == 'R':
                q1.append(i)
            else:
                q2.append(i)
        
        while q1 and q2:
            s1, s2 = q1.popleft(), q2.popleft()
            if s1 < s2:
                q1.append(s1+n)
            else:
                q2.append(s2+n)
            
        return 'Radiant' if q1 else 'Dire'

    # wrong solution, consider DDRRR
    def predictPartyVictory_trial(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        cnt_R = senate.count('R')
        cnt_D = senate.count('D')
        if cnt_R > cnt_D:
            return 'Radiant'
        elif cnt_R < cnt_D:
            return 'Dire'
        
        if senate[0] == 'R':
            return 'Radiant'
        else:
            return 'Dire'
            

test_cases = ['R', 'D', 'RDD', 'RRDD', 'DDRR', 'RDRD']
for s in test_cases:
    print(s, end = ' -> ')
    print(Solution().predictPartyVictory(s), end = ' -> ')
    print(Solution().predictPartyVictory_trial(s))