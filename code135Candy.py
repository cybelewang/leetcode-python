"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

"""
# ask what about the rule of equal rating?
class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n < 1:
            return 0

        candies = [1]*n

        for i in range(1, n):
            # left to right
            if ratings[i] > ratings[i-1]:
                candies[i] = max(candies[i], candies[i-1] + 1)
            elif ratings[i] == ratings[i-1]:
                candies[i] = max(candies[i], candies[i-1])
            # right to left
            j = n - 1 -i
            if ratings[j] > ratings[j+1]:
                candies[j] = max(candies[j], candies[j+1] + 1)
            elif ratings[j] == ratings[j+1]:
                candies[j] = max(candies[j], candies[j+1])
        
        #return reduce((lambda x, y: x+y), candies)
        res = 0
        for num in candies:
            res += num

        return candies
        #return res

obj = Solution()
test_case = [2, 2, 2, 1, 1, 1, 3, 3, 3]
print(obj.candy(test_case))