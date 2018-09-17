"""
28 Implement strStr

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""
class Solution:
    # KMP
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # corner case 1: len(needle) > len(haystack)
        if len(needle) > len(haystack):
            return -1

        # corner case 2: needle is ''
        if needle == '':
            return 0
        
        def computeLPS(pat):
            """
            Compute the longest prefix which is also suffix for each substring pat[0:i-1] with length i
            """
            length = 0 # length of previous longest prefix suffix
            i, M = 1, len(pat)
            lps = [0]*M # longest prefix suffix length for substring pat[0 to i], index i is the end index of the substring pat[0 to i]

            while i < M:
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length > 0:  # This is the tricky part, see example 'AAACAAAA' and i = 7.
                        length = lps[length-1]
                    else:
                        lps[i] = 0
                        i += 1

            return lps
        
        lps = computeLPS(needle)
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                if j == len(needle):    # for this problem (return the first occurance)
                    return i - j
                # To print all occurances, using the below codes
                # print('Found pattern at index ' + str(i - j))
                # j = lps[j - 1]    # don't forget to reset the index j
            else:
                # The basic idea is to keep i unchanged while reset j to corresponding index
                if j == 0:  # txt[i] doesn't match pat[0], so we need to advance i
                    i += 1
                else:
                    j = lps[j-1]
            
        return -1
        

    # Brutal force solution
    def strStr2(self, haystack, needle):
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

txt = 'aa'
pat = 'a'
obj = Solution()
print(obj.strStr(txt, pat))
