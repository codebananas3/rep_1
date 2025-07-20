'''
Test case 1:
I/P: 5
O/P: 10 20 30 40 50 

I/P: 2
O/P: 40 50 10 20 30

Test case 2:
I/P: 4
O/P: 10 20 30 40

I/P: 1
O/P: 40 10 20 30

'''

arr = input().split()
n = int(input())

for i in range(n+2,len(arr)+1):
    print (arr[i-1], end=' ')

for i in range(len(arr)-n):
    print (arr[i], end=' ')

