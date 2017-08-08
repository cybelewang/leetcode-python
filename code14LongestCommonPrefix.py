"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Node:
    """
    Class Node
    """
    def __init__(self, value):
        self.char = value
        self.count = 1
        self.children = []

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    root = Node('')

    for s in strs:
        node = root
        for c in s:
            # each character
            bFound = False
            for child in node.children:
                if child.char == c:
                    bFound = True
                    child.count += 1
                    node = child
                    break
            if not bFound:
                newNode = Node(c)
                node.children.append(newNode)
                node = newNode
    
    result = ''
    maxCount = 0
    if (len(root.children) == 1):
        node = root.children[0]
        result += node.char
        maxCount = node.count

    while len(node.children) == 1:
        node = node.children[0]
        if node.count == maxCount:
            result += node.char
        else:
            break    
    
    return result

test_case = ['ab', 'acd']
print(longestCommonPrefix(test_case))