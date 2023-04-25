import sys
sys.stdin=open('input.txt')

exp=input()
e=0
is_op=False
while e<len(exp):
    if exp[e]=='-':
        if not is_op:
            exp=exp[:e+1]+'('+exp[e+1:]
            is_op=True
            e+=1
        elif is_op:
            exp = exp[:e] + ')' + exp[e:]
            exp = exp[:e + 2] + '(' + exp[e + 2:]
            #is_op=False
            e+=2
    e+=1
if e==len(exp) and is_op:
    exp=exp+')'

result=[]
prev_num=0
for e in exp:
    if e=='+' or e=='-':
        if prev_num!=0:
            result.append(str(prev_num))
        result.append(e)
        prev_num=0
    elif e=='(':
        result.append(e)
    elif e==')':
        result.append(str(prev_num))
        result.append(e)
        prev_num = 0
    else:
        prev_num*=10
        prev_num+=int(e)
if not prev_num==0:
    result.append(str(prev_num))
    prev_num = 0
str_exp=''.join(result)
'''print(exp)  # 입력된 식에 괄호만 넣은 것
print(result) # 0 지우고 리스트로 만들어서
print(str_exp) # 깔끔하게 문자열 식으로 나타내고
print(str_exp)'''
print(eval(str_exp)) # eval로 결과 확인

