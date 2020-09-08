"""
68 Text Justification

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
    # 8/30/2020
    # greedy approach to append each word
    # be careful when there is only 1 word in a line
    def fullJustify(self, words, maxWidth):
        start, curLength = 0, len(words[0]) + 1
        res = []
        for end in range(1, len(words)):
            if curLength + len(words[end]) > maxWidth:
                # format the words[start:end]
                spaces = maxWidth - curLength + (end - start) # number of spaces to allocate
                slots = end - start - 1 # number of slots to fill spaces
                s = '' # line string
                for i in range(start, end - 1):
                    used = spaces // slots + (1 if spaces % slots else 0)
                    s += words[i] + ' '*used
                    spaces -= used
                    slots -= 1
                s += words[end - 1]
                # for a line with single word, add spaces after the word
                if len(s) < maxWidth:
                    s = s + ' '*(maxWidth - len(s))
                res.append(s)
                
                # reset start and curLength
                start = end
                curLength = len(words[end]) + 1
            else:
                # increment curLength
                curLength += len(words[end]) + 1
        # handle last left-adjusted part
        s = ' '.join(words[start:])
        s = s + ' '*(maxWidth - len(s))
        res.append(s)
        return res

    # original verbose solution
    def fullJustify2(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []

        if words is None or len(words) < 1:
            return res

        width, start, count = len(words[0]), 0, 1
        for i in range(1, len(words)):
            word = words[i]
            if (width + len(word) + 1) <= maxWidth: # bug fixed: previously use width + len(word) + count
                # able to append this word
                width += len(word) + 1 # count the standard 1 white space
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

    def _tostr(self, words, start, count, width, maxWidth):
        line = ''
        if count == 1 or (start + count) == len(words):
            for i in range(count - 1):
                line += words[start + i]    # bug fixed: forget to add i
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

test_case = ["My","momma","always","said,","\"Life","was","like","a","box","of","chocolates.","You","never","know","what","you're","gonna","get."]
obj = Solution()
print(obj.fullJustify(test_case, 20))
        