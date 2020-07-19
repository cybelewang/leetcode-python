"""
281 Zigzag Iterator

Given two 1d vectors, implement an iterator to return their elements alternately.
 
Example:
Input:
v1 = [1,2]
v2 = [3,4,5,6] 
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
 
Follow up:
What if you are given k 1d vectors? How well can your code be extended to such cases?
Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:
Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].
"""
class ZigzagIterator:
    def __init__(self, v1, v2):
        self.data = [v1, v2]
        self.row = 0
        self.col = [0, 0]
        self.seek()

    def next(self):
        val = self.data[self.row][self.col[self.row]]
        self.col[self.row] += 1
        self.row = (self.row + 1)%2
        self.seek()
        return val

    def hasNext(self):
        return self.col[0] < len(self.data[0]) or self.col[1] < len(self.data[1])
    
    def seek(self):
        for _ in range(2):
            if self.col[self.row] < len(self.data[self.row]): break
            self.row = (self.row + 1)%2


v1 = [1,2]
v2 = [3,4,5,6]
i, v = ZigzagIterator(v1, v2), []
while i.hasNext(): v.append(i.next())

print(v)
