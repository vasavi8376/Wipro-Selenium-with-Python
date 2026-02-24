def make_it_equal(A, B):
    if A.count('%')!=1:
        return -1
    idx = A.index('%')

    prefix = A[:idx]
    suffix = A[idx+1:]
    if not B.startswith(prefix) or not B.endswith(suffix):
        return -1
    middle = B[len (prefix): len(B)-len(suffix)]
    return middle

A = input().strip()
B = input().strip()
print(make_it_equal(A,B))
