n = int(input())
ans = []
s = 999999999.0

for i in range(n):
    in1 = input().split(',')
    if (int(in1[1])*int(in1[2])/100) < s:
        s = (int(in1[1])*int(in1[2])/100)
        ans.append(in1[0]) 
        
for i in ans:
    print (i)