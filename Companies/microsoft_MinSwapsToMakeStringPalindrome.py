"""
Given a string, what is the minimum number of adjacent swaps required to convert a string into a palindrome. If not possible, return -1.
Practice online: https://www.codechef.com/problems/ENCD12

Similar problem on geeks - without adjacent restriction
https://www.geeksforgeeks.org/count-minimum-swap-to-make-string-palindrome/
"""
from collections import Counter

# solution from https://leetcode.com/discuss/interview-question/351783/
def adj_swaps_to_palindrome(s):
    s = list(s)
    if not is_palindrome_permutation(s):
        return -1

    i, j = 0, len(s) - 1
    swap_count = 0

    while i < j:
        k = j

        while i < k and s[i] != s[k]:
            k -= 1
        
        while k < j:
            if s[k + 1] == s[i]:
                # already matched, no need to check
                break
            s[k], s[k + 1] = s[k + 1], s[k]
            swap_count += 1
            k += 1

        i += 1
        j -= 1

    return swap_count


def is_palindrome_permutation(s):
    res = 0
    for v in Counter(s).values():
        res += (v % 2)
        if res > 1:
            return False
    return True


print(adj_swaps_to_palindrome('ACCCC'))