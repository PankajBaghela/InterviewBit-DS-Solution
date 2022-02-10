def solve(A):
    maxn=A[0]
    minn=A[0]
    for i in A:
        if i>maxn:
            maxn=i
        if i<minn:
            minn=i
    print(maxn)
    print(minn)
    return (maxn+minn)
A=[-2,1,-4,5,3]
print(solve(A))
