from math import *
n=int(input())
sr=int(sqrt(n))
sum=1
for i in range(2,sr):
    if n%i==0:
        sum+=i
        sum+=n/i
if n==sum:
    print("True")
else:
    print("False")

# Perfect Number