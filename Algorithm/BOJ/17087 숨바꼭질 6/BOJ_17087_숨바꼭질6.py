import sys
sys.stdin=open('input.txt')

def GCD(A,B):
    C=A%B
    while C!=0:
        A,B=B,C
        C=A%B
    return B

# 숨바꼭질 6
# 현재 수빈이 위치 S와 각 동생들의 위치 A 간의 차이의 최대공약수를 구하는 문제

N,S=map(int,input().split())
distance=list(map(lambda x:abs(int(x)-S),input().split()))

if len(distance)==1:
    result=distance[0]
else:
    result=GCD(distance[0],distance[1])
    for d in range(2,len(distance)):
        x=GCD(result,distance[d])
        result=x
print(result)