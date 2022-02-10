def pairwithgiven_diif(A,B):
    a=set()
    for i in A:
        if i-B in a or i+B in a:
            return 1
        else:
            a.add(i)
    return 0
a=[-10,20]
print(pairwithgiven_diif(a, 30))