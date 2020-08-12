"""
Given a number and k, find the min number after removing k digits
Example: input num = 4132219, k = 3, output: 1219
follow-up: what if asking for max number?
"""
def minNumberAfterRemovingKDigits(num, k):
    def helper(s, k):
        res = ''
        i, minVal = 0, '99' # change minVal to '' for follow-up
        for j in range(k+1):
            if s[j] < minVal:
                i = j
                minVal = s[j]
        if i == k:
            res = s[i:]
        else:
            res = s[i] + helper(s[i+1:], k-i)

        return res

    # can min number start from 0? I think it's OK
    s = str(num)
    if k >= len(s):
        return 0
    return int(helper(s, k))

print(minNumberAfterRemovingKDigits(4132219, 3))