"""
13 Roman to Integer

Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
"""
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    RomanNums = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
    i, result = 0, 0
    while i < len(s):
        if (i+2) <= len(s) and s[i:i+2] in RomanNums:
            result += RomanNums[s[i:i+2]]
            i += 2
        elif s[i:i+1] in RomanNums:
            result += RomanNums[s[i:i+1]]
            i += 1
        else:
            i += 1
    
    return result
            
test_cases = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XIX", "XXXIII", "XXXIV", "XXXVIII", "LXVIII", "LXIX", "XCVIII", "C", "MD", "MDCCC", "CM"]
for s in test_cases:
    print(s + " -> " + str(romanToInt(s)))