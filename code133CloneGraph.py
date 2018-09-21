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
