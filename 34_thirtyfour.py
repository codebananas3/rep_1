s = input()
a = input()
b = input()

for i in s:
    if i == a or i == b:
        if i == a:
            print (b,end='')
        
        if i == b:
            print (a,end='')

    else:
        print (i,end='')
