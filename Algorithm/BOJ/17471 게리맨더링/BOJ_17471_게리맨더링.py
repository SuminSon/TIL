import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# ----------------------------------------------------------

# 1 ~ N-1 개 조합을 고르는 재귀 함수
# idx   조합 함수 내부에서 사용할 구간 변수
# k     몇 개의 조합을 고르는지 명시한 변수
# elem  실제 조합이 저장되는 리스트
def combi(idx:int, k:int,elem:list):
    global min_P, is_not_answer

    # k 개의 조합이 골라졌다면
    if len(elem) == k:
        # 골라진 조합을 하나의 선거구로 했을 때
        # 그 조합이 연속되며, 타 선거구 또한 연속되어 조건을 만족한다면
        if bfs(elem, 1):
            # 선거구 분할에 성공했으므로 해당 변수를 False로 바꿉니다.
            if is_not_answer: is_not_answer = False
            # 두 선거구의 인구 차이를 최솟값으로 갱신 후 리턴합니다.
            now_p = 0
            for e in elem:
                now_p += people[e]
            if min_P > abs(sum(people) - now_p - now_p):
                min_P = abs(sum(people) - now_p - now_p)
        return

    # k 개의 조합을 고르는 for문
    # 고르거나 고르지 않은 다음 수부터 탐색할 수 있도록 idx 값을 활용
    for i in range(idx+1, N+1):
        combi(i, k, elem + [i])

# ----------------------------------------------------------

# 입력된 조합을 하나의 선거구로 했을 때, 먼저 그 선거구가 연속되어 조건을 만족하고
# 그 때 남은 조합이 또 하나의 선거구 조건을 만족하는지 확인해 bool을 반환하는 bfs 함수
# check_list    입력된 조합을 담은 리스트
# type          현재 검사중인 선거구 타입. 1 - A선거구, 2 - B 선거구
# type이 2일때 마저 조건을 만족한다면 두 선거구 모두 조건을 만족한 것이므로 True 반환
def bfs(check_list:list, type:int) -> bool:
    visited = [0 for _ in range(N + 1)]
    q = deque([check_list[0]])
    visited[check_list[0]] = 1
    while q:
        v = q.popleft()
        for w in graph[v]:
            # 방문하지 않았으며, check_list에 존재하는 곳만 탐색
            if visited[w] == 0 and w in check_list:
                visited[w] = visited[v] + 1
                q.append(w)

    # 1에서 시작한 bfs가 만약 check_list중 한 곳이라도 방문하지 못했다면
    # 연속되지 못한 것 == False를 반환
    for c in check_list:
        if visited[c] == 0: return False

    # 해당 조합 선거구가 연속되었다면
    if type == 1: # 남은 영역의 선거구에 대해 한 번 더 탐색
        return bfs([i for i in range(1, N + 1) if i not in check_list], 2)
    elif type == 2: # 모든 구역이 선거구 조건 만족 == True 반환
        return True

# ---------------------- 메인 함수 시작 ----------------------
# 변수 입력 받는 영역
N = int(input())
graph = [ [] for _ in range(N+1)]
people = [0] + list(map(int,input().split()))
for i in range(1,N+1):
    graph[i].extend(list(map(int,input().split()))[1:])

# 한 번이라도 선거구 분할에 성공했다면 이 값은 False로 바뀝니다.
# 모든 탐색 후 여전히 True라면 -1을 반환하도록 합니다.
is_not_answer = True

# 선거구 분할 조합 중 차이가 최소인 값을 저장할 변수
min_P = sum(people)

# 1번 구역을 포함해서 선거구를 1개 ~ N-1개로 나누는 조합을 돌립니다.
for i in range(1,N):
    combi(1, i,[1])

if is_not_answer: print(-1)
else: print(min_P)
# ----------------------------------------------------------
