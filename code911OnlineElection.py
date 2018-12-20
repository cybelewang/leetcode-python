"""
911 Online Election

In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.  

Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.

Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation: 
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.

Note:

1 <= persons.length = times.length <= 5000
0 <= persons[i] <= persons.length
times is a strictly increasing array with all elements in [0, 10^9].
TopVotedCandidate.q is called at most 10000 times per test case.
TopVotedCandidate.q(int t) is always called with t >= times[0].
"""
from bisect import bisect
class TopVotedCandidate:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.persons, self.times = persons, times
        # votes: a max-heap list with each element contains [number of votes to the person, last voted time to the person, person]
        # index: a dict maps from person to votes' index
        N, votes, index = len(persons), [None], {}  # votes' start index is 1 for convenience in index calculation
        for i in range(N):
            p, t = persons[i], times[i]
            if p in index:
                j = index[p]
            else:
                j = len(votes)
                votes.append([0, t, p])
                index[p] = j
            # now increase the votes for person
            votes[j][0] += 1
            # update the last voted time
            votes[j][1] = t
            while j > 1 and votes[j//2] < votes[j]:   # keep swaping with parent if parent < child
                parent = votes[j//2][2] # get parent, this is why we need to store person in votes' element
                votes[j], votes[j//2] = votes[j//2], votes[j]   # swap elements with parent in votes' list
                index[parent], index[p] = j, j//2   # update index for parent and this person
                j //= 2 # update j to next iteration
            
            # find the most voted person, and update the result persons list
            self.persons[i] = votes[1][2]
        #print(self.persons)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        i = bisect(self.times, t)   # binary search to find the last vote time
        return self.persons[i-1]

#persons, times, query = [0,1,1,0,0,1,0], [0,5,10,15,20,25,30], [3,12,25,15,24,8]
persons, times, query = [0, 1, 2, 3, 4, 5], [0, 5, 10, 15, 20, 25], [3, 12, 25, 15, 24, 2**31-1, 10]
obj = TopVotedCandidate(persons, times)
for t in query:
    print(obj.q(t))


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)