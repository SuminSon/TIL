import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 수빈이 N, 동생 K
# 수빈이는 앞뒤로 1초동안 걷고, 2배 위치로 0초만에 이동 가능
# K로 도달하는 최단시간
N, K = map(int,input().split())

print(N, K)
dist = 0
while 2*N <= K :
    N = 2 * N
if K < 2*N:
    dist += min(K-N, 2*N-K)

print(dist)