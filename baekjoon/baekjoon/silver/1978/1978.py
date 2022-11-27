N=int(input())
cnt=0
num=list(map(int,input().split()))
for i in num:
    j=2
    while j<i:
        if i%j==0:
            break
        j+=1
    if j==i:
        cnt+=1
print(cnt)
        