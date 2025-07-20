n = int(input())
s = input().split()
o = []
e = []


for i in range(n):
    if i%2 == 0:
        e.append(int(s[i]))
    if i%2 != 0:
        o.append(int(s[i]))
    
e = sorted(e)
o = sorted(o)

print (e[-2],o[-2])