import sys
sys.stdin = open('input.txt')

A,B,C = map(int,input().split())
X1,X2,Y1,Y2 = map(int,input().split())

# x1 x2 구간에서... 이 직선의 x1 x2 구간 양끝점을 이은 선분이
# y1 직선 or y2 직선 두 개 중 하나와 교차한다면 poor
# 둘 다 교차하지 않으면 lucky
'''
if B == 0:
    if min(X1,X2) < -(C/A) < max(X1,X2):
        print('Poor')
    else:
        print('Lucky')
else:
    Yon1 = -(A/B)*X1 - (C/B)
    Yon2 = -(A/B)*X2 - (C/B)
    if (max(Y1,Y2) <= Yon1 and max(Y1,Y2) <= Yon2) or (min(Y1,Y2) >= Yon1 and min(Y1,Y2) >= Yon2):
        print('Lucky')
    else:
        print('Poor')
'''
X = [ X1, X2 ]
Y = [ Y1, Y2 ]
sw = 0
is_p = False
for x in X:
    for y in Y:
        r = A*x+B*y+C
        if r == 0:
            continue
        elif r > 0:
            if sw != 2: sw = 1;
            else:
                is_p = True
                print('Poor')
                break
        elif r < 0:
            if sw != 1 : sw = 2
            else:
                is_p = True
                print('Poor')
                break
    if is_p: break

if not is_p:
    print('Lucky')