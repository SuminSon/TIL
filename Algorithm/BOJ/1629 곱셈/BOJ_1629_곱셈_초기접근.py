import sys
sys.stdin=open('input.txt')
input=sys.stdin.readline

# A,B,C 모두 2,147,483,647 이하의 자연수 ( 0 아님 )
A,B,C=map(int,input().split())

'''
(A**B)%C 를 구하는 문제입니다.
제곱할수록 수 자체가 기하급수적으로 커져서 계산이 힘듭니다.

이에 이전 항의 결과로 다음 항을 구했습니다.
B를 편의상 1로 두고 A%C=D0이라고 할 때, A=(A-D0)+D0 입니다.
이 때, (A-D0)%C==0 입니다.
이제 B가 1 증가한다고 가정하고 양변에 A를 곱합니다.
A**2 = A*(A-D0) + A*D0
이 때, A*(A-D0)는 여전히 %C==0 입니다.
그렇다면 이후 B가 1 증가했을 때의 나머지 D1을
D1= A*D0 %C 로 구할 수 있습니다.(이전 항의 결과로)

또한 나머지는 이전에 등장했던 나머지와 같은 값이 등장하면
계속 반복하는 성질을 지닙니다.(이후 같은 연산이 반복되므로)
따라서 이전에 등장한 나머지와 같은 값이 나온 시점에서 리스트 갱신을 멈춘 후,
B에 대응되는 나머지 값을 찾아 출력합니다.
'''
Dlist=[]
for b in range(B):
    if b==0:
        Dlist.append(A%C)
    elif(A*Dlist[b-1])%C in Dlist:
        break
    else:
        Dlist.append((A*Dlist[b-1])%C)
        print(Dlist)
print(Dlist[B%len(Dlist)])