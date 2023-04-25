from collections import deque
def solution(n, s, a, b, fares):
    answer = 100000*n+1
    # n : 노드 개수
    # s, a, b : 출발지, 도착지1, 도착지2
    # fares: [구간1, 구간2, 요금] 모음 리스트

    graph = [ [] for _ in range(n+1) ]
    for f in fares:
        n1, n2, pay = f[0], f[1], f[2]
        graph[n1].append((pay,n2))
        graph[n2].append((pay,n1))

    # 1번 ~ n번 각 노드에 대해해
    for ni in range(1,n+1):
        dist = [100000*n+1 for _ in range(n+1)]
        dist[ni] = 0
        #cnt = 0 if ni not in [a,b,s] else 1
        this_sum = 0
        q = deque([ni])
        while q:
            v = q.popleft()
            for nj in graph[v]:
                next_pay, w = nj
                if dist[v] + next_pay < dist[w]:
                    dist[w] = dist[v] + next_pay
                    q.append(w)
        if dist[a]+dist[b]+dist[s] < answer:
            answer = dist[a]+dist[b]+dist[s]
        print(ni, dist)
        print(answer)
    return answer

solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])