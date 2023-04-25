import sys
sys.stdin=open('input.txt')

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    max_sum=0
    for i in range(N):
        for j in range(N):
            # 십자검사
            now_sum=arr[i][j]
            for k in range(1,M):
                if 0<=i+k<N: now_sum+=arr[i+k][j];
                if 0<=i-k<N: now_sum+=arr[i-k][j];
                if 0<=j+k<N: now_sum+=arr[i][j+k];
                if 0<=j-k<N: now_sum+=arr[i][j-k];
            if max_sum<now_sum:
                max_sum=now_sum

            # 대각선 검사
            now_sum = arr[i][j]
            for k in range(1,M):
                if 0<=i+k<N and 0<=j+k<N: now_sum+=arr[i+k][j+k];
                if 0<=i-k<N and 0<=j+k<N: now_sum+=arr[i-k][j+k];
                if 0<=i-k<N and 0<=j-k<N: now_sum+=arr[i-k][j-k];
                if 0<=i+k<N and 0<=j-k<N: now_sum+=arr[i+k][j-k];
            if max_sum<now_sum:
                max_sum=now_sum

    print(f'#{tc} {max_sum}')