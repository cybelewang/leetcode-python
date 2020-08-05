"""
670 Maximum Swap

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 10^8]
"""
class Solution:
    # for each digit, we need to find the max digit from its right that is (1) bigger than current digit, (2) most right comparing to other equal digits
    # therefore, we should scan from right to left when looking for this most-right max bigger digit
    # consider 1993 -> 9913, 98368 -> 98863
    def maximumSwap(self, num: int) -> int:
        a = list(str(num))
        for i in range(len(a)):
            idx = i
            for j in range(len(a)-1, i, -1):                
                if a[j] > a[idx]:
                    idx = j
            if idx > i:
                a[i], a[idx] = a[idx], a[i]
                return int(''.join(a))
        return num

    # if we scan from left to right to look for the most-right max bigger digit, we should consider the equal case
    def maximumSwap2(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))
        n = len(s)
        for i in range(n-1):
            bFound = False
            k = i
            for j in range(i+1, n):
                if s[j] > s[k] or (k != i and s[j] == s[k]):
                    k = j
                    bFound = True
            
            if bFound:
                s[i], s[k] = s[k], s[i]
                return int(''.join(s))

        return num
    # WRONG SOLUTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # 1993, expected 9913
    def maximumSwap_WRONG(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))
        n = len(s)
        for i in range(n-1):
            bFound = False
            k = i
            for j in range(i+1, n):
                if s[j] > s[k]:
                    k = j
                    bFound = True
            
            if bFound:
                s[i], s[k] = s[k], s[i]
                return int(''.join(s))

        return num

    # WRONG SOLUTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # my own solution
    # convert num to string, then for every digit s[i], try to find a bigger digit on its right side
    def maximumSwap_WRONG2(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        n = len(s)
        for i in range(n-1):
            for j in range(i+1, n):
                if s[i] < s[j]:
                    a = list(s)
                    a[i], a[j] = a[j], a[i]
                    return int(''.join(a))
        
        return num

test_cases = [0, 12, 2736, 9973, 1111, 9867, 98368, 1993]
obj = Solution()
for num in test_cases:
    print(num, end = ' -> ')
    print(obj.maximumSwap(num))