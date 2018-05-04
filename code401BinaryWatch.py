"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
"""
class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def dfs(cur, i, used, res):
            """
            cur: current number
            i: the bit index from 0 to 9
            used: number of bits set to 1            
            """
            if used == num:
                res.append(self.getTime(cur))
                return
            if num - used < 10 - i: # check if OK to set this bit as 0
                dfs(cur, i+1, used, res)
            dfs(cur|(1<<i), i+1, used+1, res)
        
        res = []
        if num < 11:
            dfs(0, 0, 0, res)
        
        return res

    def getTime(self, num):
        """
        converts number to clock time
        lower 6 bits for minutes
        higher 4 bits for hours
        """
        return str(num//64)+':'+('0' if num%64 < 10 else '')+str(num%64)

obj = Solution()
print(obj.readBinaryWatch(1))