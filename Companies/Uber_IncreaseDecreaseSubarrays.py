"""
说如果一个数组，单调递增，单调递减，先递增后递减都符合条件，然后给一个数组，让找出这个数组里所有的subarray符合这些条件的subarray的数量.
【1， 2， 1， 2， 1】里面就有十个subarray, 因为[1(index 0)， 2(index 1)]，[2(index 1)， 1(index 2)]，
[1(index 2)， 2(index 3)]，[2(index 3)， 1(index 4)]，[1(index 0)， 2(index 3)]，[2(index 1)， 1(index 4)]，
[1(index 0)， 2(index 1), 1(index 2)]，[1(index 2)， 2(index 3), 1(index 4)]]，[1(index 0)， 2(index 1), 1(index 4)]]，
[1(index 0)， 2(index 3), 1(index 4)]]，于是return 10；
【1，1，1】 就return 0
思路：建立两个数组:inc[i]表示以arr[i]结尾的递增子数组的个数，dec[i]表示以arr[i]开头的递减子数组的个数，那么最后的结果就是对于每一个i，
累加inc[i] + dec[i] + inc[i]*dec[i]
"""
def numIncDecSubarrays(arr):
    n = len(arr)
    inc = [0]*n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                inc[i] += 1 + inc[j]
    
    dec = [0]*n
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                dec[i] += 1 + dec[j]
    
    res = 0
    for i in range(n):
        res += inc[i] + dec[i] + inc[i]*dec[i]
    
    return res

arr = [1, 1, 1]
print(numIncDecSubarrays(arr)) # expect 0

arr = [1, 2, 1, 2, 1]
print(numIncDecSubarrays(arr)) # expect 10