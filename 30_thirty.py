i = int(input())
s = [int(x) for x in (input().split())]

for i in range(len(s)-1):
    if s[i] > s[i+1]:
        s[i],s[i+1] = s[i+1],s[i]

for i in range(int((len(s))/2)):
    print (max(s),min(s),end=' ')
    s.remove(max(s))
    s.remove(min(s))