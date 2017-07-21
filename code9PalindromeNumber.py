
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    nDigits = 0
    if x < 0:
        return False    # Make sure you asked the interviewer about negative integers
    y = x
    while y != 0:
        nDigits += 1
        y //= 10
    
    Lfactor = 10**(nDigits - 1)
    Rfactor = 1
    for i in range(nDigits//2):
        left = (x//Lfactor)%10  # x//10**(i)%10 is the ith digit from right, i starts from 0
        right = (x//Rfactor)%10
        if left != right:
            return False
        else:
            Lfactor //=10
            Rfactor *=10
    
    return True

test_case = [0, 3, 121, -121, 1234, 1234567654321]

for x in test_case:
    print(isPalindrome(x))