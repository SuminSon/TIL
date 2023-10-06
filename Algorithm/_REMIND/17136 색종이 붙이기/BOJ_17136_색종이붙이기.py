import sys
sys.stdin = open('input.txt')

paper = [ list(map(int, input().split())) for _ in range(10) ]
myPaper = [5,5,5,5,5]

def check(i,j,dep):
    for idx in range(i, i+ dep +1):
        for jdx in range(j, j+ dep + 1):
            if paper[idx][jdx] != 1:
                return False
    return True

result = 25
def backtracking(i,j, ans):
    global myPaper, result

    # 탐색이 끝났으니 현재 ans와 결과값 비교 후 return
    if i >= 10:
        result = min(result, ans)
        return

    # y축 끝에 도달했으니 다음 라인 탐색하러 go.
    # 라인을 바꿨으니 아래쪽 탐색은 불필요함. return
    if j >= 10:
        backtracking(i+1,0,ans)
        return

    # 붙일 수 있을 때
    if paper[i][j] == 1:
        for dep in range(5):
            # 종이 개수 안 남아있으면 pass
            if myPaper[dep] == 0: continue
            # 범위가 10 * 10 넘어가도 pass
            if i + dep >= 10 or j + dep >= 10 : continue
            # 모든 붙이기 범위가 1이 아니면 pass
            # 이걸 하려면 12345 순서로 체크해야겟네요..
            # 못 붙이면 바로 break하고 추가로 백트래킹 함수 X
            # 따라서 자동으로 stack에서 빠져나가고, result와 비교 불가
            # 무조건 자리를 매꾸든 쥘얼을하든 전부 붙이면서 나아가야
            # 끝까지 탐색되어 result와 비교하게 될 수 있다.
            if not check(i,j,dep): break

            # 붙을 구역을 0으로 만들어서 다른 넘들이 못 붙이게 처리
            # 해당 색종이 하나 사용 후 가로 dep 칸만큼 뛰어넘어 탐색
            for ni in range(i,i+dep+1):
                for nj in range(j,j+dep+1):
                    paper[ni][nj] = 0
            myPaper[dep] -= 1
            backtracking(i,j + dep + 1,ans+1)

            # 붙이지 않았던 상태로 돌아감
            myPaper[dep] += 1
            for ni in range(i,i+dep+1):
                for nj in range(j,j+dep+1):
                    paper[ni][nj] = 1

    # 붙일 수 없다면 다음 칸 고
    else: backtracking(i,j+1,ans)

backtracking(0,0,0)
print(-1 if result == 25 else result)