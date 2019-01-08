"""
925 Long Pressed Name

Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.

Note:

name.length <= 1000
typed.length <= 1000
The characters of name and typed are lowercase letters.
"""
from itertools import zip_longest
class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        def G(s):
            # generator which yields a tuple with letter and its continuous count
            i = 0
            while i < len(s):
                cnt = 1
                while i +1 < len(s) and s[i] == s[i+1]:
                    i += 1
                    cnt += 1
                else:
                    yield (s[i], cnt)
                i += 1
        
        return all(a1==a2 and c1 <= c2 for ((a1, c1), (a2, c2)) in zip_longest(G(name), G(typed), fillvalue=(None, 0)))

test_cases = [('', ''), ('a', ''), ('', 'a'),('a', 'a'), ('aa', "aaa"), ('ab', 'aa'), ("alex", "aaleex"), ("saeed", "saaed")]        
for name, typed in test_cases:
    print(name, typed, sep = ' vs ', end = ': ')
    print(Solution().isLongPressedName(name, typed))

