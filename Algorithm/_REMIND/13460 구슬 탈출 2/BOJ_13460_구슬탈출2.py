import sys
from collections import deque
sys.stdin = open('input.txt')

def Solution():
    # 세로 N, 가로 M
    N,M = map(int,input().split())
    board = [list(filter(lambda x:x!='\n',input())) for _ in range(N)]
    q = deque([])
    R = B = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                R = (i,j)
                board[i][j] = '.'
            if board[i][j] == 'B':
                B = (i,j)
                board[i][j] = '.'
    visit = []
    q.append((R,B,0))
    dr = [[-1,1,0,0],[0,0,-1,1]]
    while q:
        r,b,turn = q.popleft()
        visit.append((r,b))
        ri, rj = r
        bi, bj = b

        if turn >= 10:
            continue;

        for k in range(4):
            R = B = 0
            is_b = is_r = is_success = is_fail = False
            i = 1;
            while True:
                bbi = bi + dr[0][k] * i
                bbj = bj + dr[1][k] * i
                rri = ri + dr[0][k] * i
                rrj = rj + dr[1][k] * i
                # 파란색이 들어가면 그 턴 무조건 실패
                if not is_b and board[bbi][bbj] == 'O':
                    is_fail = True
                    break
                # 파란색 안 들어간 상태에서 R이 들어가면 성공
                if not is_r and board[rri][rrj] == 'O':
                    is_success = True

                # 파란색이 벽에 충돌하면 멈추기
                if not is_b and board[bbi][bbj] == '#':
                    B = (bbi-dr[0][k],bbj-dr[1][k])
                    is_b = True
                # 빨간색이 벽에 충돌하면 멈추기
                if not is_r and board[rri][rrj] == '#':
                    R = (rri-dr[0][k],rrj-dr[1][k])
                    is_r = True

                # R과 B가 동시에 움직이기때문에 이런 처리가 가능

                # R과 충돌하면 거기서 멈춤
                if not is_b and (bbi,bbj) == R:
                    B = (bbi-dr[0][k],bbj-dr[1][k])
                    is_b = True

                # B와 충돌하면 거기서 멈춤
                if not is_r and (rri,rrj) == B:
                    R = (rri-dr[0][k],rrj-dr[1][k])
                    is_r = True

                if is_b and is_r:
                    break

                i += 1

            if is_fail:
                continue
            if is_success:
                print(turn + 1)
                return
            if (R,B) not in visit:
                q.append((R,B,turn+1))

    print(-1)

Solution()