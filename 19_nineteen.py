''' 

n = 2, o/p = 2
n = 4, o/p = 5

'''

n = int(input())

a = 1
r = 0
for i in range(n+1):
    t = r
    r += a
    a = t

print (r,end=' ')
