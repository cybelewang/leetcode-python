"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
"""

# What about '1.', '..'?
# pitfalls: '1' and '1.0', '01' and '1', '1.0.0.0' and '1.000.00'
class Solution:
    # 
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        nums1 = list(map(int, version1.split('.')))
        nums2 = list(map(int, version2.split('.')))

        while nums1 and nums1[-1] == 0:
            nums1.pop()
        nums1.append(0)

        while nums2 and nums2[-1] == 0:
            nums2.pop()
        nums2.append(0)

        n1, n2 = len(nums1), len(nums2)
        for i in range(min(n1, n2)):
            if nums1[i] > nums2[i]:
                return 1
            elif nums1[i] < nums2[i]:
                return -1
        
        if n1 > n2:
            return 1
        elif n1 < n2:
            return -1
        else:
            return 0

test_cases = [('0','1'), ('1.0', '1'), ('0.0', '1.0'), ('0.1','0.1'), ('0.0.9', '0.1'), ('1.5.91', '1.4.100')]
obj = Solution()
for case in test_cases:
    print(obj.compareVersion(case[0], case[1]))