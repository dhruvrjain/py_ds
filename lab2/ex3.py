ip=list(map(int,input().split()))
l=[]
for n in ip:
    if n==0:
        break
    l.append(n)
l.sort()
for i in l:
    print(i,end=" ")