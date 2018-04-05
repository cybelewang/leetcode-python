"""
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false
"""
# stack solution
# push all values as False into stack, when the value is '#', we check if the last second is True, 
# if so, we will pop last three to remove both left and right children, then append True
class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # '' valid or not?
        if len(preorder) < 1:
            return False

        stack = []
        for s in preorder.split(','):
            stack.append(False)
            if s == '#':
                # remove pairing left branch
                while len(stack) > 2 and stack[-2]:
                    stack.pop()
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(True)

        return stack == [False, True]

preorder = "9,#,#,1"
obj = Solution()
print(obj.isValidSerialization(preorder))