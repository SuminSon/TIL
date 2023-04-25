import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 3096 영화제
# N: 마을 수 M: 배의 수
N, M = map(int,input().split())
path = {}
result = 0
for n in range(1,N+1):
    path[n] = []

for m in range(M):
    l, r = map(int,input().split())
    path[l].append(r)
    # path[r].append(l)

for li in range(1,N):
    for lj in range(li+1,N+1):
        for ri in range(1,N):
            for rj in range(ri+1,N+1):
                if (ri in path[li]) and (rj in path[li]) and (ri in path[lj]) and (rj in path[lj]):
                    result += 1

print(result)