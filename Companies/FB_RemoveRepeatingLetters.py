"""
https://www.1point3acres.com/bbs/thread-648579-1-1.html
Remove repeating letters and keep only different letters
Example 1
s = "abbba", output is "" because "bbb" will be removed first, then "aa" will be removed.
Example 2
s = "abbbc", output is "ac"
"""
import unittest
def removeRepeatingLetters(s):
    stack, repeat = [], False
    for letter in s:
        if not stack:
            stack.append(letter)
            repeat = False
        else:
            if letter == stack[-1]:
                # same character, skip this letter and set repeat to True
                repeat = True
            else:
                # letter != stack[-1], this is a different character
                if repeat: # if last letter in stack is repeated, we remove it
                    stack.pop()
                # if this letter is the same as stack top letter, we just mark repeat as True and skip this letter
                # bug fixed: must check if stack is empty
                if stack and letter == stack[-1]:
                    repeat = True
                else:
                    stack.append(letter)
                    repeat = False
    # don't forget the stack top letter
    if repeat:
        stack.pop()

    return ''.join(stack)

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(removeRepeatingLetters(""), "")
        self.assertEqual(removeRepeatingLetters("aaaaaaa"), "")
        self.assertEqual(removeRepeatingLetters("abcdba"), "abcdba")
        self.assertEqual(removeRepeatingLetters("abbbc"), "ac")
        self.assertEqual(removeRepeatingLetters("abcddcba"), "")
        self.assertEqual(removeRepeatingLetters("abbbbbaba"), "ba")
        self.assertEqual(removeRepeatingLetters("abcdefghiihgfedcbaxxx"), "")

unittest.main(exit = False)