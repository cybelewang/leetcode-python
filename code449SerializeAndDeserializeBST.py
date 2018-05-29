"""

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# similar to problem 297 Serialize and Deserialize Binary Tree (BFS solution)
# use DFS to solve this problem
from TreeNode import *
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def _dfs(root, encode):
            if not root:
                encode.append('X')
            else:
                encode.append(str(root.val))
                _dfs(root.left, encode)
                _dfs(root.right, encode)

        encode = []
        _dfs(root, encode)
        return ','.join(encode)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def _dfs(encode, start):
            if start < len(encode):
                value = encode[start]
                if value == 'X':
                    return (None, start + 1)
                else:
                    root = TreeNode(int(value))
                    left, index = _dfs(encode, start + 1)
                    right, index = _dfs(encode, index)
                    root.left, root.right = left, right
                    return (root, index)
            else:
                return (None, start)

        encode = data.split(',')
        root, end = _dfs(encode, 0)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

root = ListToTree([1, 2, 3, None, None, 4, 5])
PrintTree(root)
codec = Codec()
str_codec = codec.serialize(root)
print(str_codec)
recover = codec.deserialize(str_codec)
PrintTree(recover)