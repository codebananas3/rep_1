'''
iT'S THE IPL SEASON AND THE FIRST LEAGUE MATCH OF Dilip's fav team, CSK
The CSK team is playing at the IPL after 2 years and like all Dhoni lovers,
Dilip is also eagerly waiting to see Dhoni back in action.
After waiting in long queue, Dilip succeeded in getting the tickets for the big match
On the ticket, there is a letter code, that can be represented as a string of uppercase Latin letters.
Dilip believes that CSK will win the match in case exactly 2 different letter in the code alternate.
Otherwise, he believes that the team might lose.

Alternate coding:
You are given a ticket code, please determine whether the CSK team will win the match or not.
Print yes or no.

i/P: ababab
o/p: yes

i/P: abc
o/p: no

abab
'''

s = input()
l = []
k = []
l[:0] = s

if len(l) % 2 != 0:
    print ("No")

else:
    for i in s:
        if i not in k:
            k.append(i)

    if len(k) != 2:
        print ("No")
    else:
        print ("Yes")


'''
NOT THE FINAL ANSWER. NEEDS CHANGES. 
'''