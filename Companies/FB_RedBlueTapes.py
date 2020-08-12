"""
Give red tapes and blue tapes, paste red tapes first, then blue tapes. Check if red tapes can be covered.
"""
def mergeIntervals(intervals):
    # merge a list of intervals in place
    intervals.sort()
    i = 1
    while i < len(intervals):
        if intervals[i][0] <= intervals[i-1][1]:
            intervals[i-1][1] = max(intervals[i][1], intervals[i-1][1])
            intervals.pop(i)
        else:
            i += 1

def checkTapCoverage(blueTapes, redTapes):
    mergeIntervals(blueTapes)
    print(blueTapes)
    mergeIntervals(redTapes)
    print(redTapes)
    i, j = 0, 0
    while i < len(redTapes):
        if j == len(blueTapes):
            return False
        if blueTapes[j][1] <= redTapes[i][0]:
            j += 1
            continue
        if blueTapes[j][0] <= redTapes[i][0] and blueTapes[j][1] >= redTapes[i][1]:
            i += 1
        else:
            return False
    
    return True

blue = [[0, 2], [3, 5]]
red = [[1,2], [2,3]]
print(checkTapCoverage(blue, red))