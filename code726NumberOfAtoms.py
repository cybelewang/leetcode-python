"""
726 Number of Atoms

Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

Example 1:
Input: 
formula = "H2O"
Output: "H2O"
Explanation: 
The count of elements are {'H': 2, 'O': 1}.
Example 2:
Input: 
formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: 
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:
Input: 
formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: 
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
Note:

All atom names consist of lowercase letters, except for the first character which is uppercase.
The length of formula will be in the range [1, 1000].
formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.
"""
from collections import defaultdict
class Solution:
    # my own solution with bug fixed
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stack = []
        i, element = 0, ''
        count = defaultdict(int)
        while i < len(formula):
            c = formula[i]
            if 64 < ord(c) < 91:
                # this is an upper case letter, start a new element
                j = i + 1   # end index (exclusive) of the new element
                while j < len(formula) and 96 <ord(formula[j])< 123:
                    j += 1
                element = formula[i:j]  # new element
                # now search for the number for this elements
                i = j
                while j < len(formula) and 47 < ord(formula[j]) < 58:
                    j += 1
                # update count map
                if i == j:
                    count[element] += 1
                else:
                    count[element] += int(formula[i:j])
                    i = j
            elif c == '(':
                # enter a sub formula
                stack.append(count)
                count = defaultdict(int)
                i += 1
            else: #if c == ')':
                # exit a sub formula
                i += 1
                # get the repeat of the sub formula
                j = i
                while j < len(formula) and 47 < ord(formula[j]) < 58:
                    j += 1
                repeat = 1
                if i < j:
                    repeat = int(formula[i:j])
                    i = j
                # apply repeat to current count map
                for e in count:
                    count[e] *= repeat
                # merge with previous count map
                previous = stack.pop()
                for p in previous:
                    if p in count:
                        count[p] += previous[p]
                    else:
                        count[p] = previous[p]
                # bug fixed: should not push count back to stack
                #stack.append(count)

        # out of while loop
        res = ''
        for e in sorted(count.keys()):
            res += e
            if count[e] > 1:
                res += str(count[e])
        
        return res

formula = "K4(ON(SO3)2)2"
print(Solution().countOfAtoms(formula))
            