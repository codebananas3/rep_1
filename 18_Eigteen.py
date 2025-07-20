'''
    I/P: Karunya
    O/P: Kaaruunyaa

'''

n = input()

for i in n:
    if i in ['A','E','I','O','U','a','e','i','o','u']:
        print (i+i,end='')
    else:
        print (i,end='')
