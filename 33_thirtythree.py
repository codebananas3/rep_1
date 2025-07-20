s = input()
r = input()
dic = {}

for i in s:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1
    
key_max = max(zip(dic.values(),dic.keys()))[1]

for k in s:
    if k == key_max:
        print (r,end='')
    else:
        print (k,end='')