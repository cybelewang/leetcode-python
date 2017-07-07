

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

s = "ABCDEFGHIJKL"
r = convert(s, 4)
print(r)