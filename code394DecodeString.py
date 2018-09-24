"""
394 Decode String

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""
class Solution:
    # OJ's best
    def decodeString(self, s):
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString
    # my solution
    def decodeString2(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, num = [''], 0
        for c in s:
            if c.isdigit():
                num = num*10 + ord(c) - ord('0')
            elif c == '[':
                stack.append(num)
                stack.append('')
                num = 0
            elif c == ']':
                sub = stack.pop()
                count = stack.pop()
                stack[-1] += sub*count
                num = 0
            else:
                stack[-1] += c
                num = 0
        
        return stack[-1]

obj = Solution()
test_cases = ['', 'abcde', '3[a]2[bc]', '3[a2[c]]', '2[abc]3[cd]ef']
for case in test_cases:
    print(obj.decodeString(case))