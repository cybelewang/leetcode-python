"""
8 String to Integer (atoi)

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""
def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    l = len(str)
    i, j = 0, 0
    # skip the leading white spaces
    while i < l:
        if str[i] == ' ':
            i += 1
        else:
            break
    # all white spaces
    if i == l:
        return 0
    # parse the sign
    # there may be multiple signs, like "+--"
    Is_Negative = False
    if str[i] == "-":
        Is_Negative = True
        i += 1
    elif str[i] == "+":
        Is_Negative = False
        i += 1
    elif str[i] >= "0" and str[i] <= "9":
        Is_Negative = False
    else:
        return 0    

    MAX_POSITIVE_INTEGER = 2**31 - 1;
    MAX_NEGATIVE_INTEGER = 2**31;
    result = 0
    # next parse the numbers
    while i < l:
        if str[i] >= '0' and str[i] <= '9':
            result = result * 10 + ord(str[i]) - ord('0');
            if Is_Negative and result > MAX_NEGATIVE_INTEGER:
                return -MAX_NEGATIVE_INTEGER # exceed the 32-bit negative integer limit, return the most negative integer
            elif not Is_Negative and result > MAX_POSITIVE_INTEGER:
                return MAX_POSITIVE_INTEGER # exceed the 32-bit positive integer limit,return the most positive integer
            else:
                i += 1
        else:
            break;
    
    if Is_Negative:
        result *= -1
    
    return result


test_case = ["", "abc", "+0", "-0", "-12 34", "-0012" ,"123","2147483648","2147483647","-2147483648", "+-2"]
for s in test_case:
    print(myAtoi(s))