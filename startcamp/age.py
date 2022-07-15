#python age.py
from unicodedata import name
import requests

url='https://api.agify.io?name=michael'
response=requests.get(url).json()
print(response) #200..2로 시작 잘 와서 응답해줬다
name=response['name']
age=response['age']
count=response['count']
print('이름이 '+name+'인 사람의 나이는 '+str(age)+'입니다')