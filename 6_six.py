g = int(input())
k = g
sum = 0

while g > 0:
    rem = g % 10
    sum += rem
    g = int(g/10)

print (sum)