M=int(input())
N=int(input())
so=list()
for i in range(M,N+1): #i엔 m부터 n까지의 숫자가 들어간다
    error=0
    for j in range(2,int(i**(1/2))+1): #j에는 i의 제곱근+1부터 2까지 차례로 들어간다
        if i%j==0: #i가 특정 숫자로 나누어 떨어지면 소수가 아니다
            error=1
            break
    if error==0:
        so.append(i)
if 1 in so:
    so.remove(1)
if len(so)==0:
    print(-1)
else:
    print(sum(so),so[0],sep='\n')
