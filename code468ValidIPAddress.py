"""
468 Validate IP Address

Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.
"""
# python 3 module "ipaddress" doesn't handle scenarios of "::" and leading zeros
class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def valid_IPv4_segment(s):
            """
            check if given string s is a valid IPv4 segment
            """
            n = len(s)
            if n < 1 or n > 3:
                return False
            
            try:
                num = int(s)
                return -1 < num < 256 and str(num) == s # convert back to string to filter leading zeros and invalid characters with spaces, etc
            except:
                return False

        # a set of all valid hex characters
        valid_hex_chars = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F'])
        #print(valid_hex_chars)
        def valid_IPv6_segment(s):
            """
            check if given string s is a valid IPv4 segment
            """
            n = len(s)
            return 0 < n < 5 and all(c in valid_hex_chars for c in s)

        if IP.count('.') == 3:  # check IPv4
            fields = IP.split('.')
            if all(valid_IPv4_segment(f) for f in fields):
                return "IPv4"
        elif IP.count(':') == 7: # check IPv6
            fields = IP.split(':')
            if all(valid_IPv6_segment(f) for f in fields):
                return "IPv6"

        return "Neither"        


test_IPs = ['172.16.254.1', '172.16.254.01', '', '....', '277.0.0.1', '2001:0db8:85a3::8A2E:0370:7334', '2001:0db8:85a3:0000:0000:8a2e:0370:7334', '02001:0db8:85a3:0000:0000:8a2e:0370:7334']
obj = Solution()
for IP in test_IPs:
    print(obj.validIPAddress(IP))