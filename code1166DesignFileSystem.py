"""
1166 Design File System

You are asked to design a file system which provides two functions:

createPath(path, value): Creates a new path and associates a value to it if possible and returns True. Returns False if the path already exists or its parent path doesn't exist.
get(path): Returns the value associated with a path or returns -1 if the path doesn't exist.
The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

Implement the two functions.

Please refer to the examples for clarifications.

Example 1:

Input: 
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output: 
[null,true,1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1
Example 2:

Input: 
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output: 
[null,true,true,2,false,-1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.
 
Constraints:

The number of calls to the two functions is less than or equal to 10^4 in total.
2 <= path.length <= 100
1 <= value <= 10^9
NOTE: create method has been changed on August 29, 2019 to createPath. Please reset to default code definition to get new method signature.
"""
from collections import defaultdict
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = defaultdict(TrieNode)
        
class Trie:
    def __init__(self):
        self.root = TrieNode(-1)  
   
    def search(self, path):
        a = path.split('/')
        node = self.root
        for p in a[1:]:
            if p not in node.children: return None
            node = node.children[p]
        return node
        
class FileSystem_Trie:

    def __init__(self):
        self.trie = Trie()

    def createPath(self, path: str, value: int) -> bool:
        i = path.rfind('/')
        if i == -1: return False # invalid path
        prefix, sub = path[:i], path[i+1:]
        node = self.trie.search(prefix)
        # parent path doesn't exist, or path exists
        if not node or sub in node.children: return False        
        node.children[sub] = TrieNode(value)        
        return True

    def get(self, path: str) -> int:
        node = self.trie.search(path)
        return node.val if node else -1

# hashmap solution
class FileSystem_Map:

    def __init__(self):
        self.paths = {}

    def createPath(self, path: str, value: int) -> bool:
        i = path.rfind('/')
        prefix = path[:i]
        if path not in self.paths and (prefix == '' or prefix in self.paths):
            self.paths[path] = value
            return True
        else:
            return False

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)