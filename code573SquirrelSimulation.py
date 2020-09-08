"""
573 Squirrel Simulation

There's a tree, a squirrel, and several nuts. Positions are represented by the cells in a 2D grid. Your goal is to find the minimal distance for the squirrel to collect all the nuts and put them under the tree one by one. The squirrel can only take at most one nut at one time and can move in four directions - up, down, left and right, to the adjacent cell. The distance is represented by the number of moves.
Example 1:

Input: 
Height : 5
Width : 7
Tree position : [2,2]
Squirrel : [4,4]
Nuts : [[3,0], [2,5]]
Output: 12
Explanation:
​​​​​
Note:

All given positions won't overlap.
The squirrel can take at most one nut at one time.
The given positions of nuts have no order.
Height and width are positive integers. 3 <= height * width <= 10,000.
The given positions contain at least one nut, only one tree and one squirrel.
"""
# Without squirrel, each nuts have fixed round-trip distance to the tree
# If squirrel picks up the first nut which has single distance d_t to the tree
# Then the first nut distance changes from 2*d_t to d_t + d_s, all other nuts distances will remain the same
# Therefore, if a nut has the max difference (d_t - d_s) among all nuts, it should be picked first
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        roundtrip = 0
        maxDiff = -2**31
        for x, y in nuts:
            d = abs(x - tree[0]) + abs(y - tree[1]) # single distance to tree
            roundtrip += 2*d # round trip distance to tree
            d_s = abs(x - squirrel[0]) + abs(y - squirrel[1]) # distance to squirrel
            maxDiff = max(maxDiff, d - d_s) # update max difference
            
        return roundtrip - maxDiff
            