"""
TreeNode class definition using binary tree module
https://github.com/joowani/binarytree
"""
from binarytree import Node, customize, tree, show

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

def ListToTree(lt):
    """
    Convert a list to a binary tree, using leetcode style list
    :type lt: list[int, or None]
    :rtype: TreeNode
    """
    if not lt:
        return None
    
    root = TreeNode(lt[0])
    parents = [root]    # parents for the next level

    i = 1   # i is index of next available element to become a TreeNode
    while i < len(lt):
        n = len(parents)
        for parent in parents:  # No "None" in the parents array, so we don't need to check if parent is None
            # Create the left child
            if i < len(lt) and lt[i] is not None:
                leftChild = TreeNode(lt[i])
                parent.left = leftChild
                parents.append(leftChild)
            i += 1

            # Create the right child
            if i < len(lt) and lt[i] is not None:
                rightChild = TreeNode(lt[i])
                parent.right = rightChild
                parents.append(rightChild)
            i += 1
        # Keep newly created children in the parents list for the next level
        parents = parents[n:]
    
    return root

def TreeToList(root):
    """
    Convert a tree to a leetcode style list
    :type root: TreeNode
    :rtype: list[int, or None]
    """


def ConvertToNode(treeNode):
    """
    Convert a "TreeNode" type tree to a "Node" type tree to use "Node" type methods
    :type treeNode: TreeNode
    :rtype: No
    """
    node = Node(treeNode.val)
    if treeNode.left is not None:
        node.left = ConvertToNode(treeNode.left)
    if treeNode.right is not None:
        node.right = ConvertToNode(treeNode.right)
    
    return node
    
def PrintTree(root):
    """
    Pretty print of a binary tree
    :type root: TreeNode
    :rtype: No
    """
    if not root or not isinstance(root, TreeNode):
        return

    show(ConvertToNode(root))

''' test_root = TreeNode(1)
test_root.left = TreeNode(2)
test_root.right = TreeNode(3)
PrintTree(test_root) '''

"""
null = None
test_tree = [7,5,4,1,2,6,null,null,null,null,3]
root = ListToTree(test_tree)
PrintTree(root)
"""