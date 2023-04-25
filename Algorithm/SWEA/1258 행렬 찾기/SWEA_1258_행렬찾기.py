import sys
sys.stdin=open('input.txt')

# 모든 영역 탐색
def all_area(arr):
    # 폭탄 영역 전체 탐색
    for i in range(N):
        for j in range(N):
            # 새 폭탄 영역인지 확인하는 변수
            is_new = True
            # 폭탄 영역일 때,
            if arr[i][j]!=0:
                # 기존 폭탄 영역에 포함된다면 is_new를 False로 갱신하고 for문 탈출
                for i1,j1,i2,j2 in xy:
                    if i1<=i<=i2 and j1<=j<=j2:
                        is_new=False
                        break
                # 해당 인덱스가 모든 폭탄 영역에 속하지 않는 새 영역일 때 갱신
                if is_new:
                    area_count(i,j)

# 폭탄 영역 개수를 세고, 시작점과 끝점의 좌표를 xy에 한 묶음으로 저장하는 함수
def area_count(i,j):
    global cnt
    global xy
    cnt+=1
    x,y=i,j
    while arr[x][y]!=0:
        x+=1
    x-=1
    while arr[x][y] != 0:
        y += 1
    y-=1
    xy.append([i,j,x,y])

# 영역 정렬
def sort_area(xy):
    # 영역 가로, 세로 크기를 담기(인덱스 정보 -> 영역 가로,세로)
    result = []
    for i1, j1, i2, j2 in xy:
        result.append((i2-i1+1,j2-j1+1))

    # 정렬
    for r in range(0,len(result)-1):
        for rr in range(r+1,len(result)):
            # 영역 크기가 작은 순서대로 bubble sort.
            if result[r][0]*result[r][1]>result[rr][0]*result[rr][1]:
                result[r],result[rr]=result[rr],result[r]
            # 크기가 같다면 행이 작은 순서대로
            elif result[r][0]*result[r][1]==result[rr][0]*result[rr][1]:
                if result[r][0]>result[rr][0]:
                    result[r], result[rr] = result[rr], result[r]
    return result

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split()))for _ in range(N)]
    # 폭탄 영역 개수를 셀 변수 cnt, 영역 정보를 담을 리스트 xy
    cnt,xy=0,[]
    # 전체 탐색
    all_area(arr)
    # 영역 가로, 세로 크기를 담아 정렬
    result=sort_area(xy)
    # 양식에 맞게 출력
    print(f'#{tc} {cnt}', end=' ')
    for r1,r2 in result: print(r1,r2,end=' ');
    print()