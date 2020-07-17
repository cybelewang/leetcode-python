"""
17 Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
# Recursive solution on 7/15/2020
def letterCombinations(digits):
    if len(digits) < 1: return []        
    digitstr = {
                "2":list("abc"), 
                "3":list("def"), 
                "4":list("ghi"), 
                "5":list("jkl"), 
                "6":list("mno"),
                "7":list("pqrs"),
                "8":list("tuv"),
                "9":list("wxyz")
                }
    result = []
    if len(digits) == 1:
        return digitstr[digits]
    
    for prefix in digitstr[digits[0]]:
        for suffix in letterCombinations(digits[1:]):
            result.append(prefix + suffix)
    
    return result

# 1st try iterative solution
def letterCombinations2(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    result = []

    if not digits.isdigit():
        return result

    digitstr = {"0":" ", 
                "1":"*", 
                "2":"abc", 
                "3":"def", 
                "4":"ghi", 
                "5":"jkl", 
                "6":"mno",
                "7":"pqrs",
                "8":"tuv",
                "9":"wxyz"
                }

    result = []
    for digit in digits:
        s = digitstr[digit] 
        if len(result) == 0:
            for c in s:
                result.append(c)
        else:
            n = len(result)
            for i in range(n): # bug fixed. Should not use "for e in result" because result will increase size in each for loop and this will never end
                e = result[i]
                for c in s:
                    result.append(e + c)
            result = result[n:]

    return result

test_case = ["23"]
for case in test_case:
    print(letterCombinations(case))
