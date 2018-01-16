"""
Count the number of prime numbers less than a non-negative number, n.
"""
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# 1 is not a prime number
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        prime = [True for i in range(n)]
        i = 2
        while i**2 < n:
            if prime[i]:
                j = i**2
                while j < n:
                    prime[j] = False
                    j += i
            i += 1

        res = sum(1 for x in prime[2:] if x)
        # for i in range(2, n):
        #     if prime[i]:
        #         res += 1

        return res

obj = Solution()
print(obj.countPrimes(16))