"""
736 Parse Lisp Expression

You are given a string expression representing a Lisp-like expression to return the integer value of.

The syntax for these expressions is given as follows.

An expression is either an integer, a let-expression, an add-expression, a mult-expression, or an assigned variable. Expressions always evaluate to a single integer.
(An integer could be positive or negative.)
A let-expression takes the form (let v1 e1 v2 e2 ... vn en expr), where let is always the string "let", then there are 1 or more pairs of alternating variables and expressions, meaning that the first variable v1 is assigned the value of the expression e1, the second variable v2 is assigned the value of the expression e2, and so on sequentially; and then the value of this let-expression is the value of the expression expr.
An add-expression takes the form (add e1 e2) where add is always the string "add", there are always two expressions e1, e2, and this expression evaluates to the addition of the evaluation of e1 and the evaluation of e2.
A mult-expression takes the form (mult e1 e2) where mult is always the string "mult", there are always two expressions e1, e2, and this expression evaluates to the multiplication of the evaluation of e1 and the evaluation of e2.
For the purposes of this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter, then zero or more lowercase letters or digits. Additionally for your convenience, the names "add", "let", or "mult" are protected and will never be used as variable names.
Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for more details on scope.
Evaluation Examples:
Input: (add 1 2)
Output: 3

Input: (mult 3 (add 2 3))
Output: 15

Input: (let x 2 (mult x 5))
Output: 10

Input: (let x 2 (mult x (let x 3 y 4 (add x y))))
Output: 14
Explanation: In the expression (add x y), when checking for the value of the variable x,
we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
Since x = 3 is found first, the value of x is 3.

Input: (let x 3 x 2 x)
Output: 2
Explanation: Assignment in let statements is processed sequentially.

Input: (let x 1 y 2 x (add x y) (add x y))
Output: 5
Explanation: The first (add x y) evaluates as 3, and is assigned to x.
The second (add x y) evaluates as 3+2 = 5.

Input: (let x 2 (add (let x 3 (let x 4 x)) x))
Output: 6
Explanation: Even though (let x 4 x) has a deeper scope, it is outside the context
of the final x in the add-expression.  That final x will equal 2.

Input: (let a1 3 b2 (add a1 1) b2) 
Output 4
Explanation: Variable names can contain digits after the first character.

Note:

The given string expression is well formatted: There are no leading or trailing spaces, there is only a single space separating different components of the string, and no space between adjacent parentheses. The expression is guaranteed to be legal and evaluate to an integer.
The length of expression is at most 2000. (It is also non-empty, as that would not be a legal expression.)
The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.
"""
# similar problems: 224 Basic Calculator, 227 Basic Calculator II, 591 Tag Validator, 640 Solve the Equation, 722 Remove Comments
# my own recursive solution by splitting expressions to subwords, then evaluate them recursively
# to shadow the external variable's value, I used a variable map which holds a list of values. When entering an inner expression, we append value for the variable, and pop it when exiting the inner expression
class Solution:
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        variables = {}
        return self._evaluate(expression, variables)

    def _evaluate(self, expression, variables):
        """
        Evaluate current-level expression with variables' values from outside level.
        To shadow outside same-name variable, we append the local value to the end of the variable's value list, and pop out this value when exiting the function
        When looking for value of a variable, we always use the last value in the variable's value list
        """
        token = self.split(expression)
        start_word = token[0]
        local_variables = set()
        if start_word == 'let':
            for i in range(1, len(token)-1, 2):
                # token[i] is variable, token[i+1] is expression

                # evaluate the expression token[i+1]
                e = self._evaluate(token[i+1], variables)
                
                # check if variable token[i] in previous variables map, if so, shadow it by appending the local value
                v = token[i]
                if v in variables:
                    if v in local_variables:    # do not append but update the local value, this is to handle "(lex x 2 x 3 x 4 x)"
                        variables[v][-1] = e
                    else:
                        variables[v].append(e)
                        local_variables.add(v)
                else:
                    variables[v] = [e]
                    local_variables.add(v)

            # now evaluate the final value of the "let" statement
            res = self._evaluate(token[-1], variables)

        elif start_word == 'add':    
            # should have only two expressions
            res = self._evaluate(token[1], variables) + self._evaluate(token[2], variables)
        elif start_word == 'mult':
            res = self._evaluate(token[1], variables) * self._evaluate(token[2], variables)
        elif start_word in variables:   # assigned variable
            res = variables[start_word][-1]
        else:   # must be an integer
            res = int(start_word)

        # remove local variable's values from variables map
        for v in local_variables:
            variables[v].pop()
        
        return res
                        
    def split(self, expression):
        """
        split expression by whitespace and form a list, if a substring has parentheses, don't split it
        example: "(let x 2 (mult x 5))" will be splited to ["let", "x", "2", "(mult x 5)"]
        example: "x" will be splited to ["x"]
        intutiton: the left parenthesis count will tell the level, when left_parenthesis_count == 1, and there is a whitespace, it's time to append the substring
        also don't forget the last substring, which doesn't have a whitespace, but can be triggered by the last ')' or end of expression
        """
        left_parenthesis_count = 0
        token = []
        start= 0
        for i, e in enumerate(expression):
            if e == '(':
                left_parenthesis_count += 1
                if left_parenthesis_count == 1: # this is the starting '(' of the whole expression
                    start = i + 1   # do not include the starting '('
                elif left_parenthesis_count == 2:   # starts a sub-expression
                    start = i   # include the starting '('
            elif e == ')':
                left_parenthesis_count -= 1
                """ bug fixed: we don't need to check this condition because only whitespace or the last ')' will cause to append a substring
                if left_parenthesis_count == 1: # just leave a sub-expression
                    token.append(expression[start:i+1]) # push back the sub-expression, including the trailing ')'
                    start = i + 2
                elif left_parenthesis_count == 0: # this is the end ')' of the whole expression
                """
                if left_parenthesis_count == 0: # this is the end ')' of the whole expression
                    if start < i:   # bug fixed: should always check if the substring is empty
                        token.append(expression[start:i])   # do not include the end ')'
                    start = i + 1
            elif e == ' ' and left_parenthesis_count == 1:  # check if the whitespace is in the first level of expression, if not, do not split
                token.append(expression[start:i])
                start = i + 1

        # this will handle the expressions without "()"
        if start < len(expression):
            token.append(expression[start:])

        return token


expressions = ["(add 1 2)", "(let x 2 (mult x 5))", "(let x 2 (mult x (let x 3 y 4 (add x y))))", "(let x 3 x 2 x)", "(let x 1 y 2 x (add x y) (add x y))", "(let x 2 (add (let x 3 (let x 4 x)) x))", "(let a1 3 b2 (add a1 1) b2)"]
#expressions = ["(add (let x 3 (let x 4 x)) x)"]
obj = Solution()
for expression in expressions:
    print(expression, end = " = ")
    print(obj.evaluate(expression))