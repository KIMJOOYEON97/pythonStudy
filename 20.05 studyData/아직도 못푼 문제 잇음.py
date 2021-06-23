'''
i=0
while i<5:
    print("{}번 종속문장 실행".format(i))
    i +=1
else:
    print("조건식이 거짓인 경우에 실행 문장") #반복구문 다 실행한다음에 한번실행. 만약 거짓인 경우 이것만 실행)
print("메인 프로그램 실행 코드")
'''
'''
# 문제6] 다음과 같은 모형으로 출력되게 하세요. (단, 파이썬 서식을 사용안함. ) 서식문자사용X
6-1         6-2         6-3         6-4
*           *****           *       *****
**          ****           **        ****
***         ***           ***         ***
****        **           ****          **
*****       *           *****           *
'''
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
        x +=1
        print("*",end='')
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
print()

i=0
while i<5:
    x=0 #다시 x는 0
    y=4-i   #공백
    if x<=y: #항상 x=0! 이건 반드시 x<=y이어야 함. y가 0일 경우에도 출력이 되야함 
        print(" "*y,end="") #y는 공백
        x=i+1 # 그래서 정해진 횟수돌 때마다 x에 i+1 재할당
        print("*"*x)
    i += 1
print()
#4
for i in range(5):
    for j in range(i):
        print(" ",end="")
    for j in range(5-i):
        print(end="*")
    print()

i=0
while i<5:  # i 0 1 2 3 4
    x=0
    y=5-i 
    if x<y: # x가 항상 0
        print(" "*i,end="") #빈칸은 0 1 2 3 4 이어야하니까 i를 쓰면 됌
        print("*"*y) #y가 5,4,3,2,1이 될 수 있게 #y는 별
    i+=1
print()

count=0
for x in range(2,101):
    flag = True  #True이면 소수 
    #소수 판별... 
    for y in range(2,x):
        if x%y==0:
            flag=False
            break
            #(break) break를 넣지않아도 작동이 되는 이유는???
    if flag:
        print(x,end=" ")  #소수출력
        count += 1
print()
print(count,"개의 소수가 존재함!!")
'''
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
x=y=0; num=1
while num: #num=1 True
    ln=int(input("홀수 줄수를 입력: "))
    flag=True;et=ln//2;star=1
    for x in range(ln):
        for y in range(et):print(" ",end='') #et=3=>공백을 3번 출력 et=2 et=1 x=3 => et=0 //et=1...
        for y in range(star):print("*",end='') #star=1=>별 1번 출력  st=3 st=5 x=3 => st=7 //st=5...
        print()                             #개행
        if x ==(ln//2): flag=False  # x= 0,1,2,3,4,5,6// x==3 flag=False로 멈춤=>else로 넘어감.
        if flag: et-=1; star+=2 # x가 3이하의 수 x=0,1,2,3 ******* => 인쇄 됌 왜냐하면 출력이 앞에 순서
        else: et+=1;star-=2     # x가 3보다 큰 수  x=4,5,6 *****
    num = int(input("계속하겠습니까?[0.종료, 1.계속]"))

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


# 문제3] 1~15까지 랜덤 값을 중복 없이 3개 생성하여 출력하는 코드 작성
from random import random
a,b,c=0,0,0
while True:
    su=int(random()*15)+1
    a=su #su=a 하면 0이 나온다. 왜냐하면 오른쪽에 있는게 왼쪽에 할당되기 때문
    break
while True:
    su=int(random()*15)+1
    if su !=a:
        b=su
        break
while True:
    su=int(random()*15)+1
    if su != a and su !=b:
        c=su
        break
print(a, b, c)


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
'''
#원도 찍어봐라, 별도 찍어봐라
ln=int(input("홀수 줄 수를 입력하세요: "))
snt=0;st=1;et=(ln//2);flag=True
#x,y,j=0,0,0
for x in range(ln):
    for y in range(et): print("-",end="")
    print("*",end="")
    for j in range(snt): print("-",end="")
    print("*",end="")
    for y in range(et): print("-",end="")
    print()
    if x%(ln//2)==0: flag=False
    if flag: 
        et -= 1
        snt +=2
    else: 
        et +=1
        snt -=2
