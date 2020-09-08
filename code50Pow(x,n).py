"""
50 Pow(x, n)

Implement pow(x, n).

"""
# Iterative solution, time O(logn), space O(1)
# Decompose n to binary, and on each bit 1 (kth position), times the corresponding x^(2^k)
# For example, n = 45 = 32 + 8 + 4 + 1, so ans = x^32 * x^8 * x^4 * x^1
# we can calculate x = x^2 to update the factor
def myPow(self, x, n):
    if n < 0: return 1.0 / self.myPow(x, -n)
    ans, cur = 1, x
    while n > 0:
        if n % 2:
            ans = ans * cur
        cur = cur * cur
        n //= 2
    
    return ans
# Recursive solution, time O(logn), space O(logn)
# n can be negative
def myPow2(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n < 0:
        return 1.0/myPow2(x, -n)
    
    def helper(x, n):
        if n == 0: return 1.0
        half = helper(x, n//2)
        if n%2 == 0:
            return half*half
        else:
            return half*half*x
        
    return helper(x, n)

test_cases = [(1.0, 10), (2.0, 10), (0.0, 200)]
for case in test_cases:
    print(str(case[0])+'^'+str(case[1]), end = ' = ')
    print(myPow2(case[0], case[1]))
