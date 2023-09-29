## 4sum
##brute 
arr = [-1 , -3 , -2, -2, 5, 1]
target = 2
n=len(arr)
a=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            for l in range(k+1,n):
                if arr[i]+arr[j]+arr[k]+arr[l]==target:
                    a.append([arr[i],arr[j],arr[k],arr[l]])
print(a)


##optimal
for i in range(n):
    for j in range(i+1,n):
        k=j+1
        l=n-1
        while(k<l):
            sumi = arr[i]+arr[j]+arr[k]+arr[l]
            if (sumi==target):
                a.append([arr[i],arr[j],arr[k],arr[l]])
                k+=1
                l-=1
            elif(sumi<target):
                k+=1
            else:
                l-=1
print(a)
