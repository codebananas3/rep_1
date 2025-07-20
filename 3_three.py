g = int(input())
k = g
sum = 0

while g > 0:
    rem = g % 10
    sum += rem**3
    g = int(g/10)

if sum == k:
    print ("Yes, Armstrong.")

else: 
    print ("Not Armstrong.")