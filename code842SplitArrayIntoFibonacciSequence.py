"""
842 Split Array into Fibonacci Sequence

Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
Note:

1 <= S.length <= 200
S contains only digits.
"""
class Solution:
    # my own DFS solution, the first two numbers determine the result, so we just iterate all combinations of first two numbers
    # bug fixed: must check first, second and third not exceeding MAX INTEGER
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n, MAX = len(S), 2**31 - 1
        if n < 3: 
            return []

        def validate(start, S, build):
            if start == len(S):
                return True

            first, second = build[-2], build[-1]
            third = first + second
            if third > MAX:
                return False

            target = str(third)
            end = start + len(target)
            if end <= len(S) and S[start:end] == target:
                build.append(third)
                return validate(end, S, build)

            return False

        for i in range(1, min(n-1, 11)):
            first = int(S[:i])
            if str(first) != S[:i] or first > MAX: # convert integer back to string to filter out leading-zero numbers such as "03"
                continue
            for j in range(i+1, min(n, i+11)):
                second = int(S[i:j])                
                if str(second) != S[i:j] or second > MAX:
                    continue
                build = [first, second]
                if validate(j, S, build):
                    return build
        
        return []


# S = "11235813" # expected [1, 1, 2, 3, 5, 8, 13]
# S = "000" # expected [0, 0, 0]
# S = "1101111"
S = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
print(Solution().splitIntoFibonacci(S))