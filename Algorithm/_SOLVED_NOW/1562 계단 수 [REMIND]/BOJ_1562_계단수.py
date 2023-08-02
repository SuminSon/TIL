import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 45656 인접 모든 자리수 차이 1 = 계단수
# N이 주어질 때 길이가 N이면서 0~9가 모두 등장하는 계단수가 총 몇 개 있는지 구하기. 0으로 시작하는건 제외

N = (int)(input())

# isStair : 0~9 모든 수가 들어가있을때의 비트마스킹 숫자
isStair = (1<<10) - 1
MOD = 10**9

# dp[마지막 자리수][0~9비트연산자를 인덱스로 갖는 배열]
# 각각의 값에는 해당 자리 수가 현재까지 이런 조합을 가질 때 경우의 수가 기록됩니다.
dp = [[0]*(isStair+1) for _ in range(10)]

# 첫 자리 수는 1~9
# 해당 자리 수 | 0~9 방문 여부 인덱스를 1로 표기
for i in range(1, 10):
    dp[i][1 << i] = 1

# 두 번째 자리 수부터 N번째 자리 수까지 반복한다는 명시
# 해당 자리수에 대해 기록할 next_dp를 생성 후
for _ in range(2, N+1):
    next_dp = [[0]*(isStair+1) for _ in range(10)]
    for i in range(10):
        # 0~9 포함 여부 모든 경우의 수를 순회합니다.
        # 해당 i자리가 포함되는 영역에 이전 -1 값과 이전 +1 경우의 수 값을 합산해나갑니다.
        # 단, i == 0 이거나 i == 9 일때는 이전 값이 하나이므로 예외적으로 처리합니다.
        for j in range(isStair+1):
            if i>0:
                next_dp[i][j | (1<<i)] = (next_dp[i][j| (1<<i)] + dp[i-1][j]) % MOD
            if i<9:
                next_dp[i][j | (1<<i)] = (next_dp[i][j| (1<<i)] + dp[i+1][j]) % MOD

    # 해당 자리 수에 대한 경우의 수 탐색이 끝나면 기존 dp를 갱신합니다.
    dp = next_dp

# 0~9 로 끝나는 상태에서 0~9가 모두 들어가있음을 의미하는 isStair 번째 인덱스의 경우의 수 합을 구해 출력
print(sum(dp[i][isStair] for i in range(10)) % MOD)
