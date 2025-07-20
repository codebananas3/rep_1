a = input().split()

t1 = int(a[0])
t2 = int(a[1])

n = 5
d = (t2 - t1)/(n - 1)

for i in range(n):
    print (int(t1), end = ' ')
    t1 += d