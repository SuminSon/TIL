import sys
sys.stdin=open('input.txt')

# 끝을 최대 기둥으로 하는 반쪽 영역의 창고 면적 합산(최대 기둥 제외)
def side_pil(pil):
    global cnt            # 합산을 위해 메인의 변수 global 선언
    pp=(0,0)              # pp - 이전 기둥 정보값. 초기값 (0,0)
    for pl in pil:        # pl - 현재 기둥 정보값.
      if pl[1]>=pp[1]:    # 이전 기둥과 크거나 같은 높이 기둥을 만났을 때,
          cnt+=pp[1]*abs(pl[0]-pp[0]) # 이전까지의 창고 면적 합산
          if pl==pil[-1]: break; # 최대 기둥에 도달 시 반복문 탈출 후 그대로 종료
          pp=pl           # 아니라면 이전 기둥에 현재 기둥 갱신

# ----- 메인 ----- #
pils=[] # pils - 기둥 정보 (위치, 높이) 를 저장할 리스트
cnt=0   # cnt - 면적 값을 합산할 변수
# 입력값 받아오기
N=int(input())
for _ in range(N):
    L,H=map(int,input().split())
    pils.append((L,H))

# 위치 기준 오름차순 정렬(버블 소트)
for i in range(len(pils)-1,-1,-1):
    for j in range(i):
        if pils[i][0]<pils[j][0]:
            pils[i],pils[j]=pils[j],pils[i]

# 슬라이싱을 하기 위한 최대 기둥의 인덱스와,
# 마지막에 합산하기 위해 최대 기둥 높이값을 구합니다.
max_idx, max_h=0,0
for p in range(len(pils)):
    if pils[p][1]>max_h:
        max_h=pils[p][1]
        max_idx=p

# 리스트 슬라이싱 시, max_idx를 기준으로 자르되
# max_idx가 0일 경우 인덱스가 -1로 넘어가며 역순 슬라이싱 불가
# 따라서 해당 경우는 별도로 처리
pil1=pils[:max_idx+1]
pil2=pils[:max_idx-1:-1] if max_idx!=0 else pils[::-1]

side_pil(pil1)  # 왼쪽 창고 면적 합산
side_pil(pil2)  # 오른쪽 창고 면적 합산
cnt+=max_h      # 최고 높이 기둥 면적 합산
print(cnt)
