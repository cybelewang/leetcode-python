"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""
def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    offset, N = 0, len(matrix)
    while N > 1:
        temp = matrix[offset][offset:offset+N-1]                
        for i in range(N-1):
            # left to top
            matrix[offset][offset+i] = matrix[offset + N - 1 - i][offset]
            # bottom to left
            matrix[offset + N - 1 - i][offset] = matrix[offset + N - 1][offset + N - 1 - i]
            # right to bottom
            matrix[offset + N - 1][offset + N - 1 - i] = matrix[offset + i][offset + N - 1]
            # top to right
            matrix[offset + i][offset + N - 1] = temp[i]
          
        offset += 1
        N -= 2

test_cases = [[[]], [[1]], [[1,2],[3,4]], [[1,2,3],[4,5,6],[7,8,9]], [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]]
for A in test_cases:    
    print(A, end=' -> ')
    rotate(A)
    print(A)
