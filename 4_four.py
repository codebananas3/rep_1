g = int(input())
k = g
sum = 0

while g > 0:
    rem = g % 10
    sum = rem + sum * 10
    g = int(g/10)

if sum == k:
    print ("Yes, Palindrome.")

else: 
    print ("Not a Palindrome.")