"""
A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3
"""
from collections import deque
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        def encode(s):
            """
            encode input string to a 16-bit integer
            A: 0b00
            C: 0b01
            G: 0b10
            T: 0b11
            """
            res = 0
            for c in s:
                res <<= 2
                if c == 'C':
                    res += 1
                elif c == 'G':
                    res += 2
                elif c == 'T':
                    res += 3
            
            return res
        
        valid = set()
        for s in bank:
            valid.add(encode(s))
        
        s, e = encode(start), encode(end)
        #valid.add(e)   # ask if we need to add end to bank?
        
        # BFS
        q, visited, level = deque(), set(), 0
        q.append(s)
        visited.add(s)
        while q:
            l = len(q)
            for i in range(l):
                current = q.popleft()
                if current == e:
                    return level
                # iterate all possible mutations
                for shift in range(8):
                    mask = 0xFFFF - (0b11<<(2*shift))   # mask to reset the two bits to 0
                    base = current & mask
                    for offset in range(4): # iterate A C G T
                        num = base + (offset << (2*shift))
                        if num not in visited and num in valid:
                            visited.add(num)
                            q.append(num)

            level += 1

        return -1

obj = Solution()
start="AACCGGTT"
end = "AACCGGTA"
bank = []
print(obj.minMutation(start, end, bank))