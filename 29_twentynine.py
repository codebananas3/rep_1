'''
Input: 1 2 5

'''

n = int(input())
d = input().split()

print ()
for i in range(1,n+1):
    j = i
    ans = ''
    
    while True: 
        while int(d[2]) <= i:
            ans = ans + " " + (d[2])
            i -= int(d[2])
        while int(d[1]) <= i:
            ans = ans + " " + (d[1])
            i -= int(d[1])
        while int(d[0]) <= i:
            ans = ans + " " + (d[0])
            i -= int(d[0])

        if int(i) in ans.split() % 2 == 0:          #NEED TO BE UPDATED!
            print ("yes")
    
    print (j,f"-{ans}")