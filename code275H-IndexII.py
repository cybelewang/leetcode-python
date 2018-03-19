"""
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
"""
class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n < 1:
            return 0

        i, j = 0, n - 1
        while i <= j:
            mid = (i + j)//2
            if citations[mid] < n - mid:
                i = mid + 1
            else:
                j = mid - 1

        return n - i

test_cases = [[9], [9, 9], [0], [0, 0], [0, 1, 3, 5, 6]]
obj = Solution()
for case in test_cases:
    print(obj.hIndex(case))