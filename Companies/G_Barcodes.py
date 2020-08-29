"""
Rules for barcode: the first pixel and last pixel must be black, and each color has at most 3 pixels.
Given a barcode that has X pixels, how many barcodes it can generate? X >= 3

b[i] is the number of barcodes of length i, ending with black pixel
w[i] is the number of barcodes of length i, ending with white pixel

Transition function:
b[i] = w[i-1] + w[i-2] + w[i-3]
w[i] = b[i-1] + b[i-2] + b[w-3]

Initial conditions: w[0] = 1 because only B can appear in first pixel

Final result b[X]
"""
def numBarcodes(X):
    if X < 3: return 0
    if X == 3: return 1
    b, w = [0]*(X+1), [0]*(X+1)
    w[0] = 1
    for i in range(1, X+1):
        b[i] = w[i-1]
        w[i] = b[i-1]
        if i > 1:
            b[i] += w[i-2]
            w[i] += b[i-2]
        if i > 2:
            b[i] += w[i-3]
            w[i] += b[i-3]

    print(b)
    print(w)
    return max(0, b[X])

print(numBarcodes(4))