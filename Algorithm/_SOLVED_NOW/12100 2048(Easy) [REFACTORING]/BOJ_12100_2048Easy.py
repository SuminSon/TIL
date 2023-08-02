import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

# 상하좌우
di,dj = [-1,1,0,0],[0,0,-1,1]
maxVal = 0

def dfs(dir, board, cnt):
    global maxVal

    if cnt == 5:
        for i in range(N):
            for j in range(N):
                if board[i][j] > maxVal:
                    maxVal = board[i][j]
        return

    if dir==0: # 위
        # 위로 쭉 당기고
        for j in range(N):
            for i in range(1,N):
                k = 1
                ii = i
                while True:
                    if 0 <= ii-k <N and board[ii-k][j] == 0:
                        board[ii-k][j] = board[ii][j]
                        board[ii][j] = 0
                        ii = ii-k
                    else: break

        # 한 번씩 합치고
        for j in range(N):
            for i in range(N-1):
                if board[i][j] == board[i+1][j]:
                    board[i][j] += board[i+1][j]
                    board[i+1][j] = 0
                    if board[i][j] > maxVal:
                        maxVal = board[i][j]

        # 위로 쭉 당기고
        for j in range(N):
            for i in range(1,N):
                k = 1
                ii = i
                while True:
                    if 0 <= ii-k <N and board[ii-k][j] == 0:
                        board[ii-k][j] = board[ii][j]
                        board[ii][j] = 0
                        ii = ii-k
                    else: break

    if dir == 1:  # 아래
        # 아래로 쭉 당기고
        for j in range(N):
            for i in range(N-2,-1,-1):
                k = 1
                ii = i
                while True:
                    if 0 <= ii + k < N and board[ii + k][j] == 0:
                        board[ii+k][j] = board[ii][j]
                        board[ii][j] = 0
                        ii = ii + k
                    else: break


        # 한 번씩 합치고
        for j in range(N):
            for i in range(N - 1,0,-1):
                if board[i][j] == board[i - 1][j]:
                    board[i][j] += board[i - 1][j]
                    board[i - 1][j] = 0
                    if board[i][j] > maxVal:
                        maxVal = board[i][j]

        # 아래로 쭉 당기고
        for j in range(N):
            for i in range(N-2,-1,-1):
                k = 1
                ii = i
                while True:
                    if 0 <= ii + k < N and board[ii + k][j] == 0:
                        board[ii+k][j] = board[ii][j]
                        board[ii][j] = 0
                        ii = ii + k
                    else: break

    if dir == 2:  # 왼쪽
        # 왼쪽으로 쭉 당기고
        for i in range(N):
            for j in range(1,N):
                k = 1
                jj = j
                while True:
                    if 0<=jj-k<N and board[i][jj - k] == 0:
                        board[i][jj-k] = board[i][jj]
                        board[i][jj] = 0
                        jj = jj - k
                    else: break

        # 한 번씩 합치고
        for i in range(N):
            for j in range(N-1):
                if board[i][j] == board[i][j+1]:
                    board[i][j] += board[i][j+1]
                    board[i][j+1] = 0
                    if board[i][j] > maxVal:
                        maxVal = board[i][j]

        # 왼쪽으로 쭉 당기고
        for i in range(N):
            for j in range(1,N):
                k = 1
                jj = j
                while True:
                    if 0<=jj-k<N and board[i][jj - k] == 0:
                        board[i][jj-k] = board[i][jj]
                        board[i][jj] = 0
                        jj = jj - k
                    else: break

    if dir == 3:  # 오른쪽
        # 오른쪽으로 쭉 당기고
        for i in range(N):
            for j in range(N-2,-1,-1):
                k = 1
                jj = j
                while True:
                    if 0<= jj+k<N and board[i][jj+k] == 0:
                        board[i][jj+k] = board[i][jj]
                        board[i][jj] = 0
                        jj = jj + k
                    else: break

        # 한 번씩 합치고
        for i in range(N):
            for j in range(N - 1,0,-1):
                if board[i][j] == board[i][j-1]:
                    board[i][j] += board[i][j-1]
                    board[i][j-1] = 0
                    if board[i][j] > maxVal:
                        maxVal = board[i][j]

        # 오른쪽으로 쭉 당기고
        for i in range(N):
            for j in range(N-2,-1,-1):
                k = 1
                jj = j
                while True:
                    if 0<= jj+k<N and board[i][jj+k] == 0:
                        board[i][jj+k] = board[i][jj]
                        board[i][jj] = 0
                        jj = jj + k
                    else: break

    # print(f'{dir} 방향 {cnt} 번째')
    # for b in board:
    #     print(b)

    for k in range(4):
        prev_board = [item[:] for item in board]
        dfs(k, board, cnt+1)
        board = prev_board

for k in range(4):
    prev_board = [item[:] for item in board]
    dfs(k, board, 0)
    board = prev_board

print(maxVal)
