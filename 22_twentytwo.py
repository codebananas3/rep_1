s = []

s.append(input())
s.append(input())
s.append(input())

for i in s[0]:
    if i in ['A','E','I','O','U','a','e','i','o','u']:
        print ("*",end='')

    else:
        print (i,end='')

for i  in s[1]:
    if i not in ['A','E','I','O','U','a','e','i','o','u'] and i not in '1234567890':
        print ("@",end='')
    else:
        print (i,end='')

for i in s[2]:
    print (i.upper(),end='')

''' 

the first word: all vowels should be replaced by *
the second word should be changed like: all the consonants should be replaced by @
third character: all characters should be changed to uppercase, then concatenate the three words and print them.

Test case 1: 
I/P: how are you
O/P: h*wa@eYOU

Test case 2:
I/P: how 999 you
O/P: h*w999YOUa

'''