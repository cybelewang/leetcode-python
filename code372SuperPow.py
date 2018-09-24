"""
372 Super Pow

Your task is to calculate a^b mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024
"""
class Solution:
    # OJ best solution
    # https://leetcode.com/problems/super-pow/discuss/84466/Math-solusion-based-on-Euler's-theorem-power-called-only-ONCE-C++Java1-line-Python
    def superPow(self, a, b):
        result = 1
        fermatb = (int(''.join(map(str, b)))) % 570
        while fermatb:
            if fermatb & 1:
                result = (result * a) % 1337
            a = (a * a) % 1337
            fermatb >>= 1
        return result

    # https://leetcode.com/problems/super-pow/discuss/84472/C++-Clean-and-Short-Solution
    # ab % k = (a%k)(b%k)%k
    # a^1234567 % k = (a^1234560 % k)*(a^7 % k) % k = (a^123456 % k)^10 % k * (a^7 % k) % k
    # f(a, 1234567) = f(f(a, 123456), 10)*f(a, 7) % k
    def superPow2(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if a == 1:
            return 1

        res = 1
        if b:
            last = b.pop()
            res = self.powmod(self.superPow2(a, b), 10) * self.powmod(a, last) % self.base
        
        return res


    def __init__(self):
        self.base = 1337

    def powmod(self, a, c):
        """
        a^c % k, where 0 <= c <= 10 
        """
        a %= self.base
        res = 1

        for _ in range(c):
            res = (res * a) % self.base
        
        return res
    
print(Solution().superPow2(2, [1, 0]))        