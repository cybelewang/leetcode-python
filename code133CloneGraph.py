"""
133 Clone Graph

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use '#' as a separator for each node, and ',' as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

"""
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

# Use a map to save connection between origin node and copy node
# if the neighbor has already been processed, it must be in connection. In this case, do not put it in the next_queue to avoid dead loop
# if the ngighbor is not in the map, then the node has not been copied. In this case, copy the node and put the node in the next_queue to further process its neighbors
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None

        queue = [node]
        res = UndirectedGraphNode(node.label)
        connection = {node:res} # map with key = original node, value = copied node

        # BFS
        while len(queue) > 0:
            next_queue = []
            # iterate current level nodes
            for origin in queue:
                copy = connection[origin]   # get corresponding copy node as "parent"
                for neighbor in origin.neighbors:   # iterate original children list of original node in current level
                    if neighbor in connection:
                        copy.neighbors.append(connection[neighbor]) # already been copied, do not put it in the next level queue
                    else:
                        new_node = UndirectedGraphNode(neighbor.label)  # create a new copy node
                        copy.neighbors.append(new_node) # establish neighbor linking
                        connection[neighbor] = new_node # establish connection
                        next_queue.append(neighbor) # put the node into next level queue to further process its children
            
            queue = next_queue
        
        return res

# Follow-up: clone directed graph, may have duplicate node values, may have cycles
# 0 -> 0 -> 2
#     /\    |
#      |    \/
#      9 <- 3
#     /\
#      |
# 5 -> 7 -> 8
# given heads which is a list contains starting nodes (0 and 5), clone this graph.
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

class CloneDG:
    def clone(self, heads):
        """
        clone a directed graph with multiple given input nodes, may contain duplicate values, may contain cycles
        """
        # DFS function used in this problem 133 Clone Graph
        def helper(src, mem):
            if not src: return None
            if src in mem:
                return mem[src]
            dst = mem.setdefault(src, Node(src.val))
            for nei in src.children:
                dst.children.append(helper(nei, mem))
            return dst
            
        mem, res = {}, []
        for head in heads:
            res.append(helper(head, mem))
        return res

# construct the test DG
heads = [Node(0), Node(5)]

node01 = Node(0)
heads[0].children.append(node01)
node02 = Node(2)
node01.children.append(node02)
node12 = Node(3)
node02.children.append(node12)
node11 = Node(9)
node12.children.append(node11)
node11.children.append(node01)

node21 = Node(7)
heads[1].children.append(node21)
node21.children.append(node11)
node22 = Node(8)
node21.children.append(node22)

clones = CloneDG().clone(heads)
print(clones[0].val == heads[0].val)
print(clones[1].val == heads[1].val)