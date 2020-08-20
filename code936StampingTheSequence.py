"""
936 Stamping The Sequence

You want to form a target string of lowercase letters.

At the beginning, your sequence is target.length '?' marks.  You also have a stamp of lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.  You can make up to 10 * target.length turns.

For example, if the initial sequence is "?????", and your stamp is "abc",  then you may make "abc??", "?abc?", "??abc" in the first turn.  (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.  If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2], corresponding to the moves "?????" -> "abc??" -> "ababc".

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length moves.  Any answers specifying more than this number of moves will not be accepted.

Example 1:

Input: stamp = "abc", target = "ababc"
Output: [0,2]
([1,0,2] would also be accepted as an answer, as well as some other answers.)
Example 2:

Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]

Note:

1 <= stamp.length <= target.length <= 1000
stamp and target only contain lowercase letters.
"""
class Solution:
    # https://leetcode.com/problems/stamping-the-sequence/discuss/189254/Python-Greedy-and-DFS
    def movesToStamp(self, stamp, target):
        n, m, s, t, res = len(target), len(stamp), list(stamp), list(target), []
        def check(i):
            # search target[i:i+m] and if all match (ignore '?') and target[i:i+m] are not all '?', change target[i:i+m] to '?' and push i to result list
            changed = False
            for j in range(m):
                if t[i+j] == '?': continue
                if t[i+j] != s[j]: return False
                changed = True
            if changed:            
                t[i:i+m] = ['?']*m
                res.append(i)
            return changed
        
        changed = True
        while changed:
            changed = False
            for i in range(n-m+1):
                changed |= check(i)

        return res[::-1] if t == ['?']*n else []

    # my own solution
    # general idea is to reverse the sequence, start from the target, then convert it to ?????
    # (1) search all occurances of stamp in target
    # (2) start from one of the occurance, and try to expand left and right until whole target is generated. When expanding, ignore those already recovered.
    # (3) the bug here is that if there are multiple stamp occurances in target, they should be recovered all at once instead one by one
    # This is because some can only expand left, some can only expand right, if we combine them, they cannot be recovered from just recovering one occurance initially.
    # Example is stamp = "aq", target = "aqqaaq", "aqq" can only be recovered by expanding right, and "aaq" can only be recovered by expanding left, so if we initially recover "aq????" or "????aq", we cannot expand to whole target
    # The correct way is to initially recover target to "aq??aq", then we can expand to whole target 
    def movesToStamp_WRONG(self, stamp, target):
        start, init = 0, []
        # find all occurances of stamp in target and put their intervals into init list
        while start < len(target):
            f = target.find(stamp, start)
            if f == -1:
                break
            init.append([f, f + len(stamp)-1]) # [start, end] inclusive
            start = f + len(stamp)
        
        res = []
        # expand the covered range to whole target
        def expand(target, stamp, s, e, build):
            m, n = len(stamp), len(target)
            if s == 0 and e == n - 1:
                res.append(build[::-1])
                return
            if s > 0:
                # expand left
                for k in range(m, 0, -1):                
                    if s - k >= 0 and target[s-k:s] == stamp[:k]:
                        s = s - k
                        build.append(s)
                        break
                else:
                    return
            
            if e < n - 1:
                # expand right
                for k in range(m, 0, -1):                
                    if e + k < n and target[e+1:e+k+1] == stamp[m-k:]:
                        e = e + k
                        build.append(e-m+1)
                        break
                else:
                    return
            
            expand(target, stamp, s, e, build)
        
        for s, e in init:
            expand(target, stamp, s, e, [s])
            if len(res) > 0:
                return res[0]
        
        return res

stamp = "aq"
target = "aqqaaq"
print(Solution().movesToStamp(stamp, target))