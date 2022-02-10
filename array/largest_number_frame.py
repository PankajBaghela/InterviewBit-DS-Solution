def largest_number(arr):
    lar_str=""
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            temp1=str(arr[i])+str(arr[j])
            temp2=str(arr[j])+str(arr[i])
            if int(temp1)>int(temp2):
                pass
            else:
                arr[i],arr[j]=arr[j],arr[i]
    
    for i in range(len(arr)):
        if arr[i]==0:
            return 0
        else:
            lar_str+=str(arr[i])
    return lar_str



a=[0,0,0,0,0]
print(largest_number(a))