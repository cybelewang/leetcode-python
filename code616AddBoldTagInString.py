"""
616 Add Bold Tag in String

Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:

Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>" 

Example 2:

Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c" 

Constraints:

The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
Note: This question is the same as 758: https://leetcode.com/problems/bold-words-in-string/
"""
class Solution:
    # Use intervals to save the start and end position of bold
    # when seeing a bold substring, check if it can extend last interval. If not, we append a new interval.
    # finally generate the string based on the intervals list
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        wordSet = set(dict)
        bold = []
        for start in range(len(s)):
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordSet:
                    if not bold or bold[-1][1] < start:
                        bold.append([start, end])
                    else:
                        bold[-1][1] = max(bold[-1][1], end)
        
        ans = []
        last_end = 0
        for start, end in bold:
            ans.append(s[last_end:start])
            ans.append('<b>'+s[start:end]+'</b>')
            last_end = end
        ans.append(s[last_end:])
        
        return ''.join(ans)