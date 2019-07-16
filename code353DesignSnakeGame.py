"""
353 Design Snake Game

Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.
The snake is initially positioned at the top left corner (0,0) with length = 1 unit.
You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.
Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.
When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

Example:
Given width = 3, height = 2, and food = [[1,2],[0,1]].
Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).
|S| | |
| | |F|

snake.move("R"); -> Returns 0
| |S| |
| | |F|

snake.move("D"); -> Returns 0
| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )
| |F| |
| |S|S|

snake.move("U"); -> Returns 1
| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)
| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)
"""
import unittest
from collections import deque
class SnakeGame:

    def __init__(self, width, height, food):
        '''
        :type food: list[list[int]] a list of food positions
        '''
        if width < 1 or height < 1:
            raise ValueError

        self.width = width
        self.height = height
        self.food = food[::-1]

        self.board = [[0]*width for _ in range(height)] # [x][y] == 1 means x, y is snake body
        self.board[0][0] = 1
        self.snake = deque([(0, 0)])    # contains the coordinates of snakes

    def move(self, direction):
        '''
        :type direction: str, 'U', 'L', 'R', 'D'
        '''
        # get next coordinate based on the given direction
        x, y = self.snake[0]
        if direction == 'U':
            x -= 1
        elif direction == 'D':
            x += 1
        elif direction == 'L':
            y -= 1
        else:
            y += 1
        
        # touch boards or snake body, game over
        if x < 0 or x >= self.height or y < 0 or y >= self.width or self.board[x][y] == 1:
            return -1
        
        self.snake.appendleft((x, y))   # push new head to front of snake
        self.board[x][y] = 1 # mark [x][y] as snake body
        if self.food and self.food[-1][0] == x and self.food[-1][1] == y:
            # eat a food but do not remove the tail
            self.food.pop()
        else:
            # remove tail
            tail_x, tail_y = self.snake.pop()
            self.board[tail_x][tail_y] = 0
        
        return len(self.snake) - 1

# unit test
class Test(unittest.TestCase):
    def test_InvalidInput(self):
        with self.assertRaises(ValueError):
            game = SnakeGame(0, 0, [])
    
    def test_3x3(self):
        game = SnakeGame(3, 3, [[1, 2], [0, 1]])
        directions = ['R', 'D', 'R', 'U', 'L', 'U']
        expected = [0, 0, 1, 1, 2, -1]
        for dir, res in zip(directions, expected):
            self.assertEqual(game.move(dir), res)

if __name__ == '__main__':
    unittest.main(exit=False)