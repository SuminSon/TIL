import sys
sys.stdin=open('input.txt')
#input=sys.stdin.readline

nop=input().replace(' ','')
nums=[]
for n in nop:
    if n=='+' or n=='-':
        nums.append(n)
    else:
        nums.append(int(n))

result,m_sums=0,0
prev_op=None
prev_num=0
for n in nums:
    if prev_op!='-' and (n=='+' or n=='-'):
        result+=prev_num
        prev_num=0
        if n=='-':
            prev_op = '-'

    elif prev_op=='-':
        if n=='+' or n=='-':
            m_sums+=prev_num
            prev_num=0

    if not (n=='+' or n=='-'):
        prev_num*=10
        prev_num+=n

if prev_num!=0:
    if prev_op=='-':
        m_sums+=prev_num
    else:
        result+=prev_num

result-=m_sums
print(result)















'''is_op=False
prev_num=0
result=0
sums=0
for n in nop:
    if n=='-':
        if is_op==False:
            result+=prev_num
            prev_num=0
            is_op=True
        elif is_op==True:
            if sums!=0:
                result-=sums
                sums=0
            if prev_num!=0:
                result-=prev_num
                prev_num=0

    elif n=='+':
        if is_op==False:
            result+=prev_num
            prev_num=0
        else:
            sums+=prev_num
            prev_num=0
    else:
        prev_num*=10
        prev_num+=int(n)

if prev_num!=0:
    if is_op==True:
        sums+=prev_num
    else:
        result+=prev_num
if sums!=0:
    result-=sums
#print(nums)
print(result)'''