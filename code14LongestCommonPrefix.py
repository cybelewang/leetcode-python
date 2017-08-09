"""
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

test_case = ['ab', 'ac']
print(longestCommonPrefix(test_case))