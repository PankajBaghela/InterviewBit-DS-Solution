def pick_from_both(arr,k):
    res=sum(arr[:k])
    summ=res
    for i in range(k):
        summ=summ-arr[k-1-i]
        summ=summ+arr[len(arr)-1-i]
        res=max(res, summ)
    return res






if __name__=="__main__":
    A=[5,-2,3,1,2]
    B=4
    res=pick_from_both(A,B)
    print(res)