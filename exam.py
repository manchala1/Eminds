def consequitive(arr,z):
    if z<=0 or z>len(arr):
        return 
    c=[]
    for i in range(len(arr)):
        c.append(len(arr[i]))
    if z==1:
        maxi=float('-inf')
        maxiIndex=-1
        for i in range(len(c)):
            if c[i]>maxi:
                maxi=c[i]
                maxiIndex=i
        return arr[maxiIndex]
    maxi=0
    for i in range(z):
        maxi=maxi+c[i]
    maxiIndex=0
    j=0
    maximum=float('-inf')
    maximum=max(maximum,maxi)
    for i in range(z-1,len(arr)-(z-1)):
        test=maxi+c[i]-c[j]
        if test>maximum:
            maxiIndex=i
            maximum=max(test,maximum)
        maxi=test
        j=j+1
    ans=''
    for i in range(maxiIndex,maxiIndex+z):
        ans=ans+arr[i]
    return ans

arr=["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"]
z=2
ans=consequitive(arr, z)
print(ans)