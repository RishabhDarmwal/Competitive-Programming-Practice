from collections import Counter
n=int(input())
lst=range(1,n+1)
a=list(map(int,input().split()))
cl=Counter(lst)
ca=Counter(a)
for i in ca:
    if ca[i]!=cl[i]:
        print("No")
        break
else:
    print("Yes")
    