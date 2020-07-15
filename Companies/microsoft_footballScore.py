"""
American football has 4 quarters and each quarter can gain 2, 3, 6 points. If a quarter gets 6 points, then the team can gain another 0, 1, 2 pointers. 
Given the total pointes, output all possible combinations of quarter pointers.
Analysis:
1. Combination sum - can reuse numbers.
2. Convert 6 to 6, 7, 8, and in the end convert it back.
"""
# given a total score, output all possible combinations. No duplicate results.
def football_score_combinations(total):
    points = [2, 3, 6, 7, 8]
    def dfs(points, start, remain, build, res):
        if start >= len(points) or len(build) > 4 or remain < 0:
            return
        if remain == 0 and len(build) == 4:
            res.append(build[:])
            return
        for i in range(start, len(points)):
            build.append(points[i])
            dfs(points, i, remain - points[i], build, res)
            build.pop()
    
    res = []
    dfs(points, 0, total, [], res)
    return res

# given a list of scores, output all possible permutations. No duplicate results
def football_score_permutations(scores):
    scores.sort()
    def dfs(points, used, build, res):
        if len(build) == len(points):
            res.append(build[:])
            return
        for i in range(len(points)):
            if used[i] or (i > 0 and points[i] == points[i-1] and not used[i-1]): continue
            used[i] = True
            build.append(points[i])
            dfs(points, used, build, res)
            build.pop()
            used[i] = False
    used = [False]*len(scores)
    res = []
    dfs(scores, used, [], res)

    return res

# convert 6, 7, 8 to two numbers (6 + 0, 6 + 1, 6 + 2)
def splitSix(scores):
    res = []
    for score in scores:
        if score < 6:
            res.append(score)
        else:
            res.append(6)
            res.append(score-6)
    return res

# main program
total = 15
combinations = football_score_combinations(total)
print("---------------combinations---------------------")
print(combinations)
permutations = []
for comb in combinations:
    permutations.extend(football_score_permutations(comb))
print("---------------permutations---------------------")
print(permutations)
print("---------------final output---------------------")
processed = list(map(splitSix, permutations))
print(processed)