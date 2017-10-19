"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""
# Ask what to return for "None" and ''
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        build = []
        for dir in path.split('/'):
            if len(dir) > 0 and dir != '.':
                if dir == '..':
                    if len(build) > 0:
                        build.pop()
                else:
                    build.append(dir)
        
        res = '/' + '/'.join(build)

        return res

test_cases = ['/', '/home/','/a/./b/../../c/', '/../', '/home/////etc/../']
obj = Solution()
for case in test_cases:
    print(case, end = ' => ')
    print(obj.simplifyPath(case))