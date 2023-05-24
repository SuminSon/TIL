import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = (int)(input())
for tc in range(T):

    h,w = map(int,input().split())
    maze = [list(input().rstrip()) for _ in range(h)]

    q1, q2 = deque([]), deque([])
    visit1 = [[9]*w for _ in range(h)]
    visit2 = [[10**2]*w for _ in range(h)]
    pCount = 0
    answer = 0
    answer1, answer2 = 10**8,10**8
    route1, route2 = [],[]

    def qSet():
        global pCount
        for i in range(h):
            for j in range(w):
                if maze[i][j] == '$':
                    pCount += 1
                    if pCount == 1:
                        q1.append((i,j,[(i,j)]))
                        visit1[i][j] = 0
                    else:
                        q2.append((i,j,[(i,j)]))
                        visit2[i][j] = 0
                        return
    qSet()

    # 상 좌 우 하 ... 반대 인덱스 합이 무조건 4됨
    dh,dw = [-1,0,0,1],[0,-1,1,0]
    while q1:
        vh,vw, route = q1.popleft()
        for k in range(4):
            vhh, vww = vh + dh[k], vw + dw[k]
            if 0<=vhh<h and 0<=vww<w:
                if maze[vhh][vww] == '#': # 문열기. 1소모
                    if visit1[vhh][vww] > visit1[vh][vw] + 1:
                        visit1[vhh][vww] = visit1[vh][vw] + 1
                        q1.append((vhh,vww, route+[(vhh,vww)]))
                elif maze[vhh][vww] == '*': # 못 감
                    pass
                else: # 빈칸 or 다른죄수. 0소모
                    if visit1[vhh][vww] > visit1[vh][vw]:
                        visit1[vhh][vww] = visit1[vh][vw]
                        q1.appendleft((vhh,vww, route+[(vhh,vww)]))
            else: # 탈출 성공
                if answer1 > visit1[vh][vw]:
                    answer1 = visit1[vh][vw]
                    oh1, ow1 = vh,vw
                    route1 = route[:]
                    print("뤁!! " , route1)


    for r in route1:
        vh,vw = r
        if maze[vh][vw] == '#':
            maze[vh][vw] = '.'

    for a in range(h):
        print(maze[a])

    while q2:
        vh,vw, route = q2.popleft()
        for k in range(4):
            vhh, vww = vh + dh[k], vw + dw[k]
            if 0<=vhh<h and 0<=vww<w:
                if maze[vhh][vww] == '#': # 문열기. 1소모
                    if visit2[vhh][vww] > visit2[vh][vw] + 1:
                        visit2[vhh][vww] = visit2[vh][vw] + 1
                        q2.append((vhh,vww, route+[(vhh,vww)]))
                elif maze[vhh][vww] == '*': # 못 감
                    pass
                else: # 빈칸 or 다른죄수. 0소모
                    if visit2[vhh][vww] > visit2[vh][vw]:
                        visit2[vhh][vww] = visit2[vh][vw]
                        q2.appendleft((vhh,vww, route+[(vhh,vww)]))
            else: # 탈출 성공
                if answer2 > visit2[vh][vw]:
                    answer2 = visit2[vh][vw]
                    route2 = route


    print(answer1, answer2)
    # print(len(doors))

