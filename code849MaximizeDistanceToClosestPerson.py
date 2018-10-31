"""
849 Maximize Distance to Closest Person

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
"""
# similar problems: 475 Heaters
class Solution:
    # OJ O(1) space solution
    def maxDistToClosest_OJ(self, seats):
        people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)

        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))

        return ans
    # my own solution, two-pass, O(n) space
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        a = [n]*n

        res, src = 0, -1
        for i in range(n):
            if seats[i]:
                src = i
                a[i] = 0
            elif src != -1:
                a[i] = i - src

        src = n
        for i in range(n-1, -1, -1):
            if seats[i]:
                src = i                
            elif src != n:
                a[i] = min(a[i], src - i)
            
            res = max(res, a[i])
        
        return res

seats = [1, 0, 1, 0]
print(Solution().maxDistToClosest_OJ(seats))