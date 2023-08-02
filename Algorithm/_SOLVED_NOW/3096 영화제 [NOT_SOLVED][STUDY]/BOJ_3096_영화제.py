import sys
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 1000번 냅다 비트로 밀어버리는게 맞는건지? 인덱스 에러가 계속 발생합니다.
# 비트마스킹에 대해 학습 후 수정 요망

# 3096 영화제
# N: 마을 수 M: 배의 수
# 마을은 왼쪽 N개, 오른쪽 N개, 넘버링 1~N
# 왼쪽 오른쪽 마을 연결하는 배 M개, 양방향
# 4개 마을에서 영화제 개최. 왼2 오2. 왼마을은 모두 오른 마을과 배로 직접 연결되어야 한다.
# 개최 마을 고르는 방법의 수

N, M = map(int,input().split())

# 해당 값에 비트가 몇 개 있는지 기록하는 배열. 2**20까지 기록합니다.
# i & 1 => 해당 i 값과 1비트를 비교합니다
# Ones[i>>1]을 통해 i값의 1 이후 비트를 한칸씩 땡겨옵니다.
# 그리고 기존에 기록해둔 Ones 개수를 비교하여 더해주며 기록합니다.
bitNum = [0] * (1 << 20)
for i in range(1 << 20):
    bitNum[i] = (i & 1) + bitNum[i >> 1]

# 아이디어 1
# 왼쪽 마을에 대해 오른쪽 마을과 이어진 여부를 비트마스킹으로 표기한 테이블 구성
# 이후 L1 L2를 골라 비트마스킹 & 연산을 진행해 1bit이 2개 이상 나오면 경우의 수에 합산

LRtable= [0] * (N)
for i in range(M):
    l,r = map(int,input().split())

    # 오른쪽 마을 넘버 비트를 1로 변경
    LRtable[l-1] |= (1<<(r-1))

print(LRtable)

answer = 0
for l1 in range(N):
    for l2 in range(l1):
        S = LRtable[l1] & LRtable[l2]
        rCount = bitNum[S]
        if rCount > 1:
            # 오른쪽 마을 2개가 조건을 만족한다면 경우의 수를 세어봅시다
            answer += (rCount * (rCount-1)) // 2

print(answer)

