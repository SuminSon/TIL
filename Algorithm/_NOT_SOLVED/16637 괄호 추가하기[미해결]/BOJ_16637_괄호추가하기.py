def solution(m, n, puddles):
    m,n=4,3
    puddles = [[1,2],[2,1]]
    answer = 0
    arr = [[0 for _ in range(m)] for _ in range(n)]
    for p in puddles:
        i, j = p[1], p[0]
        arr[i - 1][j - 1] = -1  # 못 가는 웅덩이 -1로 표시

    # 세로 첫줄 갱신
    for ii in range(n):
        if arr[ii][0] != -1:
            arr[ii][0] = 1
        elif arr[ii][0] == -1:
            break
    # 가로 첫줄 갱신
    for jj in range(m):
        if arr[0][jj] != -1:
            arr[0][jj] = 1
        elif arr[0][jj] == -1:
            break

    for ii in range(1, n):
        for jj in range(1, m):
            if arr[ii][jj] == 0:
                if arr[ii][jj-1] == -1:
                    if arr[ii-1][jj] != -1:
                        arr[ii][jj] = arr[ii-1][jj]
                else:
                    arr[ii][jj] = arr[ii - 1][jj] + arr[ii][jj - 1]
                    if arr[ii-1][jj] == -1: arr[ii][jj] += 1

    answer = arr[n - 1][m - 1]
    for a in arr:
        print(a)
    return answer

print(solution(9,6,[[2, 3], [6, 3], [5, 5], [7, 6]]))


'''import sys
sys.stdin = open('input.txt')

N = int(input())
exp = input()
stack = []
for c in exp:
    if c.isdecimal():
        stack.append(c)
    else:
        if c == '+':

'''