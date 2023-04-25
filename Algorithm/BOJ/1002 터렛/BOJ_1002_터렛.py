import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    x1,y1,r1,x2,y2,r2= map(int,input().split())
    if r1 < r2 :
        x1,y1,r1,x2,y2,r2 = x2,y2,r2,x1,y1,r1

    d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)

    if d == 0 and r1 == r2: print(-1)
    elif r1+r2 < d or r1 > d + r2 : print(0)
    elif r1+r2 == d or r1 == d+r2 : print(1)
    elif r1+r2 >d or d < r1 < d+r2: print(2)

   # print(x1,y1,r1)
   # print(x2,y2,r2)