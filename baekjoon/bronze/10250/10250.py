T=int(input())
for t in range(T):
    h,m,n=map(int,input().split())
    if n%h==0:
        print("{:d}{:02d}".format(h,(n-1)//h+1))
    else:
        print("{:d}{:02d}".format(n%h,(n-1)//h+1))
        