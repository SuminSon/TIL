import sys
sys.stdin=open('input.txt')


#그리디 알고리즘
#백준 1092 배
#<=50
import sys
input=sys.stdin.readline
#N은 50 이하의 자연수
N=int(input())
#각 크레인 무게제한. <= 1,000,000
w_limit=list(map(int,input().split()))
#박스 수 M<=10,000
M=int(input())
#박스 무게. <= 1,000,000
w_box=list(map(int,input().split()))
round=0
w_limit.sort()
while w_box:
    for n in range(N-1,-1,-1):
        if w_limit[n]<max(w_box):
            if n==N-1:
                round=-1
                break
        else:
            w_box.remove(max(w_box))
            if not w_box:
                break
    round+=1
print(round,end='')

'''w_limit.sort(reverse=True)
w_box.sort(reverse=True)
while w_box:
    for n in range(N):
        for m in range(M):
            if w_limit[n]>=w_box[m]:
                w_box.pop(m)
                M-=1
                break
    round+=1'''