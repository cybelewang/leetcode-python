
def myAtoi(self, str):
    """
    :type str: str
    :rtype: int
    """
    l = len(str)
    i, j = 0, 0
    # skip the leading white spaces
    while i < l:
        if str[i] == ' ':
            i = i + 1
        else:
            break
    # all white spaces
    if i == l:
        return 0
    # parse the sign
    # there may be multiple signs, like "+--"
    Is_Negative = False
    while i < l:
        if str[i] == '+':
            i = i + 1
        elif str[i] == '-':
            Is_Negative = not Is_Negative
            i = i + 1
        else:
            break;
    # next parse the numbers
