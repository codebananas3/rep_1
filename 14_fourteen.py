n = int(input())

if (n%2 != 0):
    print (2**int((n-1)/2))
else:
    print (3**int((n-1)/2))

#THE SERIES IS: 1 1 2 3 4 9 8 27 16 81 32 243...