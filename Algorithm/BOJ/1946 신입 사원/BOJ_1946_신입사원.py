import sys
sys.stdin=open('input.txt')

T=int(input())
for tc in range(1,T+1):
    # 지원자 수 1<= N <= 100 000
    N = int(input())
    ranks=[]
    for _ in range(N):
        r1,r2=map(int,input().split())
        ranks.append((r1,r2))
    ranks.sort(key=lambda x:(x[0],x[1]))
    print(ranks)
    result=1
    limit_rank=ranks[0][1]
    for

'''import sys
input=sys.stdin.readline
#그리디 알고리즘
#백준 1946 신입 사원
T=int(input())
for tc in range(1,T+1):
    #지원자 수 1<= N <= 100 000
    N=int(input())
    hq=[]
    for _ in range(N):
        r1,r2=map(int,input().split())
        hq.append((r1,r2))
    hq.sort()
    result=1
    rank=hq[0][1]
    for i in range(1,N):
        if rank>hq[i][1]:
            result+=1
            rank=hq[i][1]
    print(f'#{tc} {result}')
'''

'''import heapq
T=int(input())
for tc in range(1,T+1):
    #지원자 수 1<= N <= 100 000
    N=int(input())
    hq=[]
    for _ in range(N):
        r1,r2=map(int,input().split())
        heapq.heappush(hq,(r1,r2))

    first = heapq.heappop(hq)
    result=1
    while hq:
        p=heapq.heappop(hq)
        print('p=',p)
        if first[0]>p[0] or first[1]>p[1]:
            print(first,p)
            result+=1
            first=(p[0] if first[0]>p[0] else first[0],p[1] if first[1]>p[1] else first[1])
        if first[0]==1 and first[1]==1:
            break

    print(f'#{tc} {result}')'''

