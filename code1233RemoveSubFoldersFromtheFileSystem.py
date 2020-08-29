"""
1233 Remove Sub-Folders from the Filesystem

Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.

If a folder[i] is located within another folder[j], it is called a sub-folder of it.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

Example 1:

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
Example 2:

Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d/" will be removed because they are subfolders of "/a".
Example 3:

Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]

Constraints:
1 <= folder.length <= 4 * 10^4
2 <= folder[i].length <= 100
folder[i] contains only lowercase letters and '/'
folder[i] always starts with character '/'
Each folder name is unique.
"""
from collections import defaultdict, deque
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.index = -1 # the index of the string in folder list

class Solution:
    # Two-pass Trie solution
    # 1st pass put all folders into Trie
    # 2nd pass do a BFS to collect all folder's smallest prefix
    def removeSubfolders(self, folder):
        root = TrieNode()
        for i, f in enumerate(folder):
            node = root
            for sub in f.split('/')[1:]:
                node = node.children[sub]
            node.index = i
        
        q, res = deque([root]), []
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.index != -1:
                    res.append(folder[node.index])
                else:
                    q.extend(node.children.values())
                    
        return res

    # sort folder using default lexicological order, so folders with the same prefix must be grouped after sorting
    # then iterate folder, and check if current folder starts with the stack's top folder
    # time O(N*M*logN)
    def removeSubfolders2(self, folder):
        folder.sort()
        res = []
        for f in folder:
            if not res or not f.startswith(res[-1] + '/'): # must add '/' to avoid bug like '/a', '/ac'
                res.append(f)
        return res
    # sort folder by length, then check if each folder has prefix in result set
    # time O(N*logN + N*M^2)
    def removeSubfolders3(self, folder):
        folder.sort(key = lambda f: len(f))
        res = set()
        for f in folder:
            a = f.split('/')
            for i in range(2, len(a)+1):
                if '/'.join(a[:i]) in res:
                    break
            else:
                res.add(f)
        return list(res)

folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
print(Solution().removeSubfolders3(folder))
            