"""
721 Accounts Merge

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""
# similar problems: 684, 685
# accepted at 7th try!

# Union Find Solution
# As in Solution2, draw edges between emails if they occur in the same account. 
# For easier interoperability between our DSU template, we will map each email to some integer index by using emailToID. 
# Then, dsu.find(email) will tell us a unique id representing what component that email is in.

# For more information on DSU, please look at Approach #2 in the article here. For brevity, the solutions showcased below do not use union-by-rank.
class DSU:
    def __init__(self):
        self.p = list(range(10001))
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

class Solution(object):
    def accountsMerge(self, accounts):
        dsu = DSU()
        em_to_name = {}
        em_to_id = {}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                dsu.union(em_to_id[acc[1]], em_to_id[email])

        ans = collections.defaultdict(list)
        for email in em_to_name:
            ans[dsu.find(em_to_id[email])].append(email)

        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]


import collections
from collections import defaultdict, deque
class Solution2:

    # DFS solution
    # For each account, draw the edge from the first email to all other emails. 
    # Additionally, we'll remember a map from emails to names on the side. 
    # After finding each connected component using a depth-first search, we'll add that to our answer.
    def accountsMerge(self, accounts):
        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name

        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans

    # my own BFS solution by referencing to the above DFS solution
    def accountsMerge2(self, accounts):
        graph, names = defaultdict(set), {}
        for account in accounts:
            n = len(account)
            e = account[1]
            names[e] = account[0]
            for i in range(2, n):
                graph[e].add(account[i])
                graph[account[i]].add(e)
                names[account[i]] = account[0]

        visited, q = set(), deque()
        res = []
        for e in names: # bug fixed: should not use graph because in above code graph will not have a record of email if an account has only one email
            if e in visited:
                continue
            q.clear()
            q.append(e)
            component = []
            while q:
                src = q.popleft()
                if src not in visited:
                    visited.add(src)
                    component.append(src)
                    for dst in graph[src]:
                        q.append(dst)
            
            res.append([names[e]] + sorted(component))

        return res
        

    # my own solution with map from email to record index
    # has bugs because I didn't consider the problem as a graph connection problem, must use BFS or DFS to connect all of them
    def accountsMerge_WRONG(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        records, index = [], 0
        emails = {} # map from email to index
        for account in accounts:
            person = account[0]
            index = len(records)
            # check if any email address belongs to previous record, if so, find the record
            for i in range(1, len(account)):
                if account[i] in emails:
                    index = emails[account[i]]
            
            if index != len(records):
                # we found some email in previous record, copy all emails to that record's set
                records[index][1] |= set(account[1:])
            else:
                # all emails were not found in previous records, append to records
                records.append([person, set(account[1:])])
            # update the emails map
            for i in range(1, len(account)):
                emails[account[i]] = index

        res = []
        for person, unique in records:
            res.append([person] + sorted(list(unique)))

        return res

accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# error: duplicated johnsmith@mail.com
#accounts = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
#accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
print(Solution2().accountsMerge2(accounts))
