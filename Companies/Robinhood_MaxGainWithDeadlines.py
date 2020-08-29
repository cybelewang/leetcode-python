"""
Job Sequencing Problem

Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline. 
It is also given that every job takes single unit of time, so the minimum possible deadline for any job is 1. 
How to maximize total profit if only one job can be scheduled at a time.

Examples:

Input: Four Jobs with following 
deadlines and profits
JobID  Deadline  Profit
  a      4        20   
  b      1        10
  c      1        40  
  d      1        30
Output: Following is maximum 
profit sequence of jobs
        c, a   


Input:  Five Jobs with following
deadlines and profits
JobID   Deadline  Profit
  a       2        100
  b       1        19
  c       2        27
  d       1        25
  e       3        15
Output: Following is maximum 
profit sequence of jobs
        c, a, e

Reference: https://www.geeksforgeeks.org/job-sequencing-problem/
"""
from heapq import heapify, heappop
# greedy solution, O(N^2)
# (1) sort jobs based on descending deadline
# (2) for each job, find the greatest unfilled time slot that <= deadline, if not found, skip this job
def maxJobGainScheduling(jobs):    
    T = 0 # the max deadline
    for _, t, _ in jobs: T = max(t, T)
    # jobs[i] contains job id (str), deadline (int), gain (int)
    jobs.sort(key = lambda job: (-job[2], -job[1]))
    #print(jobs)
    res, maxGain = [], 0
    free = [True]*(T+1)
    free[0] = False
    for id, dl, gain in jobs:
        t = dl
        while t > 0 and not free[t]:
            t -= 1
        if t > 0:
            free[t] = False
            maxGain += gain
            res.append(id)

    print(res)
    print(maxGain)

# Improved greedy solution with union find to find the greatest unfilled time slot <= deadline
def maxJobGainScheduling2(jobs):
    def find(root, i):
        while i != root[i]:
            i = root[i]
        return i
    
    T = 0 # the max deadline
    for _, t, _ in jobs: T = max(t, T)
    # jobs[i] contains job id (str), deadline (int), gain (int)
    jobs.sort(key = lambda job: (-job[2], -job[1]))
    free = list(range(T+1))
    res, maxGain = [], 0
    for id, dl, gain in jobs:
        t = find(free, dl)
        if t > 0:
            maxGain += gain
            res.append(id)
            free[t] = find(free, t-1)

    print(res)
    print(maxGain)

# greedy with deadline check, wrong solution on test case jobs = [['A', 1, 1], ['B', 2, 2], ['C', 3, 3]]
def maxJobGainScheduling3(jobs):
    arr = [[-gain, dl, id] for id, dl, gain in jobs]
    heapify(arr)
    print(arr)
    t, maxGain, res = 1, 0, []
    while arr:
        g, dl, id = heappop(arr)
        if t <= dl:
            maxGain -= g
            res.append(id)
            t += 1
        
    print(res)
    print(maxGain)

jobs = [['a', 2, 100],
       ['b', 1, 19], 
       ['c', 2, 27], 
       ['d', 1, 25], 
       ['e', 3, 15]] 
maxJobGainScheduling3(jobs)

jobs = [['A', 3, 3],
        ['B', 3, 2],
        ['C', 2, 4],
        ['D', 1, 1]]
maxJobGainScheduling3(jobs)

jobs = [['A', 1, 1],
        ['B', 2, 2],
        ['C', 3, 3]]
maxJobGainScheduling2(jobs)      