"""
11 Container with Most Water

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""
# similar problems: 42 Trapping Rain Water

# two pointer solution, because container with boarder i and j can have min(h[i], h[j])*(j-i)
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    i, j = 0, len(height) - 1
    maxArea = 0
    while i < j:
        if height[i] < height[j]:
            area = height[i] * (j - i)
            i += 1
        else:
            area = height[j] * (j - i)
            j -= 1
        maxArea = max(maxArea, area)
    
    return maxArea

test_cases = [[1, 1], [1, 2,  3, 4], [4, 3, 2, 1], [1, 2, 3, 3, 2, 1]]

for arrays in test_cases:
    print(maxArea(arrays))