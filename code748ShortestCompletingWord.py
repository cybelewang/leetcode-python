"""
748 Shortest Completing Word

Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate. 
Such a word is said to complete the given string licensePlate.

Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.

It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.

The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.

Example 1:
Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
Output: "steps"
Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
Note that the answer is not "step", because the letter "s" must occur in the word twice.
Also note that we ignored case for the purposes of comparing whether a letter exists in the word.
Example 2:
Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
Output: "pest"
Explanation: There are 3 smallest length words that contains the letters "s".
We return the one that occurred first.
Note:
licensePlate will be a string with length in range [1, 7].
licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
words will have a length in the range [10, 1000].
Every words[i] will consist of lowercase letters, and have length in range [1, 15].
"""
# similar problems: 438 Find All Anagrams in a String
from collections import defaultdict, Counter
class Solution:
    # my own solution
    # using a 32-bit integer to encode the count match: if a letter's count in word[i] is < that letter's count in license plate
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        count, target = defaultdict(int), 0
        for char in licensePlate.lower():
            index = ord(char) - ord('a')            
            if -1 < index < 26:
                count[char] += 1
                target |= (1 << index)

        res = None
        for word in words:
            encode, count1 = target, Counter(word)
            for letter in count:
                if count1[letter] >= count[letter]:
                    encode &= ~(1 << (ord(letter) - ord('a')))
            
            if encode == 0 and (res == None or len(word) < len(res)):
                res = word
        
        return res

#licensePlate = "1s3 PSt"
#words = ["step", "steps", "stripe", "stepple"]
licensePlate = "1s3 456"
words = ["looks", "pest", "stew", "show"]
obj = Solution()
print(obj.shortestCompletingWord(licensePlate, words))        
