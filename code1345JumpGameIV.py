"""
1345 Jump Game IV

Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
Example 4:

Input: arr = [6,1,9]
Output: 2
Example 5:

Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3
 
Constraints:

1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8
"""
from collections import deque, defaultdict
class Solution:
    # BFS with trimming trick
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        pos = defaultdict(list)
        for i, num in enumerate(arr):
            pos[num].append(i)
        
        q, steps = deque([0]), 0
        seen = [False]*n
        seen[0] = True
        while q:
            size = len(q)
            for _ in range(size):
                i = q.popleft()
                if i == n-1:
                    return steps
                # jump to i+1
                if i+1 < n and not seen[i+1]:
                    q.append(i+1)
                    seen[i+1] = True
                # jump to i-1
                if i-1 > -1 and not seen[i-1]:
                    q.append(i-1)
                    seen[i-1] = True
                # jump to j where arr[i] == arr[j]
                for j in pos[arr[i]]:
                    if not seen[j]:
                        q.append(j)
                        seen[j] = True
                # below line fixes TLE
                pos[arr[i]].clear() # trick: we don't need to visit these indices again
            steps += 1
        
        return -1