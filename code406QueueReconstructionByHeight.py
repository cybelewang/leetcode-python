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