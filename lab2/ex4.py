email=input()
# start=email.index('@')
start=0
for i in range(len(email)):
    if email[i]=='@':
        start=i
# end=email.index('.')
for i in range(start,len(email)):
    if email[i]=='.':
        end=i
print(email[start+1:end])