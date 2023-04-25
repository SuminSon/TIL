import sys
sys.stdin=open('input.txt')

#9020 골드바흐의 추측
T=int(input())
for t in range(T):
    N=int(input())
    prime=[i for i in range(2,N)]
    i,j=0,0
    while i<len(prime):
        j=i+1
        while j<len(prime):
           if prime[j]%prime[i]==0:
               prime.pop(j)
           j+=1
        i+=1

    n,nn=prime[len(prime)//2],prime[len(prime)//2]
    while n+nn!=N:
        if n+nn>N:
            nn=prime[len(prime)//2-1]
        if n+nn<N:
            n=prime[len(prime)// 2 +1]
            continue
        else:
            break
    print(nn,n)

'''
# 에라토스테네스의 체
i=0
while i<len(np):
    p=np[i]
    j=i+1
    while j<len(np):
        if np[j]%p==0:
            np.pop(j)
        j+=1
    i+=1

# 골드바흐 추측
is_gold=False
for n in nums:
    for nn in np:
        if n-nn in np:
            print(f'{n} = {nn} + {n-nn}')
            is_gold=True
            break
    if not is_gold:
        print("Goldbach's conjecture is wrong.")
'''
