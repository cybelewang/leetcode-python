"""
2d array 顺时针旋转90度，*代表障碍，#代表盒子，？代表礼物，礼物如果碰到盒子会掉进盒子，如果碰到障碍物会被挡住，没有遇到障碍物或者盒子就在最底下。
Input:
E ? E
? # E
? * E

Output:
? E E
* # E
E E ?
思路：先把重力方向调成向右90度，礼物往右边坠落，然后矩阵旋转90度就是最后结果
"""
import unittest
# rotate matrix clockwise by 90 degrees
def rotateMatrix(matrix):
    m, n = len(matrix), len(matrix[0])
    res = [[0]*m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            res[j][m-1-i] = matrix[i][j]
    
    return res

# In 1D array, fall gifts to most right side
def fall(arr):
    # scan from right to left
    n = len(arr)
    last = '*' # last is the closest right box ('#') or obstacle ('*')
    pos = n-1 # if the closest right is a obstacle, pos is the next available position to place gift
    for i in range(n-1, -1, -1):
        if arr[i] == '*':
            last, pos = '*', i-1
        elif arr[i] == '#':
            last = '#'
        elif arr[i] == '?':
            if last == '*':
                arr[i] = 'E' # pitfall here: we must set arr[i] to 'E' first, consider the case when pos == i
                arr[pos] = '?'
                pos -= 1                
            else: # last == '#'
                arr[i] = 'E'

def fallGifts(matrix):
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        fall(matrix[i])
    return rotateMatrix(matrix)

class Test(unittest.TestCase):
    def test_fall(self):
        arr = ['E', 'E', 'E']
        exp = ['E', 'E', 'E']
        fall(arr)
        self.assertEqual(arr, exp)

        arr = ['*', '#', '#']
        exp = ['*', '#', '#']
        fall(arr)
        self.assertEqual(arr, exp)

        arr = ['?', 'E', 'E']
        exp = ['E', 'E', '?']
        fall(arr)
        self.assertEqual(arr, exp)

        arr = ['?', 'E', '?', 'E']
        exp = ['E', 'E', '?', '?']
        fall(arr)
        self.assertEqual(arr, exp)

        arr = ['?', '?', 'E', '#', 'E']
        exp = ['E', 'E', 'E', '#', 'E']
        fall(arr)
        self.assertEqual(arr, exp)

        arr = ['?', '?', 'E', '#', 'E', '?', 'E', '?', '*', '*']
        exp = ['E', 'E', 'E', '#', 'E', 'E', '?', '?', '*', '*']
        fall(arr)
        self.assertEqual(arr, exp)

        arr = ['?', '?', 'E', '*', 'E', '?', 'E', '?', '#', '*']
        exp = ['E', '?', '?', '*', 'E', 'E', 'E', 'E', '#', '*']
        fall(arr)
        self.assertEqual(arr, exp)

    def test_rotate(self):
        m = [['E']]
        e = [['E']]
        self.assertEqual(rotateMatrix(m), e)

        m = [['E', '?', '*'], 
             ['#', '#', '?']]
        e = [['#', 'E'],
             ['#', '?'],
             ['?', '*']]
        self.assertEqual(rotateMatrix(m), e)

    def test_fallGifts(self):
        m = [['?', 'E', '*'], 
             ['?', 'E', 'E']]
        e = [['E', 'E'],
             ['E', '?'],
             ['?', '*']]
        self.assertEqual(fallGifts(m), e)

unittest.main(exit = False)
