i=0
while i<5:
    print("{}번 종속문장 실행".format(i))
    i +=1
else:
    print("조건식이 거짓인 경우에 실행 문장") #반복구문 다 실행한다음에 한번실행. 만약 거짓인 경우 이것만 실행)
print("메인 프로그램 실행 코드")
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
    x=0
    y=4-i
    j=i+1    
    while x<j:
        x +=1
        print("*",end="")
    while x<y:
        x +=1
        print(" ",end="")
    i+=1    
    print()
print()

#4
for i in range(5):
    for j in range(i):
        print(" ",end="")
    for j in range(5-i):
        print(end="*")
    print()

i=0
while i<5:
    x=0
    j=(i+1)-1
    y=5-i
    while x<j:
        x+=1
        print(" ",end="")
    while x<y:
        x+=1
        print("*",end="")    

    i +=1
    print()
print()

count=0
for x in range(2,101):
    flag = True  #True이면 소수 
    #소수 판별... 
    for y in range(2,x):
        if x%y==0:
            flag=False
            #(break) break를 넣지않아도 작동이 되는 이유는???
    if flag:
        print(x,end=" ")  #소수출력
        count += 1
print()
print(count,"개의 소수가 존재함!!")
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

x,y=0,0; num=1
while num:
    ln=int(input("홀수 줄수를 입력: "))
    flag=True;et=ln//2;star=1
    for x in range(ln):
        for y in range(et):print(" ",end='')
        for y in range(star):print("*",end='')
        print()
        if x ==(ln//2): flag=False
        if flag: et-=1; star+=2
        else: et+=1;star-=2
    num = int(input("계속하겠습니까?[0.종료, 1.계속"))

import os # os는 파이썬에서 제공하는 기본 라이브러리 
          # os와 관련된 함수들이 저장된 모듈 
          # system() => os의 시스템 명령어를 사용하게함
'''
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
'''