a = [1,2,3,4,5,6]
b = [2,4,6,7]
u = []
n = len(a)
m = len(b)
i,j = 0,0
while(i<n and j<m):
    if (a[i]<b[j]):
        i+=1
    elif(b[j]<a[i]):
        j+=1
    else:
        u.append(a[i])
        i+=1
        j+=1
print(u)
