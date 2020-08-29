"""
In an exam room, students sit in a m x n matrix, and each student can pass his/her answer to his neighboring student on left, right and behind.
Given the caught probability of passing answers from student A to student B, find the path from student A to student B that has max success probability.
"""
# Dijkstra algorithm
# Assume there is a graph[a][b] which represents student a can pass answer to student b with the value representing the caught probability
# In pre-processing stage, we need to convert caught probability p to -log(1-p), then the problem becomes find the shortest path in a DAG
