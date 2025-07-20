a = input().split()

t1 = int(a[0])
t2 = int(a[1])

if t1%2 == 0:
    p1 = t1+1
else:
    p1 = t1
    
while p1 <= t2:
    print (p1, end=' ')
    p1+=2