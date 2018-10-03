"""
781 Rabbits in Forest

In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. 
Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.

Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0
Note:

answers will have length at most 1000.
Each answers[i] will be an integer in the range [0, 999].
"""
class Solution:
    # the same-color rabbits can answer x for at most (x+1) times
    def numRabbits(self, answers):
        repeat, res = {}, 0
        for ans in answers:
            if ans not in repeat:   # answer not shown before, this is a new group
                res += ans + 1
                repeat[ans] = 1
            else:
                repeat[ans] += 1    # update repeat times of this color group

            if repeat[ans] > ans + 1:   # the same-color rabbits can answer x for at most (x+1) times, otherwise it's a new color group
                res += ans + 1
                repeat[ans] = 1

        return res
    # my own solution
    # check the number of unique answers
    def numRabbits_Wrong(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        unique = set(answers)
        if 0 in unique: # bug fixed: should consider 0
            unique.remove(0)

        return sum(unique) + len(unique)

#answers = [1,0,1,0,0]   # expected 5
answers = [0, 0, 1, 1, 1]   # expected 6
print(Solution().numRabbits(answers))