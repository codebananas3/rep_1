i = input()

for n in range(int((len(i)+1)/2)):
    if (n+1) != int((len(i)+1)/2):
        print (n*' '+i[n]+' '*(len(i)-n-4)+' '*(len(i)-n-3)+i[len(i)-n-1])
    
    else:
        print ((n)*' '+i[n])

for n in range(1,int((len(i)+1)/2)):
    #print ((int((n+1)/2)-n)*' '+i[int((n+1)/2)-n]+' '*(len(i)-n-2)+' '*(len(i)-n-2)+i[int((n+1)/2)+n])
    print (' '*(int((len(i)+1)/2)-1-n)+i[int((len(i)+1)/2)-1-n]+' '*n+' '*(n-1)+i[int((len(i)+1)/2)-1+n])