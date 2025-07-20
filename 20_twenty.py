n = input()
k = []
s = []

for i in n:
    if i in k and i not in s:
        print (i,end='')
        s.append(i)
    else:
        k.append(i)
        
print (k)
print (s)