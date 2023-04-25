import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 3101 토끼의 이동
# N 행렬의 크기
# K 토끼가 점프한 횟수
N, K = map(int,input().split())
jump_commend = list(input())
print(jump_commend)