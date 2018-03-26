"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

"""
class Solution:
    # DFS
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            """
            check if a given string s has valid parentheses
            """
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    if count == 0:
                        return False
                    else:
                        count -= 1
            
            return count == 0

        def helper(s, start, cnt1, cnt2, res):
            """
            recursive subfunction
            """
            if cnt1 == 0 and cnt2 == 0:
                if isValid(s):
                    res.append(s)
                return
            
            for i in range(start, len(s)):
                if i != start and s[i] == s[i-1]:   # negnect continuous same character from the second one, such as '(((' and ')))', we only process the first '(' or ')'
                    continue
                
                if cnt1 > 0 and s[i] == '(':
                    helper(s[:i] + s[i+1:], i, cnt1 - 1, cnt2, res)

                if cnt2 > 0 and s[i] == ')':
                    helper(s[:i] + s[i+1:], i, cnt1, cnt2 - 1, res)

        # cnt1 : number of extra '('
        # cnt2 : number of extra ')'
        cnt1, cnt2 = 0, 0
        for c in s:
            if c == '(':
                cnt1 += 1
            if c == ')':
                if cnt1 == 0:
                    cnt2 += 1
                else:
                    cnt1 -= 1
        
        res = []
        helper(s, 0, cnt1, cnt2, res)

        return res

test_case = '()())()'
obj = Solution()
print(obj.removeInvalidParentheses(test_case))


"""
https://leetcode.com/problems/remove-invalid-parentheses/discuss/75027/Easy-Short-Concise-and-Fast-Java-DFS-3-ms-solution
Key Points:

Generate unique answer once and only once, do not rely on Set.
Do not need preprocess.
Runtime 3 ms.
Explanation:
We all know how to check a string of parentheses is valid using a stack. Or even simpler use a counter.
The counter will increase when it is ‘(‘ and decrease when it is ‘)’. Whenever the counter is negative, we have more ‘)’ than ‘(‘ in the prefix.

To make the prefix valid, we need to remove a ‘)’. The problem is: which one? The answer is any one in the prefix. However, if we remove any one, we will generate duplicate results, for example: s = ()), we can remove s[1] or s[2] but the result is the same (). Thus, we restrict ourself to remove the first ) in a series of concecutive )s.

After the removal, the prefix is then valid. We then call the function recursively to solve the rest of the string. However, we need to keep another information: the last removal position. If we do not have this position, we will generate duplicate by removing two ‘)’ in two steps only with a different order.
For this, we keep tracking the last removal position and only remove ‘)’ after that.

Now one may ask. What about ‘(‘? What if s = ‘(()(()’ in which we need remove ‘(‘?
The answer is: do the same from right to left.
However a cleverer idea is: reverse the string and reuse the code!
Here is the final implement in Java.

Java

public List<String> removeInvalidParentheses(String s) {
    List<String> ans = new ArrayList<>();
    remove(s, ans, 0, 0, new char[]{'(', ')'});
    return ans;
}

public void remove(String s, List<String> ans, int last_i, int last_j,  char[] par) {
    for (int stack = 0, i = last_i; i < s.length(); ++i) {
        if (s.charAt(i) == par[0]) stack++;
        if (s.charAt(i) == par[1]) stack--;
        if (stack >= 0) continue;
        for (int j = last_j; j <= i; ++j)
            if (s.charAt(j) == par[1] && (j == last_j || s.charAt(j - 1) != par[1]))
                remove(s.substring(0, j) + s.substring(j + 1, s.length()), ans, i, j, par);
        return;
    }
    String reversed = new StringBuilder(s).reverse().toString();
    if (par[0] == '(') // finished left to right
        remove(reversed, ans, 0, 0, new char[]{')', '('});
    else // finished right to left
        ans.add(reversed);
}
"""