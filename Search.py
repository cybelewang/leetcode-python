A = list(range(5))
print(A, sep=' ')

def BinarySearch(A, value):
    l = 0
    r = len(A) - 1
    while l <= r:
        mid = (l + r)//2
        if A[mid]==value:
            return mid
        elif A[mid]<value:
            l = mid + 1
        else:
            r = mid - 1
    return -1

print("The index of 1 is {}",BinarySearch(A, 1))