s = input()

for i in range(len(s)):
    if i%2 != 0:
        print (int(s[i])*s[i-1],end='')