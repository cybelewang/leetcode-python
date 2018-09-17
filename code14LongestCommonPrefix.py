"""
14 Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
"""
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    result = ''
    if len(strs) == 0:
        return ''
    elif len(strs) == 1:
        return strs[0]
    else:
        for i in range(len(strs[0])):
            c = strs[0][i]
            bMatch = True
            for s in strs:
                if i >= len(s) or s[i] != c:
                    return result
            result += c          
    
    return result

# 2nd round solution on 9/16/2018 with bug fixed
def longestCommonPrefix2(strs):
    if not strs:
        return ''
    
    res = strs[0]
    for i in range(1, len(strs)):
        s = strs[i]
        j = 0
        while j < min(len(res), len(s)):
            if res[j] != s[j]:
                #res = res[:j]
                break
            else:
                j += 1
        res = res[:j]   # bug fixed here

    return res

test_case = ['ab', 'ac']
print(longestCommonPrefix2(test_case))