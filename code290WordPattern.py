"""
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
# corner cases: does '' match ''? ' ' match ' '? 
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        i, j = 0, 0
        my_dict = {}
        for p in pattern:
            while j < len(str) and str[j] != ' ':
                j += 1
            s = str[i:j]
            if p in my_dict:
                if my_dict[p] != s:
                    return False
            else:
                my_dict[p] = s
            
            i = j + 1
            j = i
        
        return i >= len(str)

obj = Solution()
p, s = 'abba', 'dog cat cat dog '
print(obj.wordPattern(p, s))