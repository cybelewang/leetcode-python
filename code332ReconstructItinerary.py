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
# TO DO: a better algorithm in https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C++


# is there any duplicated travel. yes
# this problem requires to use all the tickets' iteinerary
# use DFS to find the itinerary and then return early
from bisect import insort
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def _dfs(dep_dst, need, res):
            if need == 0:
                return True

            start = res[-1]
            if start in dep_dst and len(dep_dst[start]) > 0:
                for dst in dep_dst[start]:
                    res.append(dst)
                    dep_dst[start].remove(dst)
                    if _dfs(dep_dst, need-1, res):
                        return True
                    else:                        
                        insort(dep_dst[start], res.pop())

            return False                       

        dep_dst = {}    # departure -> destination
        for _from, _to in tickets:
            if _from in dep_dst:
                insort(dep_dst[_from], _to)
            else:
                dep_dst[_from] = [_to]

        res = ["JFK"]
        _dfs(dep_dst, len(tickets), res)

        return res

tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
obj = Solution()
print(obj.findItinerary(tickets))           
