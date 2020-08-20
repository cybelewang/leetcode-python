"""
815 Bus Routes

We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6. 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 10^5.
0 <= routes[i][j] < 10 ^ 6.
"""
class Solution:
    # BFS to traverse buses, better than traverse stops because there are too many stops
    # need to create graph for buses connected to each other
    def numBusesToDestination(self, routes, S, T) -> int:
        if S == T: return 0
        graph = defaultdict(set) # graph[i][j] means bus i and bus j are connected
        buses = defaultdict(set) # buses[i] contains all buses reach to stop i
        for b, stops in enumerate(routes):
            for s in stops:
                for c in buses[s]:
                    graph[b].add(c)
                    graph[c].add(b)
                buses[s].add(b)
        
        q, level = deque(buses[S]), 1
        visited = set(buses[S])
        while q:
            length = len(q)
            for _ in range(length):
                b = q.popleft()
                if b in buses[T]: return level
                for c in graph[b]:
                    if c not in visited:
                        visited.add(c)
                        q.append(c)
            level += 1
        
        return -1

    # BFS to traverse stops, visited must store buses, otherwise TLE
    def numBusesToDestination2(self, routes, S, T):
        if S == T:
            return 0
        
        buses = defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                buses[stop].append(bus)
                
        visited = set() # saves buses taken
        q, level = deque([S]), 1
        for b in buses[S]:
            visited.add(b)
            for s in routes[b]:
                if s == T: return 1
                q.append(s)
         
        # BFS
        while q:
            length = len(q)
            for _ in range(length):
                s = q.popleft()
                for b in buses[s]:
                    if b not in visited:
                        visited.add(b)
                        for t in routes[b]:
                            if t == T: return level + 1
                            q.append(t)

            level += 1
        
        return -1

            