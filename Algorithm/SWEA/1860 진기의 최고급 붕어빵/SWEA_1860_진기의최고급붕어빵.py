import sys
import heapq
sys.stdin=open('input.txt')

# 진기의 최고급 붕어빵

T=int(input())
for tc in range(1,T+1):
    # N명. M초에 K개 만들 수 있다.
    # 즉 M초에 K명 보낼 수 있는데,
    # 보낼 사람 다 보내고 남은 대기자를
    # 다시 K명만큼 만족시키지 못하면 바로 실패

    N,M,K=map(int,input().split())
    p=list(map(int,input().split()))

    # 빨리 오는 사람 부터 빨리빨리 처리하고 보내야하므로 시간순 정렬

    # p.sort()
    # -> 전부 정답

    '''    
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if p[i]>p[j]:
                p[i],p[j]=p[j],p[i]
    -> 버블 소트도 전부 정답
    '''

    heapq.heapify(p) # -> 989개 정답
    # p를 heapify 해주는 것 만으로는
    # p 내부에서 자체적으로 정렬되지 않으며
    # p를 빼서 다른 곳에 저장할 때 정렬되어 나오는 특징
    # 따라서 pp라는 새로운 리스트에 저장해 정렬시켜 사용

    pp=[]
    while p:
        pp.append(heapq.heappop(p))

    # 한 턴
    t=1
    can='Possible'
    while K*(t-1)<len(pp):
        # 현재 K명의 대기자 중 가장 먼저 온 사람이
        # 빵을 기다리지 않고 받을 수 있나? 만 체크하면 됨
        # 받을 수 있다면 그 뒤 K명까지 처리 가능
        if (pp[K*(t-1)]<M*t):
            can = 'Impossible'
            break
        t += 1
    print(f'#{tc} {can}')