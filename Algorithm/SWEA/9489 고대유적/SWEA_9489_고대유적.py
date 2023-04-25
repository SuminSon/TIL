import sys
sys.stdin=open('input.txt')

# 8개만 정답

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(N)]
    #print(arr)
    max_len=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==1:
                cnt=1
                if i+1<N and arr[i+1][j]==1:
                    k=1
                    while i+k<N and arr[i+k][j]==1:
                        cnt+=1
                        k+=1
                if max_len<cnt:
                    max_len=cnt

                cnt = 1
                if j+1<M and arr[i][j+1]==1:
                    k = 1
                    while j+k<M and arr[i][j+k] == 1:
                        cnt += 1
                        k += 1
                if max_len < cnt:
                    max_len = cnt

    print(f'#{tc} {max_len}')