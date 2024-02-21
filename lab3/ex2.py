s1=input()
s2=input()
s3=input()
v=['a','e','i','o','u','A','E','I','O','U']
for i in v:
    s1=s1.replace(i,'"')
print(s1)
for i in s2:
    if i not in v:
        s2=s2.replace(i,"*")
print(s2)
s3=s3.upper()
print(s3)