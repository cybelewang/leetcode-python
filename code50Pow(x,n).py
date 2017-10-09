"""
Implement pow(x, n).

"""
# Divide and conquer
# Ask if n can be negative
def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    my_dict = {}

    def _pow(x, m, my_dict):
        if m in my_dict:
            return my_dict[m]
        else:
            if m == 0:
                my_dict[0] = 1.0 
                return 1.0               
            elif m == 1:
                my_dict[1] = x
                return x
            else:
                a = _pow(x, m//2, my_dict)
                b = _pow(x, m - m//2, my_dict)
                c = a * b
                my_dict[m] = c
                return c
    if n < 0:
        return 1.0/_pow(x, -n, my_dict)
    else:
        return _pow(x, n, my_dict)

test_cases = [(1.0, 10), (2.0, 10), (0.0, 200)]
for case in test_cases:
    print(str(case[0])+'^'+str(case[1]), end = ' = ')
    print(myPow(case[0], case[1]))
