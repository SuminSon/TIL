#python lotto.py
#다음주에 할..로또 api 
from unittest import result
import requests
import random

# 1. lotto api로부터 데이터 받아오기
# 1023회가 최근 7월 9일
#Num=input() #회차 입력을 받습니다. url 뒤에 숫자로 넣을 예정이므로 str로 그냥 받기!
Num=str(1023)
url='https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+Num #추가! 입력한 회차 json을 불러옵니다.
response=requests.get(url).json()

# 2. 지난주 당첨 번호 알아내기(1등만)
drwtNo=[]
for i in range(1,7):
    drwtNo.append(response['drwtNo'+str(i)])# 당첨번호 drwtoNo1~6을 drwtNo[] 리스트에 하나씩 넣기
drwtNo.append(response['bnusNo']) #보너스 번호도 넣어줍시다~
print(drwtNo) #출력!
lottoRe=[0,0,0,0,0]  #1~5등 각 당첨 횟수
def lottoResult(Turn):
    for a in range(0,Turn):
# 3. random 모듈을 이용해서 ..얘가 가진 sample이라는 함수를 사용해서 1부터 45 중에 무작위 6개 뽑는다
        myNum=[]    #내가 뽑을 번호를 저장할 리스트를 선언합니다.

        for i in range(0,7):    #보너스까지 7개의 번호를 뽑기
            myNum.append(random.randrange(1,46))#1~45 사이의 랜덤한 수를 총 6번 + 보너스 1번 뽑습니다.
            for j in range(0,i):
                while myNum[j]==myNum[i]:
                    myNum[i]=(random.randrange(1,46)) #뽑은 수가 같으면 다를때까지 뽑아!!!

   # print(myNum) #출력!


# 4. 그 번호가 내 당첨 번호와 일치하는지 확인하기

        howSame=0 #몇 개의 숫자가 일치하는지 카운트 하기위한 int 변수
        for i in range(0,6): #당첨번호 6개와
            for j in range(0,6): #제가 뽑은 번호 6개를 먼저 비교!
                if(drwtNo[i]==myNum[j]):
                    howSame+=1
        if(howSame==6):
            print('6개의 번호가 일치합니다. 1등입니다!')
            lottoRe[0]+=1
        elif(howSame==5): #당첨 번호 숫자 5개 일치할 때
            if(drwtNo[6]==myNum[6]): #보너스 번호가 일치하는지 확인!!
                print('5개와 보너스 1개가 일치합니다. 2등입니다!')
                lottoRe[1]+=1 #2등 추가요~
        elif(howSame>=3):
            lottoRe[7-howSame]+=1
            print(howSame,'개의 번호가 일치합니다.')
        else:
            print(howSame,'개의 번호가 일치합니다.')
        
# 5. 도전과제. 천 번 이상 새로운 로또 번호를 생성해서 
# 매번 당첨이 되었는지 확인해보는 로직 만들기

print(복권 횟수? )
Turn=int(input()) #몇 번 굴릴겨?
lottoResult(Turn)


# 6. 도전과제. 1~2등포함한(보너스 번호도 알아야함) 5등까지의 각 당첨 횟수 출력
for i in range(1,6):
    print(i,'등은 ',lottoRe[i-1],'회')