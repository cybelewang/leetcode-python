
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