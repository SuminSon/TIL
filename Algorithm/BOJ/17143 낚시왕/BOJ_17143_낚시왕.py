import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

R, C, M = map(int, input().split())
fspot = [[(0, 0, 0)] * C for _ in range(R)]
# print(fspot)
for _ in range(M):
    # (r,c) 위치
    # s 속력, d 이동방향, z 크기
    r, c, s, d, z = map(int, input().split())
    fspot[r - 1][c - 1] = (s, d, z)

answer = 0
visit = [[0] * C for _ in range(R)]
meetSharks = defaultdict(list)


# 낚시왕이 한칸 움직이고 상어픽업
def pickupShark(turn: int):
    global answer, visit, meetSharks
    if turn >= C:
        return

    for r in range(R):
        if fspot[r][turn] != (0, 0, 0):
            answer += fspot[r][turn][2]
            fspot[r][turn] = (0, 0, 0)
            break

    visit = [[0] * C for _ in range(R)]
    meetSharks = defaultdict(list)
    moveShark()
    pickupShark(turn + 1)


def setShark(r, c):
    global visit
    s, d, z = fspot[r][c]
    fspot[r][c] = (0, 0, 0)

    if d == 1 or d == 2:  # 위 아래
        if d == 1:
            nr, nd, rr, ss = r - s, 1, r, s
        elif d == 2:
            nr, nd, rr, ss = r + s, 2, r, s
        while not 0 <= nr < R:
            if nr < 0:
                rr, ss = 0, -nr
                nr, nd = abs(ss), 2
            if nr >= R:
                rr, ss = R - 1, ss - ((R - 1) - rr)
                nr, nd = rr - ss, 1
        meetSharks[(nr, c)].append((s, nd, z))

    elif d == 3 or d == 4:  # 오른 | 왼
        if d == 3:
            nc, nd, cc, ss = c + s, 3, c, s
        elif d == 4:
            nc, nd, cc, ss = c - s, 4, c, s
        while not 0 <= nc < C:
            if nc < 0:
                cc, ss = 0, -nc
                nc, nd = abs(ss), 3
            if nc >= C:
                cc, ss = C - 1, ss - ((C - 1) - cc)
                nc, nd = cc - ss, 4
        meetSharks[(r, nc)].append((s, nd, z))


# 1초동안 상어들이 움직임
# 같은 칸에 접하게 된 상어들은 별도기록
def moveShark():
    for r in range(R):
        for c in range(C):
            if fspot[r][c] != (0, 0, 0) and visit[r][c] == 0:
                setShark(r, c)
    killShark()


def killShark():
    for ij in meetSharks:
        i, j = ij
        for s in meetSharks[ij]:
            if fspot[i][j][2] < s[2]:
                fspot[i][j] = s


pickupShark(0)
print(answer)