"""
241 Different Ways to Add Parentheses

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]

Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""
# use binary tree to solve this problem, see problem 95, unique binary tree II
# treat the two numbers inside a parenthesis as left leaf and right leaf, and put the result into their root
# then the root will serve as either "left subtree" or "right subtree" in the upper level parenthesis
class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = []
        for (i, c) in enumerate(input):
            if c in ('+', '-', '*'):
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        if c == '+':
                            res.append(l + r)
                        elif c == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        
        if len(res) < 1:
            res.append(int(input))

        return res

input = "2*3-4*5"
obj = Solution()
print(obj.diffWaysToCompute(input))
