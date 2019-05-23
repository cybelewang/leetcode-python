"""
332 Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
"""
# TO DO: a better algorithm in https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C++
# don't understand solutions in https://www.cnblogs.com/grandyang/p/5183210.html
# is there any duplicated travel. yes
# this problem requires to use all the tickets' iteinerary
# use DFS to find the itinerary and then return early
# better to use C++'s unordered_map<multiset<string>> to solve this problem. See C++'s solution
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(graph, need, res):
            if need == 0:
                return True
            src = res[-1]
            size = len(graph[src])  # because we modify the list, so we need to pre-calculate the number of loops
            for dst in range(size):
                dst = graph[src].pop(0)
                res.append(dst)
                if dfs(graph, need-1, res):
                    return True
                graph[src].append(dst)
                res.pop()
            
            return False

        # main
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        
        for src in graph:
            graph[src].sort()

        res = ["JFK"]
        dfs(graph, len(tickets), res) # if n = len(tickets), there are n + 1 nodes in res, and res already have 1

        return res

tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
obj = Solution()
print(obj.findItinerary(tickets))           
