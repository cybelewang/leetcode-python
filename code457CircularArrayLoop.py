"""
You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. 
Conversely, if it's negative (-n), move backward n steps. 
Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. 
Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. 
The loop must be "forward" or "backward'.

Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.

Example 2: Given the array [-1, 2], there is no loop.

Note: The given array is guaranteed to contain no element "0".

Can you do it in O(n) time complexity and O(1) space complexity?

"""
# understand this problem correctly
# 1. The loop must be "forward" or "backward'. This means it must loop on one direction. FOr example, [1, -1] is not valid
# 2. A loop starts and ends at a particular index with more than 1 element along the loop. For example, [-1, 2], where 2 goes to 2, and the start index = end index. This is invalid.
# 3. the initial position is not necessarily the zeroth element. [3, 1, 2] is a loop because 1->2->1
class Solution(object):
    # OJ sample solution, O(1) space
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            start = i
            if nums[i] == 0:
                continue
            positive = nums[start] > 0
            if nums[start] % len(nums) == 0:
                continue
            i_next = (i+nums[start]) % len(nums)
            while nums[i_next] % len(nums) != 0:
                if positive != (nums[i_next] > 0):
                    break
                if i_next == start:
                    return True
                tmp = nums[i_next]
                nums[i_next] = 0
                i_next = (i_next+tmp)%len(nums)
        return False
    # https://www.cnblogs.com/grandyang/p/7658128.html
    def circularArrayLoop2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        mem, visited = {}, [False]*n
        for i in range(n):
            if visited[i]: continue
            cur = i
            while True:
                visited[cur] = True
                next = (cur + nums[cur] + n) % n
                if next == cur or nums[next]*nums[cur] < 0: break
                if next in mem: return True
                mem[cur] = next
                cur = next
                
        return False
        
#nums = [2, 2, -1, 2]
nums = [3, 1, 2]
obj = Solution()
print(obj.circularArrayLoop(nums))