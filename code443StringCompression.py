"""

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:
Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
Example 2:
Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
Note:
All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
"""
from collections import Counter
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0

        i, j, count, last = 1, 1, 1, chars[0]
        for j in range(1, len(chars)):
            if chars[j] != last:
                if count > 1:
                    for digit in str(count):
                        chars[i] = digit
                        i += 1
                chars[i] = chars[j]
                i += 1  # bug fixed: fogot to advance i to the next available position after copying chars[j] to chars[i]
                last = chars[j]
                count = 1
            else:
                count += 1
        
        # don't forget the last repeating characters
        if count > 1:
            for digit in str(count):
                chars[i] = digit
                i += 1
        
        #print(chars[:i])
        return i

    # wrong solution, misunderstood the requirements (modify the array in place)
    def compress2(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        res, char_count = 0, Counter(chars)
        for c in char_count:
            count = char_count[c]            
            res += 1 + len(str(count))
            if count == 1: res -= 1 # remove the number if the count of letter is only 1
            
        return res

chars = ["a","a","b","b","c","c","c"]
obj = Solution()
print(obj.compress(chars))