"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""
# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

# Ask what about many points having the same coordinates?
# Leetcode says one point's result is 1, :<
# Leetcode says two same points count 2, :<
class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0

        n = len(points)
        if n == 1:
            return 1

        my_dict = {}    # key - the (k, -1, b) of the line, value - a hash set of the points in this line
        count_dict = {} # key - (x, y), value: count of the same points
        res = 0
        for i in range(n):
            p1 = points[i]
            xy = (p1.x, p1.y)
            if xy in count_dict:
                count_dict[xy] += 1
            else:
                count_dict[xy] = 1
            res = max(res, count_dict[xy])
            for j in range(i+1, n):
                p2 = points[j]
                if p1.x == p2.x and p1.y == p2.y:
                    continue
                elif p1.x == p2.x:
                    abc = (1, 0, -p1.x)
                else:
                    k = int((p2.y - p1.y)*1000/(p2.x - p1.x))   # precision issue
                    b = p1.y - k*p1.x
                    abc = (k, -1, b)

                if abc in my_dict:
                    record = my_dict[abc]
                else:
                    record = set()
                    my_dict[abc] = record

                record.add(p1)
                record.add(p2)
                res = max(res, len(record))

        return res

test_case = [[560,248],[0,16],[30,250],[950,187],[630,277],[950,187],[-212,-268],[-287,-222],[53,37],[-280,-100],[-1,-14],[-5,4],[-35,-387],[-95,11],[-70,-13],[-700,-274],[-95,11],[-2,-33],[3,62],[-4,-47],[106,98],[-7,-65],[-8,-71],[-8,-147],[5,5],[-5,-90],[-420,-158],[-420,-158],[-350,-129],[-475,-53],[-4,-47],[-380,-37],[0,-24],[35,299],[-8,-71],[-2,-6],[8,25],[6,13],[-106,-146],[53,37],[-7,-128],[-5,-1],[-318,-390],[-15,-191],[-665,-85],[318,342],[7,138],[-570,-69],[-9,-4],[0,-9],[1,-7],[-51,23],[4,1],[-7,5],[-280,-100],[700,306],[0,-23],[-7,-4],[-246,-184],[350,161],[-424,-512],[35,299],[0,-24],[-140,-42],[-760,-101],[-9,-9],[140,74],[-285,-21],[-350,-129],[-6,9],[-630,-245],[700,306],[1,-17],[0,16],[-70,-13],[1,24],[-328,-260],[-34,26],[7,-5],[-371,-451],[-570,-69],[0,27],[-7,-65],[-9,-166],[-475,-53],[-68,20],[210,103],[700,306],[7,-6],[-3,-52],[-106,-146],[560,248],[10,6],[6,119],[0,2],[-41,6],[7,19],[30,250]]
points = []
for t in test_case:
    points.append(Point(t[0],t[1]))
obj = Solution()
print(obj.maxPoints(points))