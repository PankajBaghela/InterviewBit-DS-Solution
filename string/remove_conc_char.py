def rem_cons_char(A,B):
    s=""
    i=0
    while i<len(A):
        if A[i:i+B]==A[i]*B:
            i=i+B
            continue
        s=s+A[i]
        i=i+1
    return s

a="aabbccd"
b=2
print(rem_cons_char(a,b))
