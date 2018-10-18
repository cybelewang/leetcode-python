"""
825 Friends Of Appropriate Ages

Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:

Input: [20,30,100,110,120]
Output: 
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
 

Notes:

1 <= ages.length <= 20000.
1 <= ages[i] <= 120.
"""
from bisect import bisect_left
from collections import defaultdict
class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ages.sort()
        res, count = 0, defaultdict(int)

        for i, age in enumerate(ages):
            count[age] += 1

            lower = (age ^ 1)//2 + 8    # lower age limit for B
            start = bisect_left(ages, lower)
            res += i - start    # excludes A self
        
        # bug fixed: need to handle repeated ages, for example, ages = [16, 16], the above algorithm only handles the request from right to left
        # if there are n same age in ages, then the above algorithm only calculates n*(n-1)//2, and the other n*(n-1)//2 needs to be accounted below
        for age in count:
            lower = (age^1)//2 + 8
            if lower <= age:
                res += (count[age] - 1)*(count[age])//2

        return res
        

#ages = [16, 16]    # expected 2
#ages = [16, 17, 18]    # expected 2
#ages = [20,30,100,110,120]  # expected 3
ages = [108,115,5,24,82]    # expected 3
print(Solution().numFriendRequests(ages))