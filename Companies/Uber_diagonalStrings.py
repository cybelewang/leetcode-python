"""
Sort parallel diagnol string
eg：
a b c d
e f g h
l m n o
p q r s
存在的diagnol就是从左下角开始， 保证每个diagnol组成的string长度一样我们就可以得到 “pppp”, "lplp", "emre", "afns","bgob","chch", "dddd"
然后对这几个string排序
"""
def appendLetters(arr, length):
    n = len(arr)
    while len(arr) < length:
        arr.extend(arr[:n])
    return ''.join(arr[:length])

def getDiagonalStrings(matrix):
    m, n = len(matrix), len(matrix[0])
    max_len = min(m, n)
    res = []
    for su in range(1-m, n):
        lower = max(0, -su)
        upper = min(m, n-su)
        letters = []
        for i in range(lower, upper):
            j = i + su
            letters.append(matrix[i][j])
        res.append(appendLetters(letters, max_len))
    return res

matrix = [['a', 'b', 'c', 'd'],
          ['e', 'f', 'g', 'h'],
          ['l', 'm', 'n', 'o'],
          ['p', 'q', 'r', 's']]

print(getDiagonalStrings(matrix))