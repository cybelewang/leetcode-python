def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    m, n = len(s), len(p)
    if m == 0:        
        match = [False for y in range(n+1)]
        match[0] = True
        for j in range(1, n+1):
            if p[j-1] == "*":
                match[j] = match[j-2]
        return match[n]

    match = [[False for y in range(n+1)] for x in range(m+1)] # match[i][j] means if s[0:i] matches p[0:j]
    
    match[0][0] = True; # empty always matches empty
    for j in range(2, n+1):
        if p[j-1] == "*":
            match[0][j] = match[0][j-2]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] != "." and p[j-1] != "*":
                match[i][j] = match[i-1][j-1] and (s[i-1] == p[j-1])
            elif p[j-1] == ".":
                match[i][j] = match[i-1][j-1]
            else:
                if j >= 2:  
                    matchZeroOccurance = match[i][j-2]                  
                    if p[j-2] == ".":
                        matchOnceOccurance = match[i][j-1]
                        matchMultiOccurance = match[i-1][j]# and (s[i-1] == s[i-2])
                    else:
                        matchOnceOccurance = match[i][j-1] and (s[i-1] == p[j-2])
                        matchMultiOccurance = match[i-1][j] and (s[i-1] == p[j-2])
                    match[i][j] = matchZeroOccurance or matchOnceOccurance or matchMultiOccurance

    return match[m][n]  
            
test_case = [("",""),("","a*"),("",".*"),("",".*.*"),("abcd","abc*d"),("abcc","abc*"),("ab","abc*"),("abc",".*cd"),("aa","a"),("aaa","aa"),("aa",".*"),("ab",".*"),("aab","c*a*b")]
for (s, p) in test_case:
    print(s + " matches "+ p + ": ", isMatch(s,p))                