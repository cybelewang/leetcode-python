"""
1361 Validate Binary Tree Nodes

You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

 

Example 1:



Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:



Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:



Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
Example 4:



Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false
 

Constraints:

1 <= n <= 10^4
leftChild.length == rightChild.length == n
-1 <= leftChild[i], rightChild[i] <= n - 1
"""
class Solution:
    # problem says the nodes will form exactly one binary tree
    # (1) All nodes indegrees should <= 1
    # (2) There should be a root (indegree == 0), and only one root
    # (3) The root subtree should have all nodes, no missing node
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        # all nodes shoud not have more than 1 in degrees
        indegrees = [0]*n
        root = -1
        for i in range(n):
            left = leftChild[i]
            if left != -1:
                indegrees[left] += 1
                if indegrees[left] > 1:
                    return False
                
            right = rightChild[i]
            if right != -1:
                indegrees[right] += 1
                if indegrees[right] > 1:
                    return False
        
        # find the root with indegree == 0
        # if no root or multiple roots exist, return False
        for i in range(n):
            if indegrees[i] == 0:
                if root == -1:
                    root = i
                else:
                    return False
                
        if root == -1:
            return False
        
        # start from root, check node count == n
        def count(node):
            if node == -1:
                return 0
            return 1 + count(leftChild[node]) + count(rightChild[node])
        
        return count(root) == n

n =4
left =[1,-1,3,-1]
right = [2,3,-1,-1]
print(Solution().validateBinaryTreeNodes(n, left, right))