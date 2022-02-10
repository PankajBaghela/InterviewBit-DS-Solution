def reverse_str(strr):
    s=""
    temp=""
    i=len(strr)-1
    while i>=0:
        if strr[i]!=' ':
            temp+=strr[i]
            i-=1
        if strr[i]==' ':
            s+=temp[::-1]+strr[i]
            temp=''
            i-=1
    s+=temp[::-1]
    return s

s="the sky is blue"
print(reverse_str(s))
