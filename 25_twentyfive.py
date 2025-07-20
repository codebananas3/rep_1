'''

Given an array, array of n integers,
the task to rewrite the array by putting all the multiples of 10
at the end of the given array.

Test case:
n = 9
10 12 5 40 30 7 50 9 10
O/P: 12 5 7 9 10 40 30 50 10

'''

r = input().split()

for i in r:
    if int(i) % 10 != 0:
        print (i,end=' ')

for i in r:
    if int(i) % 10 == 0:
        print (i,end=' ')