"""
444 Sequence Reconstruction

Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:

Input: org = [1,2,3], seqs = [[1,2],[1,3]]
Output: false
Explanation: [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input: org = [1,2,3], seqs = [[1,2]]
Output: false
Explanation: The reconstructed sequence can only be [1,2].
Example 3:

Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Output: true
Explanation: The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:

Input: org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Output: true

Constraints:

1 <= n <= 10^4
org is a permutation of {1,2,...,n}.
1 <= segs[i].length <= 10^5
seqs[i][j] fits in a 32-bit signed integer.
 
UPDATE (2017/1/8):
The seqs parameter had been changed to a list of list of strings (instead of a 2d array of strings). Please reload the code definition to get the latest changes.
"""
# good for pitfall checking practice
# (1) seqs may contain numbers out of range [1, n]
# (2) seqs may contain less numbers than range [1, n], for example, seqs may contains single number lists
# (3) seqs may contain duplicate edges
class Solution:
    # Check sequence and make sure we have verified all edges in org
    # cnt represents the number of edges to verify, note a corner case is cnt == 0, in this case we need to verify seqs must contain that single node
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        n = len(org)
        pos, verified = defaultdict(int), [False]*(n+1)
        verified[0] = True
        for i, num in enumerate(org):
            pos[num] = i
        
        existed, cnt = False, n-1
        for seq in seqs:
            for i in range(len(seq)):
                existed = True
                if seq[i] < 0 or seq[i] > n:
                    return False
                if i == 0: continue
                if pos[seq[i-1]] >= pos[seq[i]]:
                    return False
                if not verified[seq[i-1]] and pos[seq[i-1]] + 1 == pos[seq[i]]:
                    verified[seq[i-1]] = True
                    cnt -= 1
        
        return cnt == 0 and existed

    # Topological sort, check if queue size > 1
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        n = len(org)
        indegrees = [0]*(n+1)
        graph = defaultdict(set)
        for seq in seqs:
            for i in range(len(seq)):
                if seq[i] < 1 or seq[i] > n: return False
                if i+1<len(seq) and (seq[i+1] < 1 or seq[i+1]>n): return False
                if i+1<len(seq) and seq[i+1] not in graph[seq[i]]: # bug fixed: must handle duplicates
                    graph[seq[i]].add(seq[i+1])
                    indegrees[seq[i+1]] += 1
                graph[seq[i]]
        if len(graph) != len(org):
            print("{} != {}".format(len(graph), len(org)))
            return False # size not equal
        res, q = [], deque()
        for i in graph:
            if indegrees[i] == 0:
                q.append(i)

        while q:
            if len(q) > 1: return False # multiple results exist
            src = q.popleft()
            res.append(src)
            for dst in graph[src]:
                indegrees[dst] -= 1
                if indegrees[dst] == 0:
                    q.append(dst)
        
        if any(indegrees): return False # cycle exists
        return res == org