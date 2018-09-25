"""
739 Daily Temperatures

Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. 
If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""
class Solution:
    # my own stack solution, O(n) space, O(n) time
    # use a stack to track descending temperatures' indices, when iterating to a new temperate, we first pop out all temperatures' indices that are lower than current temperature, update their days in the result list
    # then push back current index into stack
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        days, stack = [0]*n, []

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                days[j] = i - j

            stack.append(i)

        return days

#temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
temperatures = [100, 99, 98, 97, 96]
print(Solution().dailyTemperatures(temperatures))