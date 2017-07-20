def patternMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    m, n = len(s), len(p)
    match = [[False for x in range(m+1)] for y in range(n+1)]
    match[0][0] = True # empty always matches empty
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j] != "." and p[j] != "*":
                match[i][j] = match[i-1][j-1] and (s[i-1]==p[j-1])
            elif p[j] == ".":
                match[i][j] = match[i-1][j-1]
            else:
                # p[j] == "*"
                if p[j-1] != ".":
                    match[i][j] = match[i][j-2] or (match[i-1][j] and (s[i-1] == p[j-2]))
                else:
                    
