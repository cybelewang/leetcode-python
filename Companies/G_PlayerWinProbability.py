"""
https://www.1point3acres.com/bbs/interview/google-software-engineer-176810.html
Given a list represented the initial matching teams, and a matrix representing each team's win probability to another team, 
find a team's tournament winning probability.
"""

# Use divide and conquer, similar to merge sort
# in merging process, each team i's winning probability is like the sum of left[i]*right[j]*winProb[i][j]