"""
299 Bulls and Cows

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. 
Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") 
and how many digits match the secret number but locate in the wrong position (called "cows"). 
Your friend will use successive guesses and hints to eventually derive the secret number.

For example:

Secret number:  "1807"
Friend's guess: "7810"
Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. In the above example, your function should return "1A3B".

Please note that both secret number and friend's guess may contain duplicate digits, for example:

Secret number:  "1123"
Friend's guess: "0111"
In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow, and your function should return "1A1B".
You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
"""
from collections import deque, Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0    
        sCnt, gCnt = Counter(), Counter()
        for a, b in zip(secret, guess):
            if a == b:
                bulls += 1
            else:
                sCnt[a] += 1
                gCnt[b] += 1
        cows = 0
        for d in sCnt:
            cows += min(sCnt[d], gCnt[d])
        return '{0}A{1}B'.format(bulls, cows)

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        counts = [0]*10
        bulls_index = deque()
        bulls, cows = 0, 0

        for i, c in enumerate(secret):
            if guess[i] == c:
                bulls += 1
                bulls_index.append(i)
            else:
                counts[ord(c)-ord('0')] += 1

        for i, c in enumerate(guess):
            if len(bulls_index) > 0 and i == bulls_index[0]:
                bulls_index.popleft()
            else:
                if counts[ord(c) - ord('0')] > 0:
                    cows += 1
                    counts[ord(c) - ord('0')] -= 1
        
        return str(bulls)+'A'+str(cows)+'B'

test_cases = [('1807', '7810'), ('1123', '0111'), ('',''), ('0','1'), ('01111','01100'), ('01','10')]
obj = Solution()
for (secret, guess) in test_cases:
    print(obj.getHint(secret, guess))