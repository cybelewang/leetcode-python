"""
685 Redundant Connection II

In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3
Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
"""
class Solution:
    # three cases: two indegrees only, cycle only, two indegrees and cycle
    # the third case is complex. See below analysis in code.
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def find(parent, i):
            """
            find the "root" node which is connected to i
            """
            while parent[i] != i:
                i = parent[i]

            return parent[i]

        # main
        N = len(edges)
        parent = [0]*(N+1)
        A, B = [], []
        
        # step 1, check whether there is a node with two parents
        for i in range(N):
            u, v = edges[i]
            if parent[v] == 0:
                parent[v] = u
            else:
                A, B = [parent[v], v], [u, v]   # remove either A or B can fix the two-parent-node problem, we need to further check cycle existence to determine which one to remove
                edges[i][1] = 0 # invalid the second edge
        
        # step 2, union find
        parent = list(range(N+1))
        for u, v in edges:
            if v == 0:  # pass invalid edges
                continue

            pu = find(parent, u)
            if pu == v: # a cycle exists
                # if A is not empty, this means there were two parents for A[1]: A[0], B[0]
                # although we have made B invalid, there is still a cycle, so we need to remove A to solve two problems: 2 parent nodes and cycle
                # if A is empty, this means there is only cycle, so we need to remove current edge
                return A or [u, v]
            
            parent[v] = pu
        
        # tree is valid after invalidating B, so B is the result
        return B

    # WRONG SOLUTION!
    # my own solution using problem 684's method
    # two conditions: (1) in-degree of the node is 2; (2) there is a loop
    def findRedundantDirectedConnection2(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def find(root, i):
            """
            find the "root" node which is connected to i
            """
            while root[i] != -1:
                i = root[i]

            return i

        # main
        N = len(edges)
        root = [-1]*(N+1)
        indegree = [0]*(N+1)

        for u, v in edges:
            indegree[v] += 1
            if indegree[v] == 2:
                return [u, v]
            
            x, y = find(root, u), find(root, v)
            if x == y:
                return [u, v]

            root[y] = x

        return []


edges = [[2,1],[3,1],[4,2],[1,4]]   # expected [2, 1]
print(Solution().findRedundantDirectedConnection(edges))

"""
This problem is very similar to "Redundant Connection". But the description on the parent/child relationships is much better clarified.

There are two cases for the tree structure to be invalid.
1) A node having two parents;
   including corner case: e.g. [[4,2],[1,5],[5,2],[5,3],[2,4]]
2) A circle exists
If we can remove exactly 1 edge to achieve the tree structure, a single node can have at most two parents. So my solution works in two steps.

1) Check whether there is a node having two parents. 
    If so, store them as candidates A and B, and set the second edge invalid. 
2) Perform normal union find. 
    If the tree is now valid 
           simply return candidate B
    else if candidates not existing 
           we find a circle, return current edge; 
    else 
           remove candidate A instead of B.
If you like this solution, please help upvote so more people can see.

class Solution {
public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> parent(n+1, 0), candA, candB;
        // step 1, check whether there is a node with two parents
        for (auto &edge:edges) {
            if (parent[edge[1]] == 0)
                parent[edge[1]] = edge[0]; 
            else {
                candA = {parent[edge[1]], edge[1]};
                candB = edge;
                edge[1] = 0;
            }
        } 
        // step 2, union find
        for (int i = 1; i <= n; i++) parent[i] = i;
        for (auto &edge:edges) {
            if (edge[1] == 0) continue;
            int u = edge[0], v = edge[1], pu = root(parent, u);
            // Now every node only has 1 parent, so root of v is implicitly v
            if (pu == v) {
                if (candA.empty()) return edge;
                return candA;
            }
            parent[v] = pu;
        }
        return candB;
    }
private:
    int root(vector<int>& parent, int k) {
        if (parent[k] != k) 
            parent[k] = root(parent, parent[k]);
        return parent[k];
    }
};
Java version by MichaelLeo

class Solution {
    public int[] findRedundantDirectedConnection(int[][] edges) {
        int[] can1 = {-1, -1};
        int[] can2 = {-1, -1};
        int[] parent = new int[edges.length + 1];
        for (int i = 0; i < edges.length; i++) {
            if (parent[edges[i][1]] == 0) {
                parent[edges[i][1]] = edges[i][0];
            } else {
                can2 = new int[] {edges[i][0], edges[i][1]};
                can1 = new int[] {parent[edges[i][1]], edges[i][1]};
                edges[i][1] = 0;
            }
        }
        for (int i = 0; i < edges.length; i++) {
            parent[i] = i;
        }
        for (int i = 0; i < edges.length; i++) {
            if (edges[i][1] == 0) {
                continue;
            }
            int child = edges[i][1], father = edges[i][0];
            if (root(parent, father) == child) {
                if (can1[0] == -1) {
                    return edges[i];
                }
                return can1;
            }
            parent[child] = father;
        }
        return can2;
    }
    
    int root(int[] parent, int i) {
        while (i != parent[i]) {
            parent[i] = parent[parent[i]];
            i = parent[i];
        }   
        return i;
    }
}

"""