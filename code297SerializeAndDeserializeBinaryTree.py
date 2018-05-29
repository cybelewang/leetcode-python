"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# similar to problem 449 Serialize and Deserialize BST
from TreeNode import *
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque()
        queue.append(root)
        s = []
        while len(queue) > 0:
            node = queue.popleft()
            if node is None:
                s.append('null')
            else:
                s.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        
        return ','.join(s)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def _getNextData(s, start):
            end = start
            while end < len(s) and s[end] != ',':
                end += 1            
            return s[start:end], end + 1

        root_data, start = _getNextData(data, 0)
        if root_data == 'null':
            return None
        
        root = TreeNode(int(root_data))
        queue = deque()
        queue.append(root)

        while start < len(data):
            # get parent node
            node = queue.popleft()
            # link left child
            str_data, start = _getNextData(data, start)
            if str_data != 'null':
                left_child = TreeNode(int(str_data))
                node.left = left_child
                queue.append(left_child)
            # link right child
            str_data, start = _getNextData(data, start)
            if str_data != 'null':
                right_child = TreeNode(int(str_data))
                node.right = right_child
                queue.append(right_child)

        return root


# Your Codec object will be instantiated and called as such:
root = ListToTree([1, 2, 3, None, None, 4, 5])
codec = Codec()
str_codec = codec.serialize(root)
print(str_codec)
recover = codec.deserialize(str_codec)
PrintTree(recover)