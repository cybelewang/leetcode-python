"""
Given a string with whitespaces and words, and page width, return the output formatted lines. The rule is:
(1) if at least one word can be put into a line, try to add as many words as possible in that line but don't put partial word
(2) if a single word is longer than page width, split the word and put partial word in the line

Corner cases:
(1) there may exist continuous whitespaces
(2) one word could span multiple lines
"""
def split(s):
    arr = []
    pre, start = ' ', 0
    for i, c in enumerate(s):
        #print(c)
        if c == ' ':
            if pre != ' ':
                arr.append(s[start:i])
            arr.append(' ')
        else:
            if pre == ' ':
                start = i
        pre = c
    if start < len(s):
        arr.append(s[start:])
    return arr

# split input string to a list of words and whitespaces, then use greedy method to take these words and whitespaces
def formatString(s, max_width):
    arr = split(s)
    res = []
    i, curLen, line = 0, 0, []
    while i < len(arr):
        word = arr[i]
        if curLen + len(word) <= max_width:
            line.append(word)
            curLen += len(word)
            i += 1
        else:
            # cannot fit word
            # case 1: there are already some words in this line
            if curLen > 0:
                res.append(''.join(line))
                curLen, line = 0, []
            # case 2: no word in this line
            else:
                curLen, line = max_width, [word[:max_width]]
                arr[i] = word[max_width:]
    # don't forget the last line
    if line:
        res.append(''.join(line))
    return res

s = "There is a river called missississippippippippi"
print(split(s))
print(formatString(s, 6))