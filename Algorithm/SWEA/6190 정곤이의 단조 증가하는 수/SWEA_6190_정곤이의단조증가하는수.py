import sys
sys.stdin=open('input.txt')

# 단조 여부 판단 함수
def is_danzo(num:int):
    while num>0:
        if num%10<(num//10)%10:
            return False
        num=num//10
    return True

# 부분 집합의 곱 확인 함수
def dfs(elem=[],start=0,k=2):
    global result
    if k==0: # elem에 두 개의 인덱스 조합 완성 시,
        AiAj=A[elem[0]]*A[elem[1]]
        # 단조 증가하며 기존 값보다 클 때 갱신
        if AiAj>result and is_danzo(AiAj):
            result=AiAj
        return
    for i in range(start,len(A)):
        elem.append(i)      # 값 하나 elem에 넣고
        dfs(elem,i+1,k-1)   # 다음 값 넣으러 간다. k(남은 원소 개수)는 -1
        elem.pop()          # 확인 끝내고 나왔으니 기존값 빼고 for문 돌아서 다음 값 넣음

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    A=list(map(int,input().split()))
    for a in A:
        print(a,is_danzo(a))
    result=-1   # 단조 증가 수 없을 때 -1 출력
    dfs([])
    print(f'#{tc} {result}')
