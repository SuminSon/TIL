import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = (int)(input())
xy = [tuple(map(int,input().split())) for _ in range(N)]
answer = 0
for i in range(len(xy)-2):
    for j in range(i+1,len(xy)-1):
        for k in range(j+1, len(xy)):
            d1,d2,d3 = xy[i],xy[j],xy[k]
            l1 = (d1[0]-d2[0])**2 + (d1[1]-d2[1])**2
            l2 = (d1[0]-d3[0])**2 + (d1[1]-d3[1])**2
            l3 = (d2[0]-d3[0])**2 + (d2[1]-d3[1])**2
            if 2 * max(l1,l2,l3) == l1 + l2 + l3:
                answer += 1
print(answer)