a,b=map(int,input().split())
if abs(a-b)==1 or (a==10 and b==1) or (a==1 and b==10):
    print("Yes")
else:
    print("No")