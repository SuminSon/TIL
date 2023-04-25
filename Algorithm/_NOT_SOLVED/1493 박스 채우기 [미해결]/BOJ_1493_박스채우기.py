def sublist_max(profits):
    # 코드를 작성하세요.
    max_profit = profits[0]
    for i in range(len(profits)):
        total = 0
        for j in range(i, len(profits)):
            total += profits[j]
            if total> max_profit:
                max_profit=total
    return max_profit


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))



'''import sys
sys.stdin=open('input.txt')
input=sys.stdin.readline

lwh=[0]*3
lwh[0],lwh[1],lwh[2]=map(int,input().split())
#큐브 개수
N=int(input())
boxs=[]
for _ in range(N):
    Ai,Bi=map(int,input().split())
    boxs.append([Ai,Bi])
lwh.sort()
boxs.sort()

print(lwh)
print(boxs)

result=0

while True:
    for b in range(len(boxs)):
        if boxs[b][1]==0:
            continue
        box = boxs[b]
        t, n = box[0], box[1]  # 박스 크기 유형, 해당 박스 개수
        for i in range(2, -1, -1):
            if lwh[i]%(2**(t+1))!=0 and lwh[i]>=((2**(t))):
                if n>=(lwh[i-1]//(2**t))*(lwh[i-2]//(2**t)) or (b==len(boxs)-1 and n!=0):
                    if n>=(lwh[i-1]//(2**t))*(lwh[i-2]//(2**t)):
                        n-=(lwh[i-1]//(2**t))*(lwh[i-2]//(2**t))
                        result += (lwh[i - 1] // (2 ** t)) * (lwh[i - 2] // (2 ** t))
                    else:
                        result+=n
                        n = 0
                    lwh[i] -= 2 ** t
                else:
                    result=-1
                    break
        if result==-1:
            break
        print(lwh)
        print(boxs)


print(result)'''