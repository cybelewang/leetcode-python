"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""
class Solution:
    def _dfs(self, s, start, remain, build, res):
        if remain == 0:
            res.append('.'.join(build))
            return
        minLen = max(1, len(s) - start - (remain - 1)*3)
        maxLen = min(3, len(s) - start - (remain - 1))
        for i in range(minLen, maxLen + 1):
            substr = s[start:start+i]
            if (i > 1 and substr[0] == '0') or int(substr) > 255:   # bug fixed here: original condition was (i > 1 and int(substr) ==0) or int(substr) > 255
                continue
            else:
                build.append(substr)
                self._dfs(s, start+i, remain-1, build, res)
                build.pop()

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n < 4 or n > 12:
            return []

        res, build = [], []
        self._dfs(s, 0, 4, build, res)

        return res

obj = Solution()
test_cases = ['','0000','00000','010010', '25525511135']
for case in test_cases:
    print(case, end = ' -> ')
    print(obj.restoreIpAddresses(case))