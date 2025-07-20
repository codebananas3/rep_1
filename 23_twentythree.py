'''

Given N, the number of non-parallel lines,
the task to find the maximum number of regions in which
these lines can divide a plane

Test case 1: 
I/P: N = 3
O/P: 7

I/P: N = 2
O/P: 4

'''

s = 1
k = []
for i in range(1,12):
    s += i
    k.append(s)

n = int(input())
print (k[n-1])
