import sys
sys.stdin = open('input.txt')

def check(target:(int,int), pair_list:list):
    global answer
    tx,ty = target
    for i in range(len(pair_list)):
        px,py = pair_list[i]
        for j in range(i+1, len(pair_list)):
            X, Y = pair_list[i]
            if (px-tx)*X+(py-ty)*Y-(px-tx)*tx-(py-ty)*ty == 0:
                answer += 1

N = int(input())
xy = [ tuple(map(int,input().split())) for _ in range(N) ]
print(xy)

answer = 0
for i in range(N):
    check(xy[i], xy[i+1:])
print(answer)

