"""
657 Robot Return to Origin

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). 
The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""
# similar problems: valid parentheses
class Solution:
    # http://www.cnblogs.com/grandyang/p/7514416.html
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')

    # my own solution using a set, check if the robot goes to a position more than once
    # wrongly understood the requirement, which needs to check if the final position is (0, 0)
    def judgeCircle2(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        offset = {'U':(0, 1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}
        history = {(x, y)}
        for dir in moves:
            dx, dy = offset[dir]
            x, y = x+dx, y+dy
            if (x, y) in history:
                return True
            history.add((x,y))
        
        return False
