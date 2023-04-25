import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 상하좌우
dti = [-1,1,0,0]
dtj = [0,0,-1,1]

def ball_move(type:int, dir:int):
    global cnt
    if type == 0: # r b 순서
        ri, rj = red[0], red[1]
        dri, drj = ri + dti[dir], rj + dtj[dir]
        if 0 <= dri < N and 0 <= drj < M:
            next_can = board[dri][drj]
            cnt += 1
            while next_can == '.':
                board[ri][rj] = '.'
                board[dri][drj] = 'R'
                ri, rj = dri, drj
                dri, drj = ri + dti[dir], rj + dtj[dir]
            if next_can == 'O':
                return cnt
            elif next_can == '#' or next_can == 'B':
                ri, rj = blue[0], blue[1]
                dri, drj = ri + dti[dir], rj + dtj[dir]
                if 0 <= dri < N and 0 <= drj < M:
                    next_can = board[dri][drj]
                    while next_can == '.':
                        board[ri][rj] = '.'
                        board[dri][drj] = 'B'
                        ri, rj = dri, drj
                        dri, drj = ri + dti[dir], rj + dtj[dir]
                    if next_can == 'O' :
                        return -1
                    elif next_can == '#' or next_can == 'R':
                        return None
    else : # b r 순서
        ri, rj = blue[0],blue[1]
        dri, drj = ri + dti[dir], rj + dtj[dir]
        if 0 <= dri < N and 0 <= drj < M:
            next_can = board[dri][drj]
            cnt += 1
            while next_can == '.':
                board[ri][rj] = '.'
                board[dri][drj] = 'B'
                ri, rj = dri, drj
                dri, drj = ri + dti[dir], rj + dtj[dir]
            if next_can == 'O':
                return -1
            elif next_can == '#' or next_can == 'R':
                ri, rj = red[0], red[1]
                dri, drj = ri + dti[dir], rj + dtj[dir]
                if 0 <= dri < N and 0 <= drj < M:
                    next_can = board[dri][drj]
                    while next_can == '.':
                        board[ri][rj] = '.'
                        board[dri][drj] = 'R'
                        ri, rj = dri, drj
                        dri, drj = ri + dti[dir], rj + dtj[dir]
                    if next_can == 'O':
                        return cnt
                    elif next_can == '#' or next_can == 'B':
                        return None

N, M = map(int,input().split())
board = [list(input().replace('\n','')) for _ in range(N)]

red, blue = 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R': red = (i,j)
        elif board[i][j] == 'B': blue = (i,j)
cnt = 0
result = 0
for turn in range(4):
    if turn == 0: # 위로 옮기기. i 좌표가 작은 것부터 움직인다.
        if red[0] < blue[0]: result = ball_move(0,turn)
        else : result = ball_move(1,turn)
    elif turn == 1: # 아래로 옮기기. i 좌표가 큰 것부터 움직인다.
        if red[0] > blue[0]: result = ball_move(0,turn)
        else : result = ball_move(1,turn)
    elif turn == 2: # 왼쪽으로 옮기기. j 좌표가 작은 것부터 움직인다.
        if red[1] < blue[1]: result = ball_move(0,turn)
        else : result = ball_move(1,turn)
    elif turn == 3: # 오른쪽으로 옮기기. j 좌표가 큰 것부터 움직인다.
        if red[1] > blue[1]: result = ball_move(0,turn)
        else : result = ball_move(1,turn)

    if result == cnt : print(result)
    elif result > 10 : print(-1)

