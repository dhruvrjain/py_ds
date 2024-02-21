s=input().lower()
l=list(s)
anl=[]
for i in l:
    if i.isalnum():
        anl+=i
os="".join(anl)
if os==os[::-1]:
    print(1)
else:
    print(0)