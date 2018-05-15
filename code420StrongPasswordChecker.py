"""
A password is considered strong if below conditions are all met:

It has at least 6 characters and at most 20 characters.
It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.
"""
class Solution:
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """

"""
https://leetcode.com/problems/strong-password-checker/discuss/91007/C++-0ms-O(n)-35-lines-solution-with-detailed-explanation
I've separated the problem into three cases:
(1) s.length() < 6
(2) 6 <= s.length() <= 20
(3) s.length() > 20

Let's look at case (1) first. If s.length() < 6, we know we have room to insert some more letters into s. Question is how to use the insertions effectively to reduce the number of potential replacements. I'm using a greedy approach for this one: I'm inserting one char between the second and third chars whenever I see a repetition of 3 letters as substring.

e.g. Say we have room to insert some chars in string and we see a substring of "aaaa". I'll insert a 'B' to make it "aaBaa" to break the 3-char repetition, thus reducing potential replacement by 1. And we'll do this until we can't insert any more chars into s. When we reach this point, we'll start dealing with case (2)

For case (2), I still follow a greedy approach. I'm simply searching for 3-char repetitions, and replacing one of the chars to break the repetition.
e.g. If we see a substring of "aaaa", we'll make it "aaBa".

My code deals with (1) and (2) together as s.length() <= 20.

Case (3) is a little bit tricky because simple greedy doesn't work any more.
When s.length() > 20, we want to delete some chars instead of inserting chars to reduce potential replacements. Question is the same: how to do it effectively? Let's do some observations here:

Say len is the length of each repetition.
(a) len % 3 only has three possible values, namely 0, 1 and 2.
(b) Minimum number of replacements needed to break each repetition is len / 3.
(c) Based on (a) and (b), we know that deletion can reduce replacements only if the deletion can change the value of len / 3
(d) Based on (c), we know if we want to reduce 1 replacement, we need 1 deletion for len % 3 == 0, and 2 deletions for len % 3 == 1, and 3 deletions for len % 3 == 2.

Given above observations, I simply implemented the solution to do (d).

Also note that missing of upper case char, lower case char, or digit can always be resolved by insertion or replacement.

I've pasted two versions of the solutions below, with and without comments, for easier reference.

Without comments:

class Solution {
public:
    int strongPasswordChecker(string s) {
        int deleteTarget = max(0, (int)s.length() - 20), addTarget = max(0, 6 - (int)s.length());
        int toDelete = 0, toAdd = 0, toReplace = 0, needUpper = 1, needLower = 1, needDigit = 1;
        
        for (int l = 0, r = 0; r < s.length(); r++) {
            if (isupper(s[r])) { needUpper = 0; }               
            if (islower(s[r])) { needLower = 0; }
            if (isdigit(s[r])) { needDigit = 0; }
            
            if (r - l == 2) {                               
                if (s[l] == s[l + 1] && s[l + 1] == s[r]) {     
                    if (toAdd < addTarget) { toAdd++, l = r; }  
                    else { toReplace++, l = r + 1; }           
                } else { l++; }                                 
            }
        }
        if (s.length() <= 20) { return max(addTarget + toReplace, needUpper + needLower + needDigit); }
        
        toReplace = 0;                                         
        vector<unordered_map<int, int>> lenCnts(3);            
        for (int l = 0, r = 0, len; r <= s.length(); r++) {    
            if (r == s.length() || s[l] != s[r]) {
                if ((len = r - l) > 2) { lenCnts[len % 3][len]++; } 
                l = r;
            }
        }
        
        for (int i = 0, numLetters, dec; i < 3; i++) {                
            for (auto it = lenCnts[i].begin(); it != lenCnts[i].end(); it++) {
                if (i < 2) {
                    numLetters = i + 1, dec = min(it->second, (deleteTarget - toDelete) / numLetters);
                    toDelete += dec * numLetters, it->second -= dec;                          
                    if (it->first - numLetters > 2) { lenCnts[2][it->first - numLetters] += dec; }   
                }
                toReplace += (it->second) * ((it->first) / 3);  
            }    
        }

        int dec = (deleteTarget - toDelete) / 3;                
        toReplace -= dec, toDelete -= dec * 3;
        return deleteTarget + max(toReplace, needUpper + needLower + needDigit);
    }
};
With comments:

class Solution {
public:
    int strongPasswordChecker(string s) {
        int deleteTarget = max(0, (int)s.length() - 20), addTarget = max(0, 6 - (int)s.length());
        int toDelete = 0, toAdd = 0, toReplace = 0, needUpper = 1, needLower = 1, needDigit = 1;
        
        ///////////////////////////////////
        // For cases of s.length() <= 20 //
        ///////////////////////////////////
        for (int l = 0, r = 0; r < s.length(); r++) {
            if (isupper(s[r])) { needUpper = 0; }               
            if (islower(s[r])) { needLower = 0; }
            if (isdigit(s[r])) { needDigit = 0; }
            
            if (r - l == 2) {                                   // if it's a three-letter window
                if (s[l] == s[l + 1] && s[l + 1] == s[r]) {     // found a three-repeating substr
                    if (toAdd < addTarget) { toAdd++, l = r; }  // insert letter to break repetition if possible
                    else { toReplace++, l = r + 1; }            // replace current word to avoid three repeating chars
                } else { l++; }                                 // keep the window with no more than 3 letters
            }
        }
        if (s.length() <= 20) { return max(addTarget + toReplace, needUpper + needLower + needDigit); }
        
        //////////////////////////////////
        // For cases of s.length() > 20 //
        //////////////////////////////////
        toReplace = 0;                                          // reset toReplace
        vector<unordered_map<int, int>> lenCnts(3);             // to record repetitions with (length % 3) == 0, 1 or 2
        for (int l = 0, r = 0, len; r <= s.length(); r++) {     // record all repetion frequencies
            if (r == s.length() || s[l] != s[r]) {
                if ((len = r - l) > 2) { lenCnts[len % 3][len]++; } // we only care about repetions with length >= 3
                l = r;
            }
        }
        
        /*
            Use deletions to minimize replacements, following below orders:
            (1) Try to delete one letter from repetitions with (length % 3) == 0. Each deletion decreases replacement by 1
            (2) Try to delete two letters from repetitions with (length % 3) == 1. Each deletion decreases repalcement by 1
            (3) Try to delete multiple of three letters from repetions with (length % 3) == 2. Each deletion (of three 
            letters) decreases repalcements by 1
        */
        for (int i = 0, numLetters, dec; i < 3; i++) {                
            for (auto it = lenCnts[i].begin(); it != lenCnts[i].end(); it++) {
                if (i < 2) {
                    numLetters = i + 1, dec = min(it->second, (deleteTarget - toDelete) / numLetters);
                    toDelete += dec * numLetters;               // dec is the number of repetitions we'll delete from
                    it->second -= dec;                          // update number of repetitions left
                    
                    // after letters deleted, it fits in the group where (length % 3) == 2
                    if (it->first - numLetters > 2) { lenCnts[2][it->first - numLetters] += dec; }   
                }
                
                // record number of replacements needed
                // note if len is the length of repetition, we need (len / 3) number of replacements
                toReplace += (it->second) * ((it->first) / 3);  
            }    
        }

        int dec = (deleteTarget - toDelete) / 3;                // try to delete multiple of three letters as many as possible
        toReplace -= dec, toDelete -= dec * 3;
        return deleteTarget + max(toReplace, needUpper + needLower + needDigit);
    }
};
"""        