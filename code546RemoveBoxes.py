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
# similar problems: Burst Ballons, Zuma Game, Strange Printer
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/6850657.html
    # dp[i][j][k] is the max points from i to j (inclusive) with k continuous same numbers (boxes[i]) on the left of i
    # the key is considering k, which is the count of boxes[i] on the left of i
    # knap sack approach: (1) remove current [i] (2) iterate range(i+1, j+1) and for each boxes[m]==boxes[i], remove [i:m]
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        def helper(boxes, i, j, k, dp):
            """
            return the max points in range i to j
            """
            if i > j:
                return 0

            if dp[i][j][k] > 0:
                return dp[i][j][k]

            res = (1+k)**2 + helper(boxes, i+1, j, 0, dp)   # points by removing (1+k) boxes[i]

            for m in range(i+1, j+1):
                if boxes[m] == boxes[i]:
                    res = max(res, helper(boxes, i+1, m-1, 0, dp) + helper(boxes, m, j, k+1, dp))   # points by merge boxes[i] and boxes[m], note k plus 1 because i was connected to m
            
            dp[i][j][k] = res

            return res

        # main
        n = len(boxes)
        dp = [[[0]*n for _ in range(n)] for _ in range(n)]

        return helper(boxes, 0, n-1, 0, dp)

    # my own solution 1, failed on scattered same values like test case [1, 1, 2, 1, 3, 1] where we need to remove 2 and 3 to make 1 continuous
    # 1. convert input to two lists, first list contains the numbers, and second list contains the continuous count of corresponding number. Now the example boxes become nums = [1, 3, 2, 3, 4, 3, 1] and c = [1, 1, 3, 1, 1, 1, 1]
    # 2. brutal force solution: iterate all nums, and for each number nums[i], we remove the continuous segment c[i], add c[i]*c[i] to previous points, remove nums[i] and c[i] from nums and count, update nums and c (merge same num's count), and recursively call the next routine
    # 3. improved brutal force solution: variables last_value, last_count, prev_points. Start from nums[0] for each nums[i], we have two choices: remove nums[i] or remove last_value, we add k*k for each choice, update last_value, last_count, prev_points and recursively call next subroutine.
    # 4. DP solution: dp[i][j] is the max points for nums[i:j] (including j), dp[i][j] = max(dp[i][j-1] + c[j]*c[j], dp[i][m-1] + (c[j]+c[m])**2 + dp[m+1][j-1]). The first candidate in max() is the result of removing nums[j], and the second candidate in max() is merging nums[j] with previous same number nums[m]
    def removeBoxes2(self, boxes):
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

    # combined solution 1 and 2, recursion, no DP, but this explains why we need a 3-D dp
    def removeBoxes3(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        def helper(nums, c, i, j, k):
            # k is the count of same nums[i] on the left of i
            # we need a dp[i][j][k]
            if j < i:
                return 0

            res = (k + c[i])**2 + helper(nums, c, i+1, j, 0)

            for m in range(i+1, j+1):
                if nums[m] == nums[i]:
                    res = max(res, helper(nums, c, i+1, m-1, 0) + helper(nums, c, m, j, k + c[i]))

            return res
                
        # main
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

        return helper(nums, c, 0, len(nums)-1, 0)

boxes = [1, 1, 2, 1, 3, 1]
print(Solution().removeBoxes3(boxes))