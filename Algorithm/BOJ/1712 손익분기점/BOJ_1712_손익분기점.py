import sys
sys.stdin=open('input.txt')

A,B,C=map(int,input().split())
result=0
if B>=C:
    result=-1
else:
    result=A//(C-B)+1

print(result)