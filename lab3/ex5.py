s=input()
d=dict()
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    if d[i]>1:
        print(i+":"+str(d[i]))