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
    # OJ's best solution https://leetcode.com/problems/binary-watch/discuss/88458/Simple-Python+Java
    def readBinaryWatch(self, num):
        return ['%d:%02d' % (h, m)
                for h in range(12) for m in range(60)
                if (bin(h) + bin(m)).count('1') == num]

    # pitfall : avoid 12:00 and 0:60
    def readBinaryWatch2(self, num):
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
                if cur//64 < 12 and cur%64 < 60:    # bug fixed here: forgot to add this condition because it may generate 12:00 for num==2, and 0:60 for num == 4
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

"""
Input:
2
Output:
["12:00","10:00","6:00","9:00","5:00","3:00","8:32","4:32","2:32","1:32","8:16","4:16","2:16","1:16","0:48","8:08","4:08","2:08","1:08","0:40","0:24","8:04","4:04","2:04","1:04","0:36","0:20","0:12","8:02","4:02","2:02","1:02","0:34","0:18","0:10","0:06","8:01","4:01","2:01","1:01","0:33","0:17","0:09","0:05","0:03"]
Expected:
["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"]
"""