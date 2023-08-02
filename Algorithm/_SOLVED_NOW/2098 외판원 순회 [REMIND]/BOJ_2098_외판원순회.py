import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# TSP 외판원 순회
# 1~N번 번호 매겨진 도시들이 있고, 도시 사이에는 길이 있거나 없거나
# 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래 도시로 돌아오는 순회여행
# 한 번 갔던 도시로는 돌아올 수 없다. 출발점으로 돌아오는 것은 예외
# 가장 적은 비용을 들이는 여행 계획 세우기

N = (int)(input())
W = [list(map(int,input().split())) for _ in range(N)]
isTSP = (1<<N) -1

# dp[현재 위치] [방문 여부 비트마스킹]
# 현재 도시에서 남은 도시들을 거쳐 다시 출발점으로 돌아오는 비용 저장
# 값은 아직 방문하지 않은 도시들을 모두 거쳐 다시 시작점으로 돌아가는데 드는 최소비용
# 현재 위치와 시작지점이 이어져있어야한다.
# 0은 이어져있지 않음을 의미
INF = float('inf')
dp = [[None]*(isTSP+1) for _ in range(N)]

# 출발점은 어디에서 시작하든 결국 돌아와야 하고
# 그 말인 즉슨 어디서 시작해도 최솟값이 변하지 않음
# 따라서 시작점을 idx 0으로 잡고 dfs
def dfs(x, visited):
    if visited == isTSP:
        # 출발점으로 돌아가는 경로가 있다면 반환, 없다면 무한
        if W[x][0]:
            return W[x][0] or INF

    if dp[x][visited] is not None: # 최소 비용 계산이 되어있다면
        return dp[x][visited]

    tmp = INF
    # 다른 도시 순회
    for i in range(N):
        if W[x][i]!=0 and visited & (1<<i) == 0: # 첫 방문이며 경로가 있다면
            # dp[x][11111(2)]...기본값을 INF로 설정하고, 방문한 곳으로부터 남은 도시 순회 시의 최소비용 기록
            # 즉 11111->0000 순서로 합산해나가게 됩니다.
            # 현재 값과 그 다음 값 간의 min을 계산 후 합산
            tmp = min(tmp,dfs(i,visited|(1<<i)) + W[x][i])
    dp[x][visited] = tmp
    return tmp

# 시작점 0, 시작점만을 방문한 visited 비트 000001
print(dfs(0,1))