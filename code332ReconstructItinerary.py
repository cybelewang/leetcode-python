"""
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
# is there any duplicated travel?
# this problem requires to use all the tickets' iteinerary
from heapq import heapify, heappush, heappop
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        dep_dst = {}    # departure -> destination
        for t in tickets:
            if t[0] in dep_dst:
                heappush(dep_dst[t[0]], t[1])
            else:
                dst = [t[1]]
                #heapify(dst)
                dep_dst[t[0]] = dst

        res = ["JFK"]
        while res[-1] in dep_dst and len(dep_dst[res[-1]]) > 0:
            dst = heappop(dep_dst[res[-1]])
            res.append(dst)

        return res

tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
obj = Solution()
print(obj.findItinerary(tickets))           
