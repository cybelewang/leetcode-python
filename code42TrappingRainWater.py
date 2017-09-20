"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""
# Two pointers solution, time O(n), space O(1)
def trap(height):
    i, j, plank, res = 0, len(height) - 1, 0, 0
    while i <= j:
        plank = max(plank, min(height[i], height[j]))

        if height[i] <= height[j]:
            res += plank - height[i]
            i += 1
        else:
            res += plank - height[j]
            j -= 1
    
    return res

# Stack solution, time O(n), space O(n)
def trap2(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left, result = [], 0
    for i in range(len(height)):
        if not left:
            left.append(i)
        else:
            base = 0
            while left and height[left[-1]] <= height[i]: # note: this while will stop at the most left element whose value <= height[i]
                j = left[-1]
                #base = height[j] # bug fixed: this will cause next statement's right side always be zero
                result += (height[j] - base)*(i - j - 1)
                left.pop()
                base = height[j]
            if left: # bug fixed: forgot the rain between i and left[-1]
                result += (height[i] - base)*(i - left[-1] - 1)
            left.append(i)

    return result

test_cases = [[], [0, 1, 2, 3], [4, 3, 2, 1], [0, 0, 1, 0, 0], [0,1,0,2,1,0,1,3,2,1,2,1], [1, 2, 3, 4, 5, 0 ,2, 1, 6]]  
for case in test_cases:
    print(case, end = ' -> ')
    print(trap(case))                                      