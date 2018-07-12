"""
Given several boxes with different colors represented by different positive numbers. 
You may experience several rounds to remove boxes until there is no box left. 
Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1), 
remove them and get k*k points.
Find the maximum points you can get.

Example 1:
Input:

[1, 3, 2, 2, 2, 3, 4, 3, 1]
Output:
23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)
Note: The number of boxes n would not exceed 100.

"""
class Solution:
    # my own solution
    # 1. convert input to two lists, first list contains the numbers, and second list contains the continuous count of corresponding number. Now the example boxes become nums = [1, 3, 2, 3, 4, 3, 1] and c = [1, 1, 3, 1, 1, 1, 1]
    # 2. brutal force solution: iterate all nums, and for each number nums[i], we remove the continuous segment c[i], add c[i]*c[i] to previous points, remove nums[i] and c[i] from nums and count, update nums and c (merge same num's count), and recursively call the next routine
    # 3. improved brutal force solution: variables last_value, last_count, prev_points. Start from nums[0] for each nums[i], we have two choices: remove nums[i] or remove last_value, we add k*k for each choice, update last_value, last_count, prev_points and recursively call next subroutine.
    # 4. DP solution: dp[i][j] is the max points for nums[i:j] (including j), dp[i][j] = max(dp[i][j-1] + c[j]*c[j], dp[i][m-1] + (c[j]+c[m])**2 + dp[m+1][j-1]). The first candidate in max() is the result of removing nums[j], and the second candidate in max() is merging nums[j] with previous same number nums[m]
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        if not boxes:
            return 0

        # convert boxes to a nums list (nums) and count list (c)
        nums, c, prev = [], [], -1
        for box in boxes:
            if box != prev:
                prev = box  # bug fixed: forgot to update prev
                nums.append(box)
                c.append(1)
            else:
                c[-1] += 1

        # create a list (p) to quickly look for the index of the previous same number in nums
        mem, p = {}, []
        for i, num in enumerate(nums):
            if num in mem:
                p.append(mem[num])
            else:
                p.append(-1)            
            mem[num] = i

        n = len(nums)
        dp = [[0]*n for _ in range(n)]  # dp[i][j] is the max point from nums[i] to nums[j] (inclusive)
        for i in range(n-1, -1, -1):
            dp[i][i] = c[i]**2
            for j in range(i+1, n):
                point1 = dp[i][j-1] + c[j]**2
                m = p[j]
                if m < i:
                    # no same number found in nums[i:j]
                    dp[i][j] = point1
                else:
                    # same number found in nums[i:j], we should consider the case of merging these two numbers
                    point2 = 0 if m == 0 else dp[i][m-1]
                    point2 += (c[m] + c[j])**2 + dp[m+1][j-1]
                    dp[i][j] = max(point1, point2)
        
        return dp[0][n-1]

boxes = [1, 1, 2, 1, 3, 1]
print(Solution().removeBoxes(boxes))