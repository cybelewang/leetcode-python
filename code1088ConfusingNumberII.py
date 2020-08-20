"""
1088 Confusing Number II

We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.

A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.)

Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.

Example 1:

Input: 20
Output: 6
Explanation: 
The confusing numbers are [6,9,10,16,18,19].
6 converts to 9.
9 converts to 6.
10 converts to 01 which is just 1.
16 converts to 91.
18 converts to 81.
19 converts to 61.
Example 2:

Input: 100
Output: 19
Explanation: 
The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].
 
Note:

1 <= N <= 10^9
"""
class Solution:
    # We can't verify each number between 1 to N is confusing, however, there are 5 digits, so we can generate the confusing numbers on the fly
    # DFS with helper function with input: num - the original number, rotate - rotate of original number, factor - factor to add most significant digit
    def confusingNumberII(self, N: int) -> int:
        self.res = 0
        convert = {0:0, 1:1, 9:6, 8:8, 6:9}
        def helper(num, rotate, factor):
            if num != rotate:
                # print("{}!={}".format(num, rotate))
                self.res += 1
            for d in convert:
                if num == 0 and d == 0:
                    continue
                if 10*num + d <= N:
                    # to generate next possible confusing number, add one more digit to original number
                    # to generate rotate for new original number, add corresponding convert digit as most significant digit, this is why we need the factor                  
                    helper(10*num+d, convert[d]*factor+rotate, factor*10)
        
        helper(0, 0, 1)
        return self.res