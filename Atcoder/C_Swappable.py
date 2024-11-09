# from itertools import permutations
n=int(input())
nn=range(1,n+1)
A=list(map(int,input().split()))

ans=0
for i in A:
    for j in A:
        if i!=j and i<j:
            ans+=1
# for i in list(pairs):

#     if i[0]<i[1]  and i[0]!=i[1]:
#         #if i[0] in nn and i[0] in nn :
#             ans+=1

print(ans)
    
