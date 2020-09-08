"""
387 First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

"""
class Solution:
    # bit solution, use 2 bits for each character
    # 0b00 - not present
    # 0b01 - present once
    # 0b11 - present more than once
    def firstUniqChar(self, s: str) -> int:
        encode = 0
        for c in s:
            mask = 0b11 << 2*(ord(c) - ord('a'))
            if (encode & mask):
                # c already exists
                encode |= mask # set the two bits to 0b11
            else:
                # c doesn't exist, set the two bits to 0b01
                encode |= 0b01 << 2*(ord(c) - ord('a'))
        #print(bin(encode))
        for i, c in enumerate(s):
            shift = 2*(ord(c) - ord('a'))
            mask = 0b11 << shift
            unique = 0b01 << shift
            if (encode & mask) == unique:
                return i
        return -1
        
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count, base = [0]*26, ord('a')
        for c in s:
            count[ord(c)-base] += 1
        
        for i, c in enumerate(s):
            if count[ord(c)-base] == 1:
                return i
        
        return -1

# alternative solution in C++, one pass
# use a LRUCache-like data strucutre, a dict maps character to a doubly-linked list node
# when a new character is seen, append it to the tail of linked list
# when an existing character is seen, remove it from linked list, and set map value to NULL
# the result will be the begin node in the linked list

test_cases = ['leetcode', 'loveleetcode']
for case in test_cases:
    print(Solution().firstUniqChar(case))