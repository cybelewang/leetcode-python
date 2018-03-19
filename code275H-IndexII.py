"""
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
"""
class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        i, j = 0, len(citations) - 1
        while i <= j:
            mid = (i + j)//2
            if citations[mid] < mid + 1:
