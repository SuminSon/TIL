from collections import deque

def solution(n, results):
    answer = 0
    # 왼쪽은 나를 이긴 집단, 오른쪽은 내게 진 집단
    llrw = [[[], []] for _ in range(n + 1)]
    for r in results:
        winner, loser = r[0], r[1]
        llrw[winner][1].append(loser)
        llrw[loser][0].append(winner)

    for i in range(1, n + 1):
        visited = [0 for _ in range(n + 1)]
        visited[i] = 1
        q = deque([i])
        while q:
            v = q.popleft()
            for w in llrw[v][0]:
                visited[w] = 1
                q.append(w)

        q = deque([i])
        while q:
            v = q.popleft()
            for w in llrw[v][1]:
                visited[w] = 1
                q.append(w)

        if all(a == 1 for a in visited[1:]):
            answer += 1

    print(llrw)
    print(answer)
    return answer

solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])