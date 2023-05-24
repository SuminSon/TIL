import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int,input().split())
q = deque([N])

dist = [10**9]*200001
dist[N] = 0

# 현재 Node를 꺼내서 인접 노드 살펴보고
# 현재 노드까지의 소비 비용 + 그 노드까지 가는 가중치 < 그 노드 가는데 소비 비용
# 이 때 소비 비용을 갱신(다익스트라 구조)
# 가중치가 0이면 덱의 front, 1이면 덱의 back에 삽입
# 목적지에 도달하면 그 때의 도달 값을 출력 후 종료
while q:
    cur = q.popleft()

    if cur == K:
        print(dist[K])
        break;

    w = cur * 2
    if w <= 200000 and dist[w] > dist[cur]:
        dist[w] = dist[cur]
        q.appendleft(w)

    lcur, rcur = cur-1, cur+1
    if 0 <= lcur and dist[lcur] > dist[cur] + 1:
        q.append(lcur)
        dist[lcur] = dist[cur] + 1

    if rcur <= 200000 and dist[rcur] > dist[cur] + 1:
        q.append(rcur)
        dist[rcur] = dist[cur] + 1
