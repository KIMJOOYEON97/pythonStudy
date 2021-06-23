'''
# 문제6] 다음과 같은 모형으로 출력되게 하세요. (단, 파이썬 서식을 사용안함. ) 서식문자사용X
6-1         6-2         6-3         6-4
*           *****           *       *****
**          ****           **        ****
***         ***           ***         ***
****        **           ****          **
*****       *           *****           *
'''
for i in range(5):
    for y in range(i+1):
        print("*",end='')
    print()
print()
#or
i=0
while i<5:
    x=0
    j=i+1
    while x <j:
        print("*",end='')
        x +=1
    print()
    i +=1
print()

#2
for i in range(5):
    for y in range(5-i):
        print("*",end='')
    print()
print()
#or
i=0
while i<5:
    x=0
    y=5-i
    i +=1
    while x <y:
        print("*",end='')
        x +=1
    print()
    
print()
#3
for i in range(5):
    for j in range(4-i):
        print(" ",end="")
    for j in range(i+1):
        print(end="*")
    print()

#4
for i in range(5):
    for j in range(i):
        print(" ",end="")
    for j in range(5-i):
        print(end="*")
    print()
'''
6-5 출력 줄수를 입력하면 다음과 같이 출력
  입력 줄은 홀수이여야만 함. 
  hint:별,공백,줄수,반복문을 위한 변수,flag(booL): 반전을 줄 수 있는 신호
홀수 줄수를 입력: 7
   *        st: 줄이 바뀔때마다 +2(줄수의 반)/반 넘으면, -2
  ***       sp: 줄수를 //2(초기값), 줄수의 반 전 -1,후 +1
 *****      
*******
 *****
  ***
   *
'''
'''
star="*"
et=" "
while True:
    line=int(input("홀수 줄수를 입력: "))
    for x in range(line+1):
        flag=True
        if x%2==0:
            flag=False
            continue
        if flag:
            print((line-x)//2*et,end="");print(x*star)
        if x==line:
            print(line+x)

import os # os는 파이썬에서 제공하는 기본 라이브러리 
          # os와 관련된 함수들이 저장된 모듈 
          # system() => os의 시스템 명령어를 사용하게함

i,j=0,0 ;num=1
while num:
    os.system("cls")  #"cls"는 위에 있는 것 날려줌
    ln= int(input("홀수 줄수를 입력 :"))
    sp=ln//2;st=1;flag=True  #flag=반전을 위한 값
    for i in range(ln):
        for j in range(sp):print(end=" ")  #공백
        for j in range(st):print(end="*")  #별
        print() #줄바꿈
        if i == (ln//2): flag=False
        if flag: sp-=1; st+=2
        else: sp+=1;st-=2
    num = int(input("계속하겠습니까?[0.종료,1.계속] : "))


# 랜덤 함수
# : 임의의 값을 출력하는 함수.
# (랜덤처럼보이는 계산, 퍼센트연산의 특성을 이용한 계산연산) =>가상랜덤
# 100집어 넣으면 10나오고 또 100집어넣으면 10이나옴.<컴터는 계산기니까> 
# 어떤 숫자(seed값,원형값)을 집어넣느냐에 따라 다름 =>매번 다른 값을 넣어야함 ==>원형값이 중요!
# => 시간을 쓴다(같은 간격으로 늘려나지만 값이 늘 바뀜)
# 생성되는 값을 "난수"라고 한다 ("난수">통신할때 많이쓰는 알고리즘)
#  
# 랜덤 함수를 사용하기 위한 모듈 : random 모듈
#  
# 모듈 사용 방법: import [모듈명]
#   ex) import random #랜덤 모듈 전제를 로딩
#   or
#   ex) from random[모듈] import random[함수] #랜덤 모듈에서 random()를 로딩
#..import turtle import os 

from random import random   #정육각형은 함수 심볼

print(random())             #0.0 ~ 1.0 미만의 값을 출력(float)
print(random()*10)          #0.0 ~10.0 미만의 값을 출력(float)
print(int(random()*10))     #0~10미만의 값을 출력(int)
print(int(random()*10)+1)   #1~10까지의 값을 출력(int)

# 예제1] 1 ~45 까지의 임의의 값 6개를 출력
from random import random

for x in range(6):
    print(int(random()*45)+1,end=' ')   #임의의 값 1 ~45사이의 숫자
print()
'''
# 문제1] 1~100 까지 랜덤 값을 6개 출력하는 코드를 작성하세요.
from random import random
for x in range(6):
    print(int(random()*100)+1,end=' ')
print()

# 문제2] 1~100까지 랜덤 값을 반복하여 출력하되, 출력 값이 50이 출력되는 순간 반복을 종료하는 코드를 작성하세요. 
from random import random
while True:
    x=int(random()*100)+1
    print(x,end=' ')
    if x==50:
        break
print()
# 문제3] 1~15까지 랜덤 값을 중복 없이 3개 생성하여 출력하는 코드 작성
from random import random
count=0; num=1
while num:
    count+=1
    x=int(random()*15)+1
    print(x,end=" ")
    if count==3:
        break

#풀이
from random import random
num1,num2,num3=0,0,0

while True:
    su = int(random()*15)+1
    if num1 != su:
        num1=su
        break
while True:
    su = int(random()*15)+1
    if num1 != su and num2 !=su:
        num2 = su
        break
while True:
    su = int(random()*15)+1
    if num1 != su and num2 != su and num3 !=su:
        num3 =su
        break
print("{} {} {}".format(num1,num2,num3))

# random 모듈내에 있는 다른 형태의 random함수들....
# -randint():임의의 값을 출력하는 int값 랜덤 함수
# 
# 사용방법
#   randint(a,b) 
#         a:시작값 b:마지막값 =>시작값부터 마지막값까지의 랜덤
#예시)1~6까지의 임의의 값 출력하는 예시
from random import random,randint

print(randint(1,6))         #1~6사이의 임의의 정수를 출력
print(randint(100,200))     #100~200사이의 임의의 정수 출력

#또 다른 random함수
# -randrange(): 범위 내에 있는 임의 값을 출력 <random+range>
# 
#  예시1) 
#   randrange(5,10)   => 5~10미만의 값을 출력([5,6,7,8,9]중 하나)
#  예시2)
#   randrange(5,10,2)  => 5~10미만까지 2씩 증가 값을 출력([5,7,9]중 하나)

#예제 3]
from random import random,randint,randrange
print(randrange(10))        #[0,1,2,3,4,5,6,7,8.9]중 하나
print(randrange(5,10))      #[5,6,7,8,9]중 하나
print(randrange(5,10,2))    #[5,7,9] 중 하나

# random 모듈 내에 choice()함수
# : 이 함수의 특징은 리스트와 같은 형태(Sequence)의 자료 중 일부를 랜덤하게 추출하는 함수
# 
# 예시) dice =[1,2,3,4,5,6] 
# choice(dice) #dice 리스트 내에 있는 멤버중 하나를 추출하여 출력 

#예제4]
import random
dice=[1,2,3,4,5,6]
x = random.choice(dice) #.=참조연산자 모듈내에 있는 초이스를 불러오겠다 turtle.forward 같은 것.
print(x)
#or
from random import random,choice,randint,randrange #모듈에 있는 특정함수들을 불러온것.
dice=[1,2,3,4,5,6]
x=choice(dice)
print(x)

#문제4] 1~99까지 랜덤 값 중에는 짝수는 True, 홀수면 False출력하는 프로그램 코딩
from random import randrange
for x in range(1):
    if x%2==0:
        print(randrange(1,100,1),"True")
    if x%2==1:
        print(randrange(1,100,1),"False")

#풀이
from random import random
print("출력 결과 : ",end="")
rand = int(random()*99)+1
if rand%2==0:
    print("True({})".format(rand))
else:
    print("False({})".format(rand))

#ftp참조자료 폴더에 "ascii코드표.png"파일을 보고 외우기