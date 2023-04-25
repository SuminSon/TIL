import sys
sys.stdin = open('input.txt')

N = int(input())
xy = []
for i in range(N):
    x,y = map(int,input().split())
    xy.append((x,y))

answer = 0
for i in range(N-2):
    x1, y1 = xy[i]
    for j in range(i+1,N-1):
        x2, y2 = xy[j]
        for k in range(j+1,N):
            x3, y3 = xy[k]
            a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
            b = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** (1 / 2)
            c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** (1 / 2)
            s = (a + b + c) / 2
            A = (s*(s-a)*(s-b)*(s-c)) ** (1 / 2)
            answer = max(answer,A)

print(f'{answer:.1f}')