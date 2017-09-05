"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""
def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    l1 = len(haystack)
    l2 = len(needle)
    for i in range(l1 - l2 + 1):  # bug fixed, see below
        if haystack[i, i + l2] == needle:
            return i
    
    return -1

# The end index of haystack is l1 - 1
# Assume the last index is x so haystack[x:x+l2] has the same length as l2
# l1 - 1 - x + 1 = l2
# x = l1 - l2
# Note that x is index. To get the full range from 0 to x, we use range(x + 1), which is range(l1 - l2 + 1)