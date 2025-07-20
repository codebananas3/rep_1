'''
There is a meeting room in a firm.
There are n meetings in the form of (start(i),end(i))
Start(i) is the start time of the meeting, 
End(i) is the finish time of the meeting.

What is the maximum number of meetings that can be accomodated in the meeting room
when only 1 meeting can be held in the meeting room at a particular time.

'''

n = int(input())

st = [int(x) for x in (input().split())]
et = [int(x) for x in (input().split())]

mt = {st[0]:et[0]}
mtc = mt
for i in range(1,n):
    for j in mt.keys():
        if (st[i] < j and et[i] < mt[j]) or (st[i] > j and et[i] > mt[j]):
            mt[st[i]] = et[i]

print(mt)
