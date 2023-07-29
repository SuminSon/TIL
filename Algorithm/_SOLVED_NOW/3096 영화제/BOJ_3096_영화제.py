import sys
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 3096 영화제
# N: 마을 수 M: 배의 수
# 마을은 왼쪽 N개, 오른쪽 N개, 넘버링 1~N
# 왼쪽 오른쪽 마을 연결하는 배 M개, 양방향
# 4개 마을에서 영화제 개최. 왼2 오2. 왼마을은 모두 오른 마을과 배로 직접 연결되어야 한다.
# 개최 마을 고르는 방법의 수

N, M = map(int,input().split())


# 아이디어 1
# 왼쪽 마을에 대해 오른쪽 마을과 이어진 여부를 비트마스킹으로 표기한 테이블 구성
# 이후 L1 L2를 골라 비트마스킹 & 연산을 진행해 1bit이 2개 이상 나오면 경우의 수에 합산

# 3% 시간초과

LRtable= [0] * (N+1)
for i in range(M):
    l,r = map(int,input().split())

    # 오른쪽 마을 넘버 비트를 1로 변경
    LRtable[l] |= (1<<r)

answer = 0
for k in combinations([i for i in range(1,N+1)],2):
    l1,l2 = k
    S = LRtable[l1] & LRtable[l2]
    if S > 0:
        rCount = 0
        for r in range(1,N+1):
            if S & (1 << r): rCount += 1
        if rCount > 1:
            # 경우의 수를 세어봅시다
            answer += len(list(combinations([i for i in range(rCount)],2)))

print(answer)