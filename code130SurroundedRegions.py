"""
130 Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

"""
# start from 'o' in four edges, then use DFS to search neighboring 'o's and mark them as 'non-captured'
# on the second round, change all 'o' to 'x' except those marked 'non-captured'
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # corner cases
        if not board or len(board) == 1 or len(board[0]) == 1:
            return

        m, n = len(board), len(board[0])
        keep = set()    # will put tuple(row_index, col_index) inside to mark that this element should not change to 'x'
        not_processed = []

        # iterate the top and bottom rows, and push the index to "not_processed" list if the element is 'o' 
        for i in range(n - 1):
            if board[0][i] == 'O':
                not_processed.append((0, i))
            if board[m-1][n-1-i] == 'O':
                not_processed.append((m-1, n-1-i))

        # iterate the left and right columns, and push the index to "not_processed" list if the element is 'o' 
        for i in range(m - 1):
            if board[m-1-i][0] == 'O':
                not_processed.append((m-1-i,0))
            if board[i][n-1] == 'O':
                not_processed.append((i, n-1))
        
        # keep marking 'o' as 'keep' because they shoud not be changed to 'x'
        while len(not_processed) > 0:
            (i, j) = not_processed.pop()
            if -1 < i < m and -1 < j < n and board[i][j] == 'O':
                keep.add((i, j))
                neighbors = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
                for neighbor in neighbors:
                    if neighbor not in keep:   # if already in keep, that means this element has been processed
                        not_processed.append(neighbor)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in keep:
                    board[i][j] = 'X'
        
test_case = [
['X', 'X', 'X'],
['X', 'O', 'X'],
['X', 'X', 'X']
]
obj = Solution()
obj.solve(test_case)
print(test_case)