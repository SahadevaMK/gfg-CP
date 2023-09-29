s = 'we are python lovers'
a = s.split()
print(a)
b = a[::-1]
print(b)
c = ' '.join(b)
print(c)
## output of this above code is - lovers python are we


a = s.split()
b=[]
for i in a:
    b.append(i[::-1])
c = " ".join(b)
print(c)


## output of this above code is - ## output of this above code is -
