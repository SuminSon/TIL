import sys
sys.stdin=open('input.txt')

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    farm=[list(map(int,input()))for _ in range(N)]
    result,m=0,N//2 # 결과값, 범위 증감 분기
    for i in range(N):
        if m-i>=0:  # 증가 분기
            for j in range(m-i,m+i+1):
                result+=farm[i][j]
        else:       # 감소 분기
            for j in range(m-((N-1)-i),m+((N-1)-i)+1):
                result+=farm[i][j]
    print(f'#{tc} {result}')
