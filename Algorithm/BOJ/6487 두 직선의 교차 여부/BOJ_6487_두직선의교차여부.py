import sys
sys.stdin = open('input.txt')

def point_out():
    px = ((y4 - m2 * x4) - (y2 - m1 * x2)) / (m1 - m2)
    py = m1 * px + (y2 - m1 * x2)
    print(f'POINT {px:.2f} {py:.2f}')

N = int(input())
for tc in range(1,N+1):
    x1, y1, x2, y2, x3, y3 ,x4, y4 = map(int,input().split())
    if x1 != x2: m1 = (y2-y1)/(x2-x1)
    else: m1 = 'INF'
    if x3 != x4: m2 = (y4-y3)/(x4-x3)
    else: m2 = 'INF'
    if m1 == 'INF':
        if m2 == 'INF':
            if x1 == x3: print('LINE')
            else: print('NONE')
        else:
            px = x1
            py =  m2 * px + (y4 - m2 * x4)
            print(f'POINT {px:.2f} {py:.2f}')
    elif m2 == 'INF':
        if m1 == 'INF':
            if x1 == x3: print('LINE')
            else: print('NONE')
        else:
            px = x3
            py =  m1 * px + (y2 - m1 * x2)
            print(f'POINT {px:.2f} {py:.2f}')
    elif m1 == m2:
        if (y4 == m2*x4 + y3-m2*x3) and (y2 == m1*x2 + y3-m2*x3): print('LINE')
        else: print('NONE');
    else: point_out()
