"""
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"

first round to find the fingerprint letter
zero    ->      eorz    ->  z(1)
two     ->      otw     ->  w(1)
four    ->      foru    ->  u(1)
six     ->      isx     ->  x(1)

second round to find the fingerprint letter
one     ->      eno     ->  o(2)
three   ->      ehrt    ->  r(2)
five    ->      efiv    ->  f(2)
seven   ->      ensv    ->  s(2)
eight   ->      eghit   ->  g(2)

third round to find the fingerprint letter
nine    ->      ein     ->  e(3)

"""
class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        digit_count = [0]*10
        letter_count = [0]*26
        base = ord('a')
        
        fp = [('z', 'zero', 0), ('w', 'two', 2), ('u', 'four', 4), ('x', 'six', 6), ('o', 'one', 1), ('r', 'three', 3), ('f', 'five', 5), ('s', 'seven', 7), ('g', 'eight', 8), ('e', 'nine', 9)]
        
        for c in s:
            letter_count[ord(c) - base] += 1
        
        for key, s, num in fp:
            digit_count[num] = letter_count[ord(key) - base]
            for c in s:
                letter_count[ord(c) - base] -= digit_count[num]

        return ''.join(map(str, sum([i]*digit_count[i] for i in range(10), [])))        

