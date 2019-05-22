"""
331 Verify Preorder Serialization of a Binary Tree

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
class Solution:
    # similar to validating parentheses
    # if using a stack, we push numbers to stack, when seeing a '#', then each '#' will pop its parent if '#' is left child, or one ancestor if '#' is right child. In summary, a '#' pops a number.
    # so we don't need a stack, we can use a counter to track the unmatched '#' and numbers
    def isValidSerialization(self, preorder):
        A = preorder.split(',')
        cnt = 0
        for i in range(len(A)-1):
            if A[i] == '#':
                if cnt == 0:    return False
                cnt -= 1
            else:
                cnt += 1
        
        return cnt == 0 and A[-1] == '#'

    # stack solution
    # push all values as False into stack, when the value is '#', we check if the last second is True, 
    # if so, we will pop last three to remove both left and right children, then append True
    def isValidSerialization2(self, preorder):
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


"""
Some used stack. Some used the depth of a stack. Here I use a different perspective. In a binary tree, if we consider null as leaves, then

all non-null node provides 2 outdegree and 1 indegree (2 children and 1 parent), except root
all null node provides 0 outdegree and 1 indegree (0 child and 1 parent).
Suppose we try to build this tree. During building, we record the difference between out degree and in degree diff = outdegree - indegree. When the next node comes, we then decrease diff by 1, because the node provides an in degree. If the node is not null, we increase diff by 2, because it provides two out degrees. If a serialization is correct, diff should never be negative and diff will be zero when finished.

public boolean isValidSerialization(String preorder) {
    String[] nodes = preorder.split(",");
    int diff = 1;
    for (String node: nodes) {
        if (--diff < 0) return false;
        if (!node.equals("#")) diff += 2;
    }
    return diff == 0;
}
"""