"""
https://www.geeksforgeeks.org/number-buildings-facing-sun/
"""
class Solution:
    def countBuildings(self, arr):
        maxH = -2**31
        count = 0
        for i in range(len(arr)):
            if arr[i] > maxH:
                maxH = arr[i]
                count += 1
        
        return count

arr = [7, 4, 8, 2, 9] # expect 3
print(Solution().countBuildings(arr))