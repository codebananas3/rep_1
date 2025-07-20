n = int(input())
o = 1

for i in range(n+1):
    for j in range(i):
        print ('#',end=' ')

    for k in range(n,i,-1):
        print (o,end=' ')
        o+=1 
    print ("/n",end='')
    for l in range(i):
        print ()


    print ()
