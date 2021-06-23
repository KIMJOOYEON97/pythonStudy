'''
# lambda함수
# 익명 함수로 일시적인 함수를 의미함. 
# 사용은 함수가 생성된 곳에서 필요할 경우, 사용한 후 버리는 함수
# 
# (형식)
#  lambda 인자리스트: 표현식
#  변수명 = lambda 인자리스트 : 표현식
#  
#  예) lam = lambda x : x**2
#      print(lam(8))   => 출력 결과 : 64
#   
#      lam2 = lambda x,y:x+y
#      print(lam2(2,5))=> 출력 결과 : 7
# 
# 람다는 어디서든지 사용할 수 있는 임시함수   
#   
lam = lambda x:x**2
print(lam(8))

lam2 = lambda x,y:x+y
print(lam2(2,5))

# 예제1) 다음과 같은 함수를 lambda로 표현한 방식
def swap(x,y):
    return y,x
a = 100
b = 200
print(a,b)          # 100 200
a,b = swap(a,b)     # a, b = (200, 100) => swap(a,b)
print(a,b)          # 200 100

# 람다를 사용한 예
swap = lambda a,b: [b,a]
a = swap(10,20)
print(a,type(a))    # [20,10]

# 예제2) 
lam = lambda a: a*10
lam2 = lambda a,b: a+b
noData = lambda :print("인자가 없는 lambda")

#출력 결과 확인
print(lam(10))      # 100
print(lam2(10,20))  # 30
noData()

# 람다 문제) 람다 함수를 사용하여 두수의 +,-,*,/의  사직연산하는 
# 프로그램을 작성하세요. 
Sum = lambda x,y:x+y
Sub = lambda x,y:x-y
Mul = lambda x,y:x*y
Div = lambda x,y:x/y
import os

while True:
    os.system('cls')
    num1 = int(input("첫번째 정수 입력 : "))
    num2 = int(input("두번째 정수 입력 : "))
    giho = input("계산 기호를 입력(+,-,*,/) : ")
    if giho == '+':
        print("계산 결과 : ",Sum(num1,num2))
    elif giho == '-':
        print("계산 결과 : ",Sub(num1,num2))
    elif giho == '*':
        print("계산 결과 : ",Mul(num1,num2))
    elif giho == '/':
        print("계산 결과 : %.2f" % Div(num1,num2))
    else:
        print("계산 기호를 잘못 입력했습니다.")
    sel = input("계속하겠습니까?(Y/n) : ")
    if sel == 'n':
        break

# python의 모듈 및 패키지 사용
#  모듈(Module)이란? 함수, 변수, 클래스들을 모아 놓은 파일
#  (모듈은 만들어 놓은 다른 파이썬 프로그램에서 블러와 사용이 가능함.)
# 
# 모듈을 만드는 방법: *.py 확장자를 이용하여 만들 수 있음. 
# 
# 모듈을 불러오는 방버 : import명령어를 사용하여 모듈을 불러와 사용. 
# (표준 라이브러리를 불러와 사용할 때에서 import사용함.) 
#       

# 시간과 관련있는 모듈들... 
import datetime,time

# datetime 모듈은 시간에 대해서 가공된 정보를 처리.
s = datetime.datetime.now() # 현재 시간을 알아오는 함수
print(s)
t = time.localtime()  # 현재 동작 중인 지역의 시간
print(t)
print(t.tm_year)
print(t.tm_mday)

start = time.time()     # 1970.01.01 00시를 기점으로... 
print(start)          
time.sleep(5)           # 프로그램의 흐름을 지정된 시간동안 멈춤... 
end = time.time()
print(end)

# 모듈을 불러와 사용하기
# (형식1)
#  import 모듈명 => 모듈 내에 있는 모든 함수,클래스,변수 들을 호출
# 
# 모듈에 있는 내용을 사용할 경우 : 모듈명.함수(변수,클래스)
#   
import calc
a = 100
b = 200
c = 10
Sum = calc.Sum(a,b)
Sub = calc.Sub(b,a)
Mul = calc.Multi(b,c)
Div = calc.Div(b,a)
calc.Result = (Sum + Sub)-int((Mul/Div))
print("변수 a,b,c의 계산 결과들... ")
print("a+b의 결과 : ",Sum)
print("b-a의 결과 : ",Sub)
print("b*c의 결과 : ",Mul)
print("b/a의 결과 : ",Div)
print("((a+b)+(b-a))-((b*c)/(b-a))의 결과 : ",calc.Result)


# (형식2)
# from 모듈 import *
# => 모듈 내에 있는 모든 변수, 함수와 클래스를 호출
# 
# 모듈에 있는 내용을 사용할 경우 : 함수(변수,클래스)명을 그대로 사용

from calc import *

a = 10
b = 20
c = 30
Sum_re = Sum(a,b)
Sub_re = Sub(b,a)
Mul_re = Multi(a,b)
Div_re = Div(c,a)
Result = Sum_re + Sub_re + Mul_re + Div_re
print(Sum_re)
print(Sub_re)
print(Mul_re)
print(Div_re)
print(Result)

# (형식3)
# from 모듈 import <함수,변수,클래스명>
# => 모듈 내에 있는 특정 변수,함수,클래스를 호출
# 
# 모듈에 있는 내용을 사용할 경우 : 함수(변수,클래스)명을 그래로 사용 

from calc import Sum,Sub,Multi,Div,Result

a = 100
b = 300
c = 10
Sum = Sum(a,b)
Sub = Sub(b,a)
Mul = Multi(b,c)
Div = Div(b,a)
print(Sum)
print(Sub)
print(Mul)
print(Div)
print(Result)
'''
# 패키지 생성 후 사용하기
#  패키지란? 여러 동작과 관련된 모듈을 모아 놓은 것을 의미함.
# 
# (패키지 생성 순서)
#  1. 패키지로 사용할 폴더를 생성
#  2. 패키지 폴더에 묶어서 사용할 모듈을 저장
#   ([주의사항] python 3.3이하 버전에서는 폴더에 "__init__.py"파일을 생성해야 
#   합니다. 파일 안에 내용이 없어도 상관이 없음.)
#  3. 패키지를 import 명령어를 사용하여 불러옴
#   (패키지 풀더 이름이 바로 패키지명이 된다.)
#   from 패키지명 import 모듈명    
#    

from packTest import Sum_mo,Sub_mo,Multi_mo,Div_mo

print(Sum_mo.Sum_func(100,200))
print(Sub_mo.Sub_func(100,200))
print(Multi_mo.Multi_func(100,200))
print(Div_mo.Div_func(100,200))

# Python 파일 입출력 사용
#  -디스크에 파일을 읽어 들이거나
#  -디스크에 파일을 생성하여 저장하는 기능을 의미함.
#  -많은 양의 데이터를 처리(저장)할 때에 유용하게 사용됨.
#  ex) 홈페이지 이미지, 데이터, 음악, 파일 정보등을 저장할 때에... 
# 
# [과정-순서]
#  1. open함수를 이용하여 파일을 열기
#  2. read(읽기) 또는 write(쓰기) 관련 함수를 이용하여 파일에 대한 작업
#    진행 및 처리하는 단계
#  3. open으로 열린 파일의 내용을 close함수를 사용하여 닫아준다.
#      

# 1.open함수 사용
file = open("test.txt","a",encoding="utf-8")
# -test.txt => 작업할 파일명(파일의 경로도 포함)

# -"a" => 모드 영역
# open함수 사용시 모드 설정 값
# r(read-읽기)  => 파일이 있는 경우, 해당 파일에 대해 읽기 동작을 실행
#                 파일이 없는 경우, 에러를 출력(File Not Found!!)
# w(write-쓰기) => 파일이 있는 경우, 파일에 있는 내용을 삭제 후 새롭게 쓰기
#                 파일이 없는 경우, 파일을 생성하고, 쓰기를 진행
# a(append-추가)=> 파일이 있는 경우, 파일에 마지막에 추가로 쓰기 작업을 진행
#                 파일이 없는 경우, 파일을 생성하고, 쓰기를 진행
# * Mode에 "+"를 사용하는 경우, 추가 기능이 사용됨. (읽기와 쓰기 가능함)
# ** 모드에 t => text작업 , b => binary작업
# 
# -encoding : 문자 설정   

# 2. open으로 저장된 내용을 토대로 작업을 진행
str1 = input("파일에 저장할 내용 : ")
i = file.write(str1)
print("file.write()의 반환 값 : ",i)
# 3. 작업한 파일의 내용을 close()로 종료
file.close()

