"""
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""
class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if len(num) < 1:
            return []

        # add operators for numbers in the list
        # a [+/-] b [+/-/*] c, initally a = 0
        def _add(nums, s, a, b, sign, target, build, res):
            """
            nums: the list of digits
            s: start index of nums
            a, b: numbers in operation
            sign: 1 for '+' and -1 for '-'
            target: the target value
            build: the growing list
            res: the result to be returned
            """
            if s == len(nums):
                if (a + sign*b) == target:
                    res.append(''.join(build))
            else:
                c = nums[s]
                # try operator '+'
                build.append('+')
                build.append(str(c))
                _add(nums, s + 1, a + sign*b, c, 1, target, build, res)

                # try operator '-'
                build[-2] = '-'
                _add(nums, s + 1, a + sign*b, c, -1, target, build, res)

                # try operator '*'
                build[-2] = '*'
                _add(nums, s + 1, a, b*c, sign, target, build, res)

                # remove the appended strings
                build.pop()
                build.pop()

        nums = [int(c) for c in num]
        res = []
        _add(nums, 1, 0, nums[0], 1, target, [num[0]], res)

        return res

obj = Solution()
print(obj.addOperators('232', 8))