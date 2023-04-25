import sys
sys.stdin=open('input.txt')
input=sys.stdin.readline

N,K=map(int,input().split())
num_list=[i for i in range(2,N+1)]
kcnt=0
result=num_list[0]
while kcnt<K:
    P=num_list.pop(0)
    result=P
    kcnt+=1
    if kcnt == K:
        break
    for n in num_list:
        if n%P==0:
            result=n
            kcnt += 1
            num_list.remove(n)
            if kcnt == K:
                break
print(result)