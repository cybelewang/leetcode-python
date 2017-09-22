"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """     
    zero = ord('0')
    m, n = len(num1), len(num2)
    result = [0]*(m + n) # key: must allocate the list to avoid check list length

    for i in range(m):
        for j in range(n):
            product = (ord(num1[m - 1 - i]) - zero) * (ord(num2[n - 1 - j]) - zero)
            k = i + j
            s = product + result[k]
            carry = s // 10
            result[k] = s % 10
            while carry > 0: # bug fixed: forgot to handle the situation that sum may > 9 after adding
                k += 1
                s = carry + result[k]
                result[k] = s % 10
                carry = s // 10            
    
    while result and result[-1] == 0:
        result.pop()

    result.reverse()

    return ''.join(map(str, result))

test_cases = [('',''), ('1','2'), ('12345','6789'), ('9999','999999')]
for case in test_cases:
    print(case[0], end = ' * ')
    print(case[1], end = ' = ')
    print(multiply(case[0], case[1]))