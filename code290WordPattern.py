"""
290 Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""
# use bimap, not a single direction map
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        i, j = 0, 0
        map1, map2 = {}, {}
        for p in pattern:
            if j >= len(str):# bug fixed: need to consider the length mismatch case
                return False

            while j < len(str) and str[j] != ' ':
                j += 1
            s = str[i:j]
            # check the bimap singularity
            if p in map1 and s in map2:
                if map1[p] != s or map2[s] != p:
                    return False
            elif p not in map1 and s not in map2:
                map1[p] = s
                map2[s] = p
            else:
                return False
            
            i = j + 1
            j = i
        
        return i >= len(str)

# 2nd round solution on 10/5/2018
class Solution2:
    def wordPattern(self, pattern, str):
        map = {}
        a = str.split()
        if len(pattern) != len(a):
            return False

        for i, p in enumerate(pattern):
            if p in map:
                if map[p] != a[i]:
                    return False
            else:
                map[p] = a[i]
        
        return True

obj = Solution()
p, s = 'he', 'unit'
print(obj.wordPattern(p, s))