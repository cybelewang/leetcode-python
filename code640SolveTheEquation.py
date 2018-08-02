"""

Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
"""
# similar problems: 224, 227 calculator
class Solution:
    def solveEquation_OJBest(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        x, n, side = 0, 0, 1
        
        for eq, sign, num, isx in re.findall(r'(=)|([-+]?)(\d*)(x?)', equation):
            if eq:
                side = -1
            elif isx:
                x += side*int(sign+'1')*int(num or 1)
            elif num:
                n -= side*int(sign+num)
        
        return 'x=%d' % (n/x) if x else 'No solution' if n else 'Infinite solutions' 
    # my own solution with bug fixed
    # don't forget the case 'x', '-x'
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        if equation.count('=') != 1:
            return 'No solution'
        
        index = equation.find('=')
        left, right = equation[:index]+'+', equation[index+1:]+'+'  # append a '+' to avoid missing calculating the last number or x
        a, b = self.simplify(left)
        c, d = self.simplify(right)

        if a == c and b == d:
            return "Infinite solutions"
        elif a == c:
            return "No solution"
        else:
            return "x="+str((d-b)//(a-c))

    def simplify(self, expression):
        """
        simplify an expression to ax+b form
        return a, b
        """
        a, b = 0, 0
        i = 0
        for j in range(1, len(expression)):
            if expression[j] in ('+', '-'):
                if expression[j-1] == 'x':  # bug fixed: missed cases 'x', '+x' and '-x', which corresponds to '', '+', and '-'
                    e = expression[i:j-1]
                    if e == '+' or e == '':
                        a += 1
                    elif e == '-':
                        a -= 1
                    else:
                        a += int(e)
                else:
                    b += int(expression[i:j])
                i = j

        return (a, b)

equations = ['', '-x', 'x=-x', '1=2', '2x+3x-6x=x+2', 'x=x']
obj = Solution()
for e in equations:
    print(obj.solveEquation(e))
