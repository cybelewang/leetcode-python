"""
Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.

"""
class Solution:
    # OJ best solution
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        dict={0:0}
        maxlen=0
        line=input.split("\n")
        for i in line:
            name=i.lstrip('\t')
            #print(name)
            #print(len(name))
            depth=len(i)-len(name)
            if '.' in name:
                maxlen=max(maxlen, dict[depth]+len(name))
            else:
                dict[depth+1]=dict[depth]+len(name)+1
        return maxlen
    # my solution
    def lengthLongestPath2(self, input):
        """
        :type input: str
        :rtype: int
        """
        def countLevel(s, start):
            """
            return the level of path starting from index "start"
            """
            level = 0
            while (start+1 <= len(s)) and (s[start:start+1] == '\t'):
                level += 1
                start += 1

            return (level, start)

        start, res = 0, 0
        stack = [(-1, 0)] # tuple (level, total length of the directions including '/'), bug fixe: very import to initialiate it with (-1, 0) (like a virtual root direction) to make sure stack will never be empty, think about "dir\ndir1\nabc.txt"
        
        while start < len(input):
            # get upper level direction's level number, and total length
            upper_level, upper_length = stack[-1]
            # parse current substr's level and start index
            level, start = countLevel(input, start)
            # bug fixed: remove lower or equal level directions, as file name may be at the same level, or upper level of last direction
            while level <= upper_level:
                stack.pop() # we do not need to care about empty stack because level will always > -1
                upper_level, upper_length = stack[-1]

            # get the end index of this substr
            end = input.find('\n', start)
            if end == -1:
                # this hits the end of path
                end = len(input)

            if input[start:end].count('.') > 0:
                # this is a file name (having extension)
                res = max(res, end-start+upper_length)   # end-start: this substr length, +1: '/'
            else:
                # this is a direction
                stack.append((level, end-start+upper_length+1)) # end-start: this substr length, +1: '/' at the end

            # reset start to beginning of next substr
            start = end + 1

        return res

input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext\n\tsubdir3\n\tveryveryveryveryveryveryveryveryveryverylong.txt"
#"abc.exe"
#"dir\ndir1\nabc.txt"
#"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext\n\tsubdir3\n\tveryveryveryveryveryveryveryveryveryverylong.txt"
obj = Solution()
print(obj.lengthLongestPath(input))