"""
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

def letterCombinations(digits):
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

test_case = ["12", "23"]
for case in test_case:
    print(letterCombinations(case))
