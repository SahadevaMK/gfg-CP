arr = [1, 1, 0, -1, -2]
n = len(arr)
a=[]
for i in range(len(arr)):
    j = i+1
    k=n-1
    while(j<k):
        sumi = arr[i]+arr[j]+arr[k]
        if (sumi<0):
            j+=1
        elif(sumi>0):
            k-=1
        else:
            a.append([arr[i],arr[j],arr[k]])
            j+=1
            k-=1
print(a)
// brute

arr = [1, 1, 0, -1, -2]
n = len(arr)
a = []
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if (arr[i]+arr[j]+arr[k]==0):
                a.appprint(aend([arr[i],arr[j],arr[k]])
print(a)
