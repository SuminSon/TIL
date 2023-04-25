import sys
sys.stdin=open('input.txt')

K=int(input())
dir=[]
# 동1 서2 남3 북4
dw,w,dh,h=0,0,0,0
# 입력값 저장하면서 최대 너비높이와 그때의 방향도 함께 구합니다.
for _ in range(6):
    d,l=map(int,input().split())
    if (d==1 or d==2):
        if w<l: dw,w=d,l
    if (d==3 or d==4):
        if h<l: dh,h=d,l
    dir.append([d,l])

# 기존의 dw dh 조합으로 붙어있는게 있는지 보고 있다면 해당 순서로 픽스
max_d=None
is_near=False
for i in range(len(dir)-1):
    if sorted([dir[i][0],dir[i+1][0]])==sorted([dw,dh]):
        max_d=[dir[i][0],dir[i+1][0]]
        is_near=True
        break

# 없으면 태양이가 돈 꼭지점이... 하필 그 사이였을테니까
# 만날 수 있도록... 붙여준 후 그 순서를 픽스
if not is_near:
    dir.append(dir.pop(0))
    max_d=[dir[-2][0],dir[-1][0]]

# 최대로 도는 방향이 처음에 올 수 있도록 순서 조정
# 안그러면 방향체크 불가능
while [dir[0][0],dir[1][0]]!=max_d:
    dir.append(dir.pop(0))

# 이제 이 max_d로 도는 방향과 반대되는 min_d를 찾습니다
# 그때의 가로 세로 값을 곱해 빼주면 전체 면적이 나오기 때문
dirdic={1:2,2:1,3:4,4:3}
min_d=[dirdic[max_d[1]],dirdic[max_d[0]]]

for d in range(len(dir)-1):
    if [dir[d][0],dir[d+1][0]]==min_d:
        print((w*h-dir[d][1]*dir[d+1][1])*K)
        break
