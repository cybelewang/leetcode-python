"""
917 Reverse Only Letters

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "
"""
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        a, j = [], len(S)-1
        for i in range(len(S)):
            if S[i].isalpha():
                while not S[j].isalpha():
                    j -= 1
                a.append(S[j])
                j -= 1
            else:
                a.append(S[i])
        
        return ''.join(a)

#S = "Test1ng-Leet=code-Q!"
S = "aaaaa---------------------------"
print(Solution().reverseOnlyLetters(S))
