"""
Write a function that splits long SMS string into smaller pieces. 
Each piece should be less than or equal to 60 characters and contains indices at the end. Function should not break words into pieces. 
If word does not fit -- it should go to the next SMS.

Assume the final paragraphs < 10.
"""
def formatWords(sms, max_width):
    res = []
    paragraph = []
    cur = 0
    for word in sms.split():
        if cur + len(word) + 6 <= max_width:
            paragraph.append(word)
            cur += len(word) + 1
        else:
            res.append(' '.join(paragraph))
            paragraph = [word]
            cur = len(word) + 1
    
    res.append(' '.join(paragraph))

    total = len(res)
    for line in range(total):
        res[line] += " ({0}/{1})".format(line+1, total) 
    return res

sms = "Write a function that splits long SMS string into smaller pieces. Each piece should be less than or equal to 60 characters and contains indices at the end. Function should not break words into pieces. If word does not fit -- it should go to the next SMS."
max_width = 60
print(formatWords(sms, max_width))