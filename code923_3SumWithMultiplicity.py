"""
923 3Sum With Multiplicity

Given an integer array A, and an integer target, return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.

Example 1:

Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:

Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.

Note:

3 <= A.length <= 3000
0 <= A[i] <= 100
0 <= target <= 300
"""
# similar problems: 167 Two Sum II - Input array is sorted; 15 3Sum, three sum
class Solution:
    # similar to problem 15's solution
    # first sort A
    # second iterate all elements in A, for each element x, we need to find remaining elements with sum of target - x
    # Then we use problem 167's method, using two pointers to find elements with sum of target - x
    # the difference of this problem is to count the pairs of the two elements, so we need to divide to two scenarios: when A[j] == A[k] and A[j] != A[k]
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        A.sort()
        ans, M = 0, 10**9 + 7
        for i, x in enumerate(A):
            T = target - x
            j, k = i + 1, len(A) - 1
            while j < k:
                if A[j] + A[k] < T:
                    j += 1
                elif A[j] + A[k] > T:
                    k -= 1
                else:   # A[j] + A[k] == target - A[i]
                    if A[j] == A[k]:    # we choose 2 elements from (k-j+1) elements
                        ans = (ans + (k-j+1)*(k-j)//2)%M
                        break
                    else:
                        cnt1, cnt2 = 1, 1   # count of A[j] and A[k]
                        j, k = j+1, k-1
                        # update counts and index
                        while A[j] == A[j-1]:
                            j += 1
                            cnt1 += 1
                        while A[k] == A[k+1]:
                            k -= 1
                            cnt2 += 1
                        # as A[j] and A[k] are different, we time their counts
                        ans = (ans + cnt1*cnt2)%M

        
        return ans

A, target = [1,1,2,2,3,3,4,4,5,5], 8
#A, target = [1,1,2,2,2,2], 5
print(Solution().threeSumMulti(A, target))