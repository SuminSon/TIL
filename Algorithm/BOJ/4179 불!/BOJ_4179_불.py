import sys
import copy
from collections import  deque
sys.stdin = open('input.txt')

di,dj = [-1,1,0,0],[0,0,-1,1]

R,C = map(int,input().split())
maze = [list(input()) for _ in range(R)]
visited = copy.deepcopy(maze)

fires = deque([])
q = deque([])
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'F':
            fires.append((i,j))
            maze[i][j] = 0
            visited[i][j] = '.'
        elif maze[i][j] == 'J':
            q.append((i,j,0))
            maze[i][j] = '.'
            visited[i][j] = 0

is_can = False
while fires:
        fi, fj = fires.popleft()
        for k in range(4):
            fdii, fdjj = fi + di[k], fj + dj[k]
            if 0 <= fdii < R and 0 <= fdjj < C and maze[fdii][fdjj] == '.':
                fires.append((fdii,fdjj))
                maze[fdii][fdjj] = maze[fi][fj] + 1
while q:
        ji, jj, turn = q.popleft()
        if (ji == 0 or ji == R - 1 or jj == 0 or jj == C - 1) and (maze[ji][jj] == '.' or maze[ji][jj] > turn):
            is_can = True
            print(turn + 1)
            break
        for k in range(4):
            jdii, jdjj = ji + di[k], jj + dj[k]
            if 0 <= jdii < R and 0 <= jdjj < C:
                if visited[jdii][jdjj] == '.' :
                    visited[jdii][jdjj] = visited[ji][jj] + 1
                    q.append((jdii, jdjj, visited[jdii][jdjj]))

if not is_can: print('IMPOSSIBLE')
