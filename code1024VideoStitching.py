"""
1024 Video Stitching

You are given a series of video clips from a sporting event that lasted T seconds.  These video clips can be overlapping with each other and have varied lengths.
Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends at time clips[i][1].  We can cut these clips into segments freely: for example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event ([0, T]).  If the task is impossible, return -1.

Example 1:
Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
Output: 3
Explanation: 
We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].

Example 2:
Input: clips = [[0,1],[1,2]], T = 5
Output: -1
Explanation: 
We can't cover [0,5] with only [0,1] and [0,2].

Example 3:
Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
Output: 3
Explanation: 
We can take clips [0,4], [4,7], and [6,9].

Example 4:
Input: clips = [[0,4],[2,8]], T = 5
Output: 2
Explanation: 
Notice you can have extra video after the event ends.

Note:

1 <= clips.length <= 100
0 <= clips[i][0], clips[i][1] <= 100
0 <= T <= 100
"""
# tag: greedy, interval
# similar problems: 45 Jump Game II
class Solution:
    def videoStitching(self, clips, T):
        """
        :type clips: list[list[int]]
        :type T: int
        :rtype: int
        """
        pre, t, count = 0, 0, 0 # pre: the last selected interval's end time, t: max end time 
        for s, e in sorted(clips):
            # current start > previous end, we try to add an interval with max end time 
            if s > pre:                
                if t > pre: # this is possible only when max end time > previous end time
                    pre = t # update previous end time to t
                    count += 1  # and increase count by 1
                else:
                    return -1   # if max end time <= previous end time, it's impossible to go further
            
            if s <= pre:
                t = max(t, e)
                if t >= T:
                    return count + 1
        
        return -1

    # easier to understand logic (onenote)
    def videoStitching2(self, clips, T):
        pre, t, count = 0, 0, 0
        for s, e in sorted(clips):
            if s <= pre:
                # overlap with last selected clip
                t = max(t, e)   # extend t as much as possible
                if t >= T:
                    return count + 1
            else:
                # not overlap with last selected clip
                if s <= t:  # check if t was extended enough to reach s
                    # update pre and count
                    pre = t
                    count += 1
                    # need to process this clip
                    t = max(t, e)
                    if t >= T:
                        return count + 1
                else:
                    return -1

        return -1

clips, T = [[0, 0]], 0  # expect 1
clips, T = [[0,1],[1,2]], 5 # expect -1
clips, T = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9 # expect 3
print(Solution().videoStitching2(clips, T))