import sys
from itertools import combinations
sys.stdin = open('input.txt')


answer = -(2)**32
N = int(input())
formula = input()

if len(formula) == 1:
    answer = (int)(formula)


num = list(map(lambda x: int(x),formula[::2]))
op = formula[1::2]
opVisit = [0] * len(op)

#만들 수 있는 최대 괄호 갯수
max_bracket = (len(op)+1)//2
o = [i for i in range(len(op))]

# 괄호 개수에 따른 괄호선택과, 그에 따른 계산 순서
for b in range(1,max_bracket+1):
    c = [i for i in range(0, len(op))]
    pars = list(combinations(c, b))
    for par in pars:
        isOpSet = True
        for p in par:
            if p-1 in list(par) or p+1 in list(par):
                isOpSet = False
                break
        if isOpSet:
            opSet = list(par) + list(filter(lambda i: i not in list(par), o))
            for p in opSet:
                num = list(map(lambda x: int(x), formula[::2]))
                v = [0] * len(num)
                thisNum = 0
                for k in opSet:
                    if op[k] == '+':
                        thisNum = num[k] + num[k + 1]
                    elif op[k] == '-':
                        thisNum = num[k] - num[k + 1]
                    elif op[k] == '*':
                        thisNum = num[k] * num[k + 1]
                    num[k] = num[k + 1] = thisNum
                    if v[k] == v[k + 1] == 0:
                        v[k] = v[k + 1] = k + 1
                    elif v[k] == 0 and v[k + 1] != 0:
                        v[k] = v[k + 1]
                        for idx in range(k + 2, len(num)):
                            if v[k + 1] == v[idx]:
                                num[idx] = thisNum
                    elif v[k + 1] == 0 and v[k] != 0:
                        v[k + 1] = v[k]
                        for idx in range(k - 1, -1, -1):
                            if v[k] == v[idx]:
                                num[idx] = thisNum
                    else:
                        for idx in range(k - 1, -1, -1):
                            if v[k] == v[idx]:
                                v[idx] = min(v[k], v[k + 1])
                                num[idx] = thisNum

                        for idx in range(k + 2, len(num)):
                            if v[k + 1] == v[idx]:
                                v[idx] = min(v[k], v[k + 1])
                                num[idx] = thisNum
                        v[k] = v[k + 1] = min(v[k], v[k + 1])
                answer = max(answer, thisNum)
print(answer)
