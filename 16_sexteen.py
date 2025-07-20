''' 
Given a maximum of 100 digit numbers as input, find the difference between sum of odd and even position digits.

Test case 1: 4567
Output: 2

Test case 2: 5476
Output: 2

Test case: 9834698765123
Output: 1

'''


n = (input())
o = 0
e = 0

for i in range(len(n)):
    if i % 2 == 0:
        o += int(n[i])

    else:
        e += int(n[i])

print ("Sum of odd:",o)
print ("Sum of even:",e)

print ("\nDifference: ",abs(o-e))