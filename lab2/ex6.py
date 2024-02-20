n=input()
d=dict()
for c in n:
    d[c]=d[c]+1
dk=list(d.values())
print(dk)
if dk.count(dk[0])==len(dk):
    print("Stable")
else:
    print("Unstable")