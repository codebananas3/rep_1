n = int(input())

for i in range(n):
    if i % 2 == 0:
        for j in range(1,n):
            print (i+1,end=' ')
        print (i+2,end=' ')
    else:
        print (i+2,end=' ')
        for j in range(1,n):
            print (i+1,end=' ')

    print ()