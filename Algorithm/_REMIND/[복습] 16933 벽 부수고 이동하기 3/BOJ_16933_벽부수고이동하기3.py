import sys
from collections import deque
sys.stdin = open('input.txt')

# 1% 메모리 초과 / 시간초과

N, M, K = map(int,input().split())
maps = [list(map(lambda x: (int)(x),input())) for _ in range(N)]

def bfs():
    visit = [[[10**7]*M for _ in range(N)] for _ in range(K+1)]
    visit[K][0][0] = 1
    q = deque([(0,0,True,1,K)])

    while q:
        i,j,day,dist,floor = q.popleft()
        # print(q)
        # print(f"i,j{i,j} | day {day} | dist {dist} | floor {floor}")
        # for k in range(K + 1):
        #     print(f"floor = {k}")
        #     for n in range(N):
        #         print(visit[k][n])
        #     print()
        # print("="*40)

        if (i,j) == (N-1, M-1):
            return visit[floor][i][j]

        for k in [(0,1),(-1,0),(1,0),(0,-1)]:
            di, dj = k
            ni, nj = i + di, j + dj

            # 이동 가능한 곳일 때
            if 0 <= ni < N and 0 <= nj < M:
                # 0이라 낮밤 상관없이 이동 가능
                if maps[ni][nj] == 0 and visit[floor][ni][nj] > dist + 1:
                    visit[floor][ni][nj] = dist + 1
                    q.append((ni, nj, not day, dist + 1, floor))
                # 1칸에 아직 부숴서 갈 수 있을 때,
                elif maps[ni][nj] == 1 and floor and visit[floor-1][ni][nj] > dist + 1:
                    # 낮이면 부수고 전진
                    if day:
                        visit[floor-1][ni][nj] = dist + 1
                        q.append((ni,nj,not day, dist + 1, floor - 1))
                    elif not day:
                        # 밤이면 대기타기 위해 그냥 멈추고
                        q.append((i, j, not day, dist + 1, floor))

answer = bfs()
print(answer) if answer else print(-1)

