from collections import deque

def solution(tickets):
    answer = []
    graph = {}
    for t in tickets:
        s, g = t[0], t[1]
        if s not in graph:
            graph[s] = [(g, 0)]
        else:
            graph[s].append((g, 0))

    for s in graph: graph[s].sort()
    print(graph)

    q = deque(['ICN'])
    stack = [q]
    path = ['ICN']
    cnt = 0
    while stack:
        v = stack[-1].popleft()
        if not stack[-1]: stack.pop()

        if cnt == len(tickets):
            answer = path[:]
            break

        q = deque([])
        for wdx in range(len(graph[v])):
            w, w_go = graph[v][wdx]
            if w_go == 0:
                graph[v][wdx] = (w, 1)
                path.append(w)
                cnt += 1
                q.append(w)
        stack.append(q)

    return answer


#solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])