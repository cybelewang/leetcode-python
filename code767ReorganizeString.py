"""
767 Reorganize String

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""
# 
from collections import Counter
class Solution:
    # https://leetcode.com/problems/reorganize-string/solution/
    def reorganizeString(self, S):
        N = len(S)
        A = []
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if c > (N+1)//2: return ""
            A.extend(c * x)
        print(A)
        ans = [None] * N
        ans[::2], ans[1::2] = A[N//2:], A[:N//2]
        return "".join(ans)
    # my own greedy solution by sorting the letters of by their count
    # then inserting the biggest count letters into the proper position
    def reorganizeString_WRONG(self, S):
        """
        :type S: str
        :rtype: str
        """
        count, n = Counter(S), len(S)        
        letters = sorted(count.keys(), key= lambda x: count[x]) # sort the list of letters in ascending count order
     
        i, j, res = 0, 1, ['']*n
        while letters:
            c = letters.pop()
            for _ in range(count[c]):
                if i < n:
                    res[i] = c
                    i += 2
                else:
                    #print("empty returned")
                    return ""

            # bug fixed: no need for the below commented code because we just take the smaller index of odd and even
            # if i-1 < n and res[i-1] == "":  # bug fixed: should check res[i-1] before decreasing i to make sure res[i-1] is empty
            #     i -= 1  # reset i to the next insert position for a different letter
            if i > j:   # always set i to the smaller of (i, j) so always insert a letter to i
                i, j = j, i
        
        return ''.join(res)

S = "tndsewnllhrtwsvxenkscbivijfqnysamckzoyfnapuotmdexzkkrpmppttficzerdndssuveompqkemtbwbodrhwsfpbmkafpwyedpcowruntvymxtyyejqtajkcjakghtdwmuygecjncxzcxezgecrxonnszmqmecgvqqkdagvaaucewelchsmebikscciegzoiamovdojrmmwgbxeygibxxltemfgpogjkhobmhwquizuwvhfaiavsxhiknysdghcawcrphaykyashchyomklvghkyabxatmrkmrfsppfhgrwywtlxebgzmevefcqquvhvgounldxkdzndwybxhtycmlybhaaqvodntsvfhwcuhvuccwcsxelafyzushjhfyklvghpfvknprfouevsxmcuhiiiewcluehpmzrjzffnrptwbuhnyahrbzqvirvmffbxvrmynfcnupnukayjghpusewdwrbkhvjnveuiionefmnfxao"
print(Solution().reorganizeString(S))