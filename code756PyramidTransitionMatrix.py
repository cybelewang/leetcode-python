"""
756 Pyramid Transition Matrix

We are stacking blocks to form a pyramid. Each block has a color which is a one letter string, like `'Z'`.

For every block of color `C` we place not in the bottom row, we are placing it on top of a left block of color `A` and right block of color `B`. 
We are allowed to place the block there only if `(A, B, C)` is an allowed triple.

We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. 
Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:
Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  D   E
 / \ / \
X   Y   Z

This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.
Example 2:
Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
Note:
bottom will be a string with length in range [2, 8].
allowed will have length in range [0, 200].
Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.
"""
from collections import defaultdict
class Solution:
    # OJ solution https://leetcode.com/articles/pyramid-transition-matrix/
    def pyramidTransition_OJ(self, bottom, allowed):
        T = defaultdict(set)
        for u, v, w in allowed:
            T[u, v].add(w)

        #Comments can be used to cache intermediate results
        #seen = set()
        def solve(A):
            if len(A) == 1: return True
            #if A in seen: return False
            #seen.add(A)
            return any(solve(cand) for cand in build(A, []))

        def build(A, ans, i = 0):
            if i + 1 == len(A):
                yield "".join(ans)
            else:
                for w in T[A[i], A[i+1]]:
                    ans.append(w)
                    for result in build(A, ans, i+1):
                        yield result
                    ans.pop()

        return solve(bottom)
    # help from http://www.cnblogs.com/grandyang/p/8476646.html
    # the key is the prototype of the recursive function pyramid(self, cur, above, mydict), where we must use two strings: current (or bottom) and above, where above is building
    # originally I thought using a single string recursive function such as pyramid(self, bottom, mydict) and it is hard
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        mydict = defaultdict(list)
        for s in allowed:
            mydict[s[:2]].append(s[-1])
        
        return self.pyramid(bottom, "", mydict)
    
    def pyramid(self, cur, above, mydict):
        """
        cur: current bottom string
        above: above string, starting from empty string
        """
        if len(cur) == 2 and len(above) == 1:
            return True
        elif len(cur) == len(above) + 1:
            return self.pyramid(above, "", mydict)
        
        pos = len(above)
        base = cur[pos:pos+2]
        for s in mydict[base]:
            if self.pyramid(cur, above + s, mydict):
                return True
        
        return False
        
bottom = "XXYX"
allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
print(Solution().pyramidTransition_OJ(bottom, allowed))