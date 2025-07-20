'''
26 chaurs need to be arragedm , named from A TO Z, 
original number of alphabets needs to be arranged,
it is randomly arranged, find the number of chairs arranged correctly.

Test case 1:
I/P:  ABCDODCNEK
O/P: 4

I/P: ABKJFFGH
O/P: 5

'''

s = input()
a = 97 
count = 0

for i in range(len(s)):
    if ord(s[i].lower()) == a:
         count += 1 
    a += 1

print (count)