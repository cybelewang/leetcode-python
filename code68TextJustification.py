"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.
"""
class Solution(object):
    def _tostr(self, words, start, count, width, maxWidth):
        line = ''
        if count == 1 or (start + count) == len(words):
            for i in range(count - 1):
                line += words[start]
                line += ' '
            line += words[start + count - 1]

            for i in range(maxWidth - width):
                line += ' '
        else:
            extraWhiteSpaces = maxWidth - width # number of white spaces to distribute
            extraWhiteSpacesPerSlot = extraWhiteSpaces//(count - 1) # average number of white spaces besides the normal 1 white space
            largeSlots = extraWhiteSpaces - extraWhiteSpacesPerSlot * (count - 1)   # number of slots with 1 more extra white spaces than others
            for i in range(count - 1):
                line += words[start + i]
                if i < largeSlots:
                    for j in range(2 + extraWhiteSpacesPerSlot):
                        line += ' '
                else:
                    for j in range(1 + extraWhiteSpacesPerSlot):
                        line += ' '

            line += words[start + count - 1]

        return line               

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []

        if not words or len(words) < 1:
            return res

        width, start, count = 0, 0, 0
        for (i, word) in enumerate(words):
            if (width + len(word) + count) <= maxWidth:
                # able to append this word
                width += len(word)
                if count > 0:   # bug fixed: should not count the white space if only one word in the line
                    width += 1  # count the standard 1 white space
                count += 1 # number of words in this line increases
            else:
                # cannot append this word, must generate the line string and append to result
                res.append(self._tostr(words, start, count, width, maxWidth))
                
                # reset parameters
                start = i
                count = 1
                width = len(word)

        # append the last line string        
        res.append(self._tostr(words, start, count, width, maxWidth))

        return res

test_case = ["This", "is", "an", "example", "of", "text", "justification."]
obj = Solution()
print(obj.fullJustify(test_case, 21))
        