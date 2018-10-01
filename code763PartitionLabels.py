"""
763 Partition Labels

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, 
and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""
# similar problems: 45 Jump Game II; 758 Bold Words in String
class Solution:
    # my own improved solution by extending end first, then check if current index equals to end (if so, add the length to res).
    def partitionLabels(self, S):
        right = {c:i for i, c in enumerate(S)}    # most right index of a letter

        res, start, end = [], 0, -1
        for i, c in enumerate(S):
            end = max(end, right[c])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        
        return res
    # my own first trial solution with bugs fixed
    # try to extend the end index of current partition
    def partitionLabels2(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        right = {}    # most right index of a letter
        for i, c in enumerate(S):
            right[c] = i
        
        res, start, end = [], 0, -1
        for i, c in enumerate(S):
            if i > end:
                len_ = end - start + 1
                if len_ > 0:
                    res.append(len_)
                start = i
            end = max(end, right[c])
        
        # don't forget the last partition
        res.append(len(S) - start)

        return res

ss = ["a", "abc", "ababcbacadefegdehijhklij"]
obj = Solution()
for S in ss:
    print(obj.partitionLabels2(S))