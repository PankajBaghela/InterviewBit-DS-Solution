def pelindrome(A):
    A=A.lower()
    s=""
    for i in range(len(A)):
        if 'a'<=A[i]<='z' or '0'<=A[i]<='9':
            s=s+A[i]
    left=0
    right=len(s)-1
    while left<right:
        if s[left]==s[right]:
            left+=1
            right-=1
        else:
            return 0
    return 1


a="A 9 man, a plan, a canal: Panam9a"
print(pelindrome(a))
