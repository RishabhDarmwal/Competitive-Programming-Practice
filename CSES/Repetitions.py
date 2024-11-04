s=input()
ans=0
n=len(s)
count=0
current=s[0]
for i in range(0,n):
    #print(f"Before Iteration {i+1}, ans {ans} count {count} current {current}")
    if s[i]==current:
        count+=1
        if count>ans:ans=count
    else:
        if count>ans:ans=count
        count=1
        current=s[i]
    #print(f"After Iteration {i+1}, ans {ans} count {count} current {current}")
    
print(ans)