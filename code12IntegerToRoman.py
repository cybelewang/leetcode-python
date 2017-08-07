"""
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
"""
def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    numsLetters = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I') ]
    result = ''
    i = 0

    while num > 0:
        (x, l) = numsLetters[i]
        if num < x:
            i += 1
        else:
            result += l
            num -= x

    return result


test_cases = list(range(1, 101))
test_cases.extend([200, 300, 400, 500, 600, 700, 800, 900, 999, 1000])

for num in test_cases:
    print(str(num) + ' -> ' + intToRoman(num))