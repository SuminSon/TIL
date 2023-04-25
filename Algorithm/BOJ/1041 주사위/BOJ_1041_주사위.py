import sys
from itertools import combinations
sys.stdin = open('input.txt')

N = int(input())
dices = list(map(int,input().split()))

if N == 1:
    print(sum(dices) - max(dices))
else:
    result = 0
    min_dices = sorted(dices)

    # 3면 - 4개
    min3 = sum(dices)
    for combi in combinations([0,1,2,3,4,5], 3):
        c1,c2,c3 = combi[0],combi[1],combi[2]
        if c1 + c2 != 5 and c2 + c3 != 5 and c1 + c3 != 5:
            if dices[c1] + dices[c2] + dices[c3] < min3:
                min3 = dices[c1] + dices[c2] + dices[c3]
    result += (4 * min3)

    # 2면 - 8n-12
    min2 = sum(dices)
    for combi in combinations([0,1,2,3,4,5], 2):
        c1,c2 = combi[0],combi[1]
        if c1 + c2 !=5:
            if dices[c1] + dices[c2] < min2:
                min2 = dices[c1] + dices[c2]
    result += ((8*N-12) * min2)

    # 1면 - 5n**2 - 16n +12
    result += (5*(N**2)-16*N+12) * min(dices)
    print(result)
