n=int(input())
nums=set(range(1,n+1))
inp=set(map(int,input().split()))
print(list(nums-inp)[0])