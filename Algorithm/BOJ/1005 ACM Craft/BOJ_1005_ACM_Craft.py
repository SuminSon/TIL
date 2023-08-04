import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = (int)(input())

for tc in range(T):
    N, K = map(int,input().split())
    Dn = list(map(int,input().split()))
    prevNeed = [[] for _ in range(N + 1)]

    # 위상정렬
    # tTable[건물 번호] = 도달 정점 개수
    tTable = [0]*(N+1)
    for _ in range(K):
        x, y = map(int,input().split())
        prevNeed[y].append(x)
        tTable[y] += 1
    W = (int)(input())

    # 위상 정렬 시작을 위한 초기값 큐에 넣기
    # 해당 건물이 완성될 수 있는 최소 시간을 기록하는 dp 테이블
    # 선행 건물이 없는 경우 해당 건물 완성 시간 = 최소 시간
    q = deque([])
    dp = [0]*(1+N)
    for i in range(1,N+1):
        if tTable[i] == 0:
            q.append(i)
            dp[i] = Dn[i-1]

    # v가 나오는 순서 = 위상 정렬 순서
    # 해당 문제에서는 전체 순서보다는 W를 지을때까지의 시간 기록 후 결과가 필요
    # 해당 건물이 완성되는 시점에서 break
    # 이전 건물 완성 후 해당 건물 짓기까지의 시간의 최댓값을 기록한다
    while q:
        v = q.popleft()
        if v == W and tTable[v] == 0:
            break

        for p in range(1,N+1):
            if v in prevNeed[p]:
                prevNeed[p].remove(v)
                tTable[p] -= 1
                if tTable[p] == 0:
                    q.append(p)
                # 하나의 건물이 생성될 때 마다
                # 그 건물 생성 후 p 건물 생성 코스트를 합한게 최대가 되도록 기록
                dp[p] = max(dp[p], Dn[p-1] + dp[v])
    print(dp[W])
