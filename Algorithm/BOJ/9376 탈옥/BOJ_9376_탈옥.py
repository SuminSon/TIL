import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline
def bfs01(i,j):
    visit = [[10 ** 5] * (w + 2) for _ in range(h + 2)]
    q = deque([])
    q.append((i,j))
    visit[i][j] = 0
    while q:
        vh,vw = q.popleft()
        for k in range(4):
            vhh, vww = vh + dh[k], vw + dw[k]
            if 0<=vhh<h+2 and 0<=vww<w+2:
                if maze[vhh][vww] == '#': # 문열기. 1소모
                    if visit[vhh][vww] > visit[vh][vw] + 1:
                        visit[vhh][vww] = visit[vh][vw] + 1
                        q.append((vhh,vww))
                elif maze[vhh][vww] == '*': # 못 감
                    pass
                else: # 빈칸 or 다른죄수. 0소모
                    if visit[vhh][vww] > visit[vh][vw]:
                        visit[vhh][vww] = visit[vh][vw]
                        q.appendleft((vhh,vww))
    return visit

def qSet():
    global pCount
    for i in range(h+2):
        for j in range(w+2):
            if maze[i][j] == '$':
                pCount += 1
                prisoner.append((i,j))
                if pCount > 1:
                    return

T = (int)(input())
for tc in range(T):

    h,w = map(int,input().split())
    maze = [['.']*(w+2) for _ in range(h+2)]
    for i in range(1,h+1):
        maze[i] = ['.'] + list(input().rstrip()) + ['.']

    pCount = 0
    prisoner = []
    qSet()

    # 상 좌 우 하 ... 반대 인덱스 합이 무조건 4됨
    dh,dw = [-1,0,0,1],[0,-1,1,0]
    visit1 = bfs01(prisoner[0][0],prisoner[0][1])
    visit2 = bfs01(prisoner[1][0],prisoner[1][1])
    visit3 = bfs01(0,0)

    answer = 10 ** 5
    for aa in range(h+2):
        for bb in range(w+2):
            d3Count = visit1[aa][bb] + visit2[aa][bb] + visit3[aa][bb]
            if maze[aa][bb] == '#': d3Count -= 2
            if answer > d3Count: answer = d3Count

    print(answer)




