import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 5430 AC
T = int(input())
for tc in range(T):
    p = list(map(str,input()))[:-1]
    n = int(input())
    if n != 0:
        Xns = list(map(int,input().replace('[','').replace(']','').split(',')))
    else:
        Xns = input()
        Xns = []

    # 최초 리스트를 덱에 넣고 R 커맨드에 따라 앞 혹은 뒤에서 뺀 후 마지막에 앞에서부터 / 뒤에서부터 출력
    q = deque(Xns)
    is_e = False
    is_rev = False
    for pf in p:
        if pf == 'R':
            is_rev = not is_rev
        elif pf == 'D':
            if q:
                if is_rev == False:
                    q.popleft()
                else:
                    q.pop()
            else:
                print('error')
                is_e = True
                break
    
    if not is_e:
        if is_rev == False:
            print('['+','.join(str(e) for e in list(q))+']')
        else:
            lq = (list(q))
            lq.reverse()
            print('['+','.join(str(e) for e in list(lq))+']')
    