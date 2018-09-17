"""
6 ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    l = len(s)
    if numRows <= 1 or numRows >= l:
        return s
    else:
        edge = numRows - 1
        result = ""
        for i in range(numRows):
            j = i
            while j < l:
                result = result + s[j]
                j = j + 2*(edge - j%edge)
        return result

# 2nd round solution on 9/14/2018
def convert2(s, numRows):
    if numRows <= 1:
        return s
    rows = [[] for _ in range(numRows)]
    for i, c in enumerate(s):
        i %= 2*numRows - 2
        index = i if i < numRows else  2*numRows - 2 - i
        rows[index].append(c)
    
    return ''.join(sum(rows, []))

s = "ABCDEFGHIJKL"
r = convert2(s, 4)
print(r)