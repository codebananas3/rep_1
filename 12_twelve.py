n = 5
for i in range(6):
    s = 0
    for j in range(6-i):
        print (" ",end=' ')
    for k in range(i):
        if k % 2 == 0:
            print (0,end=' ')
        else:
            print (1,end=' ')
    print ()
