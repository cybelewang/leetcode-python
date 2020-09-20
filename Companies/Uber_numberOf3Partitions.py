"""
有一个integer array， 要将array分成三个subarray要求1st subarray小于等于 2nd subarray sum， 
2nd subarray sum 小于等于 3rd subarray sum。 return所有可能的partition的个数

思路：建立一个从左到右的累加和数组，一个从右到左的累加和数组，然后用两个指针i, j来表示分成的三段：arr[:i], arr[i:j], arr[j:]
i range: 1 to n-2
j range: i + 1 to n-1
"""
import unittest
def numPartitions(arr):
    n = len(arr)
    left = [0] # left[i] is the sum of arr[:i]
    for num in arr:
        left.append(left[-1] + num)

    right = [0] # right[i] is the sum of arr[n-i:]
    for num in reversed(arr):
        right.append(right[-1] + num)

    total = left[-1]
    res = 0
    for i in range(1, n-1):
        first = left[i]
        for j in range(i+1, n):
            third = right[n-j]
            second = total - first - third
            if first <= second <= third:
                res += 1
    
    return res

class Test(unittest.TestCase):
    def test_1(self):
        arr = [1, 1, 1]
        self.assertEqual(numPartitions(arr), 1)

        arr = [1, 1, 1, 1, 1]
        self.assertEqual(numPartitions(arr), 2)

unittest.main(exit = False)