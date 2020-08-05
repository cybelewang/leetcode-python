"""
158 Read N Characters Given Read4 II - Call multiple times

Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. Your method read may be called multiple times.
 
Method read4: 
The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.
The return value is the number of actual characters read.
Note that read4() has its own file pointer, much like FILE *fp in C.
Definition of read4:
    Parameter:  char[] buf4
    Returns:    int

Note: buf4[] is destination not source, the results from read4 will be copied to buf4[]
Below is a high level example of how read4 works:

File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
char[] buf = new char[4]; // Create buffer with enough space to store characters
read4(buf4); // read4 returns 4. Now buf = "abcd", fp points to 'e'
read4(buf4); // read4 returns 1. Now buf = "e", fp points to end of file
read4(buf4); // read4 returns 0. Now buf = "", fp points to end of file
 
Method read:
By using the read4 method, implement the method read that reads n characters from the file and store it in the buffer array buf. Consider that you cannot manipulate the file directly.
The return value is the number of actual characters read.
Definition of read: 
    Parameters:	char[] buf, int n
    Returns:	int

Note: buf[] is destination not source, you will need to write the results to buf[]
 
Example 1:
File file("abc");
Solution sol;
// Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.
sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.
sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
Example 2:
File file("abc");
Solution sol;
sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
 
Note:
Consider that you cannot manipulate the file directly, the file is only accesible for read4 but not for read.
The read function may be called multiple times.
Please remember to RESET your class variables declared in Solution, as static/class variables are persisted across multiple test cases. Please see here for more details.
You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
It is guaranteed that in a given test case the same buffer buf is called by read.
"""
# Suitable for python because of python's list range selection
# Understand problem correctly:
# (1) buf4 must be initialized correctly, we can't pass an empty buf4 to read4 because read4 won't fill buf4 for us, instead read4 will copy element one by one to buf4.
# (2) read4 will return actual size it reads, assume the size is cnt, then buf4[:cnt] is the actual range we can use.
# (3) After buf extending buf4, if the size is bigger than n, the overflow elements should be picked up by next read call, so we should store the overflow elements.
# (4) input buf has already been initialized to a list which can hold n or more characters

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.overflow = []  # overflow elements from last "read" call, initially this is empty
        
    def read(self, buf: List[str], n: int) -> int:
        buf.clear()
        if n < 1: return 0        
        
        buf.extend(self.overflow) # take the overflow elements from last "read" call
        while len(buf) < n: # continue calling "read4" if length < n
            buf4 = ['']*4 # initialize buf4 to size 4
            cnt = read4(buf4)
            if cnt == 0: break # no more elements from read4, exit while loop
            buf.extend(buf4[:cnt])
        
        self.overflow = buf[n:]
        buf = buf[:n]
        
        return len(buf)

# 8/2/2020 solution without clearing input buf, this is more similar to C
# instead of extending read chars to buf, we copy chars to buf
class Solution:
    def __init__(self):
        self.overflow = []
        
    def read(self, buf: List[str], n: int) -> int:        
        buf[:len(self.overflow)] = self.overflow
        i = len(self.overflow)
        while i < n:
            buf4 = ['']*4
            k = read4(buf4)
            if k == 0:
                break
            buf[i:i+k] = buf4[:k]
            i += k
        
        self.overflow = buf[n:i]
        return min(i, n)