"""
49 Group Anagrams

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
"""
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    result = []
    my_dict = {}

    for s in strs:
        ordered = ''.join(sorted(s))
        if ordered in my_dict:
            result[my_dict[ordered]].append(s)
        else:
            index = len(result)
            result.append([s])
            my_dict[ordered] = index
    
    return result

test_case = ['a','b','ab','ba','ab']
print(groupAnagrams(test_case))