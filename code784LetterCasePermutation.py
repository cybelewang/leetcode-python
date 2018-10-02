"""
784 Letter Case Permutation

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  
Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length at most 12.
S will consist only of letters or digits.
"""
class Solution:
    # my own solution, typical DFS
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def helper(S, build, start, res):
            if start == len(S):
                res.append(''.join(build))
                return
            
            letters = set([S[start].lower(), S[start].upper()])
            for letter in letters:
                build.append(letter)
                helper(S, build, start + 1, res)
                build.pop()

        # main
        res = []
        helper(S, [], 0, res)

        return res

test_cases = ["", "12345", "a1B2", "ABAB"]
obj = Solution()
for S in test_cases:
    print(obj.letterCasePermutation(S))