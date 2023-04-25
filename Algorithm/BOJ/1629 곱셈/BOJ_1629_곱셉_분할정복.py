import sys
sys.stdin=open('input.txt')
input=sys.stdin.readline

def squdiv(A:int,B:int,C:int):
    if B==1:
        return A%C
    elif B%2==0:
        x = squdiv(A,B//2,C)
        return (x*x)%C
    elif B%2==1:
        x = squdiv(A,B//2,C)
        return (x*x*A)%C

# A,B,C 모두 2,147,483,647 이하의 자연수 ( 0 아님 )
A,B,C=map(int,input().split())
print(squdiv(A,B,C))
