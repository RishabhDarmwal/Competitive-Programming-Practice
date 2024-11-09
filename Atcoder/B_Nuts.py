n=int(input())
A=list(map(int,input().split()))
nuts=0
for i in A:
    if i>10:
        nuts+=i-10
print(nuts)