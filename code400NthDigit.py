"""
400 Nth Digit

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 2^31).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""
class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        length, count = 0, 0
        while count < n:
            length += 1
            count += 9*(10**(length-1))*length
            
        count -= 9*(10**(length-1))*length

        num = 10**(length - 1) + (n-count-1)//length
        return ord(str(num)[(n-count-1)%length]) - ord('0')

    # 2nd visit on 7/18/2020
    def findNthDigit2(self, n: int) -> int:
        # i is the final number's length
        i, pre = 1, 0
        while pre + i*9*10**(i-1) < n: # find the length of the final number, do not use "<=" because we don't want to increment the digit length if equal to n
            pre += i*9*10**(i-1)
            i += 1
        #print("length is {}".format(i))
        #print("pre is {}".format(pre))
        base = 10**(i-1) - 1 # starting number of current length i
        #print("base number is {}".format(base))
        diff = n - pre - 1 # -1 for module calculation
        number = base + 1 + diff//i # +1 because of module calculation
        #print("number {}".format(number))
        remain = diff%i
        return int(str(number)[remain])

obj = Solution()
print(obj.findNthDigit(3))