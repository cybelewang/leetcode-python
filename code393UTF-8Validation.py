"""
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
"""
class Solution:
    # OJ's best solution, but OJ test cases don't check data range
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count=0
        for x in data:
            if count==0:
                if x>>5==0b110:
                    count=1
                elif x>>4==0b1110:
                    count=2
                elif x>>3==0b11110:
                    count=3
                elif x>>7==1:
                    return False
            else:
                if x>>6!=0b10:
                    return False
                count-=1
        return count==0
    # my solution, also checking the data range
    def validUtf8_2(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        start = 0
        while start < len(data):
            first = data[start]
            count, factor = 0, 0x80
            while first & factor:
                count += 1
                factor //=2
            if count > 4:   # bug fixed: count may > 4
                return False
            mask = 1 << (7-count)   # bit 1 on the '0' position
            if count == 1 or first & mask:
                return False
            # decoded value from the first byte
            value = first & (mask - 1)
            
            # count == 0, no need to check
            # count == 2 to 4, check if following integers start with binary 10
            for i in range(1, count):
                # maybe out of index
                if start + i >= len(data):
                    return False
                follow = data[start + i]
                if follow & 0xC0 != 0x80:
                    return False

                # continuously update the decoded value
                value = (value << 6) + (follow & 0x3F)

            # now check if decoded value is in range, we only need to check if value >= min_range
            # count == 0, always valid
            if (count == 2 and value < 0x80) or \
                (count == 3 and value < 0x800) or \
                (count == 4 and value < 0x10000):
                return False

            # advance start index
            start += count if count > 0 else 1  # bug fixed: count may be zero and start will never advance!!!
        
        return True

obj = Solution()
data = [194,155,231,184,185,246,176,131,161,222,174,227,162,134,241,154,168,185,218,178,229,187,139,246,178,187,139,204,146,225,148,179,245,139,172,134,193,156,233,131,154,240,166,188,190,216,150,230,145,144,240,167,140,163,221,190,238,168,139,241,154,159,164,199,170,224,173,140,244,182,143,134,206,181,227,172,141,241,146,159,170,202,134,230,142,163,244,172,140,191]
print(obj.validUtf8(data))