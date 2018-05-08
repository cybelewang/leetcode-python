"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), 
where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. 
Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""
class Solution:
    # 1. sort the input list with this rule: first compare height, people with bigger height on left, second, if the height is the same, people with smaller count on left
    # 2. for each people in the sorted list, insert the people into result list with the second count as insert index
    # succinct solution but with extra space
    # http://www.cnblogs.com/grandyang/p/5928417.html
    # Why this works? 
    # In the 2nd step, after sorting and then try to insert the ith people, we know that the height of ith people is the smallest (or the same height but with bigger count, we will analyze it later)
    # for simplicity, first we analyze the situation that height[i] < height[0:i]. We know that insert people[i] into positions 0-i will not affect any people[0:i] because height[i] is the smallest,
    # so we just insert people[i] to the correct position count[i]
    # Now we analyze the case when height[i] == height[i-1, i-2, ...], from the sorting rule, we know that people[i] will have bigger count[i] than previous people[i-1], people[i-2], ..., 
    # so using count[i] as insert position, people[i] is always inserted on right side of people[i-1], people[i-2], ... and counts people[i-1], people[i-2], ..., before it in res list.
    # for people already in res but having bigger heights, inserting people[i] to position count[i] will not affect their counts, so count[i] is the correct position for people[i]
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        print(people)
        res = []
        for p in people:
            res.insert(p[1], p)
            print(res)

        return res
    
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
obj = Solution()
print(obj.reconstructQueue(people))