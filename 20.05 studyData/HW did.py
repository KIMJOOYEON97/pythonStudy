'''
print(0b100)
print(0o100)
print(100)
print(0x100)
print(bin(100))
print(oct(100))
print(hex(100))

print(0b1101010001110001)
print(0x3D5F)
print(hex(1024))
print(hex(3452+5785))
print(sum([0x5C90+0o653]))

print("%s님의 나이는 %d입니다."%("김동완",38))
print("{}님의 나이는 {}입니다.".format("김동완",38))

print("%s님의 무게는 %f입니다."%("김동완",75.5))
print("{}님의 무게는 {:f}입니다.".format("김동완",75.5))

print("%10d원\n%10d원" %(10000,200000))
print("{:10}원\n{:10}원".format(10000,200000))

print("%5d %05d" %(1,1))
print("{:5}{:05}".format(1,1))

print("{:,}".format(1000000))
print("다음 라인으로\n이동")
var=input("정수 입력: ")
print("{}을 입력 받았습니다".format(var))

var1=input('문자열 입력 : ')
var2=input('정수 입력 :')
print("{}".format(type(var1)))
print("{}".format(type(var2)))

print("|{:-<40,.4f}|".format(12303499))

age=input("나이 : ")
name=input("이름 : ")

year=int(input("몇 년도 인가?:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("{}년도는 윤년입니다.".format(year))
        else:
            print("{}년도는 평년입니다.".format(year))
    else:
            print("{}년도는 윤년입니다.".format(year))
else:
    print("{}년도는 평년입니다.".format(year))

# 3)각 숫자의 자리를 구할 때 사용 
    # 123의 값의 각 자리 수 구하기 
    # 1의 자리:123%10 =>3
    # 10의 자리:(123//10)%10 =>2 
    # 100의 자리: (123//100)%10 =>1 
# 4)범위 내에 숫자를 구할 때 ????????
    # 어떤 값을 넣어도 1~6 사이의 값을 출력 
    # => (x%6)+1 
    #     x%6=>(0,1,2,3,4,5)+1


#(6) 비트 연산자 : 두 피연산자의 bit값을 가지고 처리하는 연산자들을 의미함.((2진수로 변환하여)bit값으로 연산)

#\print((276//10)%10)
x=int(input("숫자를 넣으시오"))
print((x%3)+1)

print("오늘도 여러분 홧팅합시다.\r내일도")

##파이썬의 내장 함수
# -max() : 최대값 구하는 함수
# -min() : 최소값 구하는 함수
# -sum() : 주어진 값의 합을 구하는 함수
# -pow() : 제곱승수 값을 구하는 함수
# -divmod() : 나누기를 구하는 함수(몫,나머지)
 
print(max(2,3,5,-7,9,-8,1))
print(min(2,3,5,-7,9,-8,1))
print(sum([2,3,5,-7,9,-8,1]))
print(pow(10,3))
print(divmod(10,3))

# 2. 절대값 구하는 프로그램을 만드세요
x= int(input("[절대값]을 구해드립니다. : "))
if x<0: x=-x;print("{}입니다.".format(x))
else: print("{}입니다.".format(x))
#문제1].사용자로부터이름, 키, 체중값을입력받아비만도를구하고 //등급이 적혀잇음
# 결과를출력할때비만도값100을기준으로100 미만이면저체중, 
# 100 이상110 미만은정상, 110 이상120 미만과제중, 120 이상130 미만비만, 130 이상은고도비만으로출력하시오.
#비만도계산식: 비만도(%) = 현재체중/ 표준체중* 100
#표준체중계산식: 표준체중= (현재키–100) * 0.9
#출력예제: 홍길동님의비만도는112.15% 로과체중입니다.

x=input("사용자의 이름: ")
y=float(input("{}님의 키를 입력하세요.: ".format(x)))
z=float(input("{}님의 몸무게를 입력하세요.: ".format(x)))
avg=(y-100)*0.9
fat=y/avg*100
if fat<100:level="저채중"
elif fat>=100 and fat<110: level="정상" 
elif fat>=110 and fat<120: level="과체중" 
elif fat>=120 and fat<130: level="비만" 
else: level="고도비만"
print("{}님의 비만도는{:.2f}%로 {}입니다.".format(x,fat,level))

#문제3]윤년을구하는코드를작성하시오.
#-4의배수는윤년이된다. 그외는평년
#-4의배수면서100의배수인경우는평년이다. 그외는윤년
#-4 그리고100의배수이면서400의배수인경우윤년이다.
year = int(input("년도를 입력하세요. :"))
if year%4==0:
    if year%100==0:
        if year%400==0:print(year,"년은 윤년입니다.")
        else: print(year,"년은 평년입니다.")
    else: print(year,"년은 윤년입니다.")
else:  print(year,"년은 평년입니다.")

for x in range(10): print(x,end=" ")
print()
for x in range(5,10): print(x, end=" ")
print()
for x in range(1,10,2): print(x, end=" ")
print()
for value in 'String':
    print(value*5,end=" ")
print()

x= int(input("숫자입력: "))
while x<10:
    print("x는 뭐다")
    x=x+1

#예제4]for문(range()4) -증감값
for x in range(10,0,-2):
    print(x, end=" ")
print()

# 예제5] for문- 문자열 (자바에도 잇음)
Sum=0
for x in 'string':
    print(x,end="") #end="" : Null
    Sum += 1        #반복구문이 등장할때마다 1씩 증가.
print();print(Sum)


#int() 함수의 확장사용
print(int('0xA',16))  #base=10 : 숫자를 10진수로 읽어드림 16:16진수값에 맞게 변환 시켜줌
print(int('0b1010',2))
print(int('A',16))
print(int('1010',2))
#진수값으로 변환시켜서 보여줌
print(0xA)
print(0b1010)
print(int('A',16))
print(int('101',8))
print("{:_>15,.2f}".format(1000))
print("|{:_>15,.2f}|".format(1000))


for x in range(1,10):
    for y in range(2,10):
        print("{}x{}={:<3}".format(y,x,x*y), end=" ")
    print()
for x in range (5):
    for y in range (x+1):
        print("*",end='')
    print()
print()

for x in range (1,6):
    for y in range (6-x):
        print("*",end='')
    print()
print()

for x in range (5):
    for y in range (x+1):
        print(" ",end='');print("*",end='')
    print()
print()

# 예제1]while구문을 이용한 반복문(짝수의 합, 홀수의 합)


import turtle
num = int(input(" 3 ~ 12까지 다각형 그리기 : "))
if num >=3 and num <=12:
    for x in range(num):
        turtle.forward(100)
        turtle.left(360/num)
    turtle.mainloop()
else:
    print("그럴수 없습니다.")

a=int(input("몇 각형을 그리겠습니까?: "))
import turtle
while 3<=a<=12:
    turtle .forward(100)
    turtle .left(360/a)
    turtle .mainloop
    if a==3:
        break 
else:
    print("그릴 수 없습니다.")

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

# 문제3] 1~15까지 랜덤 값을 중복 없이 3개 생성하여 출력하는 코드 작성\
from random import random
a,b,c=0,0,0
while True:
    su=int(random()*15)+1
    a=su
    break
while True:
    su=int(random()*15)+1
    if a!=b:
        b=su
        break
while True:
    su=int(random()*15)+1
    if a!=b and b!=c:
        c=su
        break
print(a,b,c)

# 변수를 선언하여 3개의 정수를 입력받아 합을 출력하는 코딩
# 출력결과>> "합계 = xx " "합계"도 변수로 저장하여 사용
a=int(input("정수를 입력하세요: "))
b=int(input("정수를 입력하세요: "))
c=int(input("정수를 입력하세요: "))
d= "합계 ="
lst=[d,a,b,c]
print(lst[0],a+b+c)

lst1 = [9, 10, 3, 2, 6, 1, 7, 8, 4, 5]
lst2 = sorted(lst1)  
lst3 = sorted("I am a student".split()) 
lst5 = sorted("I am a student") 
print(lst2)
print(lst3)
lst4 = sorted("I am a student".split(),key=str.lower)  
print(lst4)
print(lst5)

# 예제 4] 멤버연산자, 식별연산자를 이용한 if
x=15 #변수선언
if x in (10,11,15):
    print("x변수의 값은 Members에 속해 있습니다.")
if type(x) is int:  #int인지 아닌지 타입 구분
    print("x변수의 값을 INT형 자료입니다.")
    
a= 0
if a==0:
    pass #나중에 코드를 입력할 예정,주석으로 설명
    print(a) #실행을 안하는 것은 아니다. indendtion error가 안뜸
print(a)

tup=(('a','b'),('c','d'),('e','f'))
for val in tup:
    print(val[0],val[1])

# 문제 1.numbers = (10, 20, 30, 40, 50, 60, 70)
# 위 튜플 자료에서 30과 40을 따로 num1, num2 변수에 할당하시오.
numbers = (10, 20, 30, 40, 50, 60, 70)
idx1=numbers.index(30)
idx2=numbers.index(40)
num1=numbers[idx1]
num2=numbers[idx2]
print(num1,num2)

# 문제 2.menu = (('칼국수', 6000), ('비빔밥', 5500), ('돼지국밥', 7000))
# 위 자료의 값을 다음의 양식처럼 출력하시오.
#칼국수-6,000원
#비빔밥-5,500원
#돼지국밥–7,000원
menu = (('칼국수', 6000), ('비빔밥', 5500), ('돼지국밥', 7000))

for x in range(len(menu)):
    for y in range(1):# range(2)하면 [0][1][2]가 됌 [2]없음>> IndexError Tuple index out of range
        #y+=1  #[1]부터 시작해서 가격만 나오게 됌
        print(menu[x][y],end=" ")
        print("-{}원".format(menu[x][y+1])) #[y+1] 가격 나오게 할려면 index가 [1]이어야함
        
for val in menu:
    print("{} - {}원".format(val[0],val[1]))  #.format(val[0][1]) >IndexError Tuple index out of range
                                            #val=("칼국수",6000)  >이중 튜플이 아님으로 범위를 넘어간거임
                                            #      val[0],val[1]




menu=(('칼국수',6000),('비빔밥',5500),('돼지국밥',7000),('김밥',2000),('라면',2500))
#김밥과 라면 가격 각각 출력
num1=menu[3][1]
num2=menu[4][1]
print("김밥: {}원 ,라면: {}원".format(num1,num2))
# 가격이 7000에 해당하는 메뉴출력
for i in menu:
    if i[1] ==7000:
        print(i)

print()
# 가격이 6000원 이하인 메뉴 출력
menu=(('칼국수',6000),('비빔밥',5500),('돼지국밥',7000),('김밥',2000),('라면',2500))
for i in menu:
    if i[1]<6000:
        print(i[0])
    else:
        continue
    #else:         =>답이 아무 것도 안나오는 이유?
    #    break       처음에 칼국수가 6000이다. 그래서 if 구문에 들어가지 않고 else 구문에 들어가서 break가 됌.
# 사용자 입력으로 메뉴를 입력 받아 해당하는 메뉴 가격을 출력
# 사용자입력으로 1개 이상의 메뉴를 입력받아 해당 메뉴의 총 가격을 출력하시오(exit를 입력하면 더 이상의 입력 받지X) 

# [ Tuple 종합 문제 ]
#1. 여러 개의 값을 패킹시킨 후 저장되어 있는 값을 빼내어 
#  출력 하시오. (5개 값 저장)
#( Tuple의 값을 리스트에 저장하시오. 단, Len함수를 이용)
tu='금요일',20200605,8,'달걀샐러드','hello'
lst=[]
for x in range(len(tu)):
    lst.append(tu[x])
print(lst)

#2.아래와 같이 출력 시키시오
#----------------------------------------------------
#     (Tuple)          (List)
#    회사정보     :   삼성전자
#    제품명       :    Galaxy
#    가격정보     :    100원
#    출시일       :    미정
#----------------------------------------------------
tu = '회사정보','제품명','가격정보','출시일'
lst = ['삼성전자','Galaxy','100원','미정']
print("-"*40)
print(" "*5,"(Tuple)\t\t","(List)")
for x in range(len(tu)):
    print(" "*5,"{}\t:\t{}".format(tu[x],lst[x]))
print("-"*40)

#3. 위에서 출력 한 내용을 업데이트 하시오. 
#[ 단, Index, Insert, Remove 함수를 전부 사용할 것 ]
#가 격 : 100 -> 110
#출시일 : 미정 -> 이번 달 말
a= lst.index("100원")
lst.remove("100원")
lst.insert(a,"110원")
b = lst.index("미정")
lst.remove("미정")
lst.insert(b,"이번 달 말")
tu = '회사정보','제품명','가격정보','출시일'
lst = ['삼성전자','Galaxy','100원','미정']
print("-"*40)
print(" "*5,"(Tuple)\t\t","(List)")
for x in range(len(tu)):
    print(" "*5,"{}\t:\t{}".format(tu[x],lst[x]))
print("-"*40)

# <<아래의 내용을 토대로 프로그램을 작성해보세요.>>
# 1. 다음과 같은 메뉴와 가격을 key와 value로 사용하여
# 사전형 자료를 만들어보세요(변수명은 menu)
#  칼국수(6000원), 비빕밥(5500원), 돼지국밥(7000원),
#  돈까스(7000원), 깁밥(2000원), 라면(2500원) 
menu={'칼국수':6000,'비빔밥':5500,'돼지국밥':7000,'돈까스':7000,'김밥':2000,'라면':2500}
# 2. 위에서 만든 사전형 자료 menu 변수에서 가격이 6000원 미만에
# 해당하는 메뉴와 가격을 출력하는 코드를 작성하세요. 
for x in menu:
    if menu[x] <6000:
        print(x,menu[x],"원")

# 3. 사용자 입력으로 메뉴와 가격을 입력 받아  menu 변수에 자료를
# 추가 할 수 있도록 하시오.(동일한 메뉴는 가격만 변경)
me=input("메뉴를 입력하세요: ")
p=int(input("가격을 입력하세요: "))
for x in menu:
    if x ==me:
        menu.pop(x)
        menu.update({x:p})
    if x !=me:
        menu.update({me:p})
print(menu)



#멤버연산자를 사용해서 해보기

#update의 특성을 이용해서 해보기

#[ Quiz ] : List 정의하여 첨자 위치 저장
# a의 총 개수와 첨자의 위치를 출력 하시오
# st = 'Have a nice day Have a nice day Have a nice day'
#  
#결과 
#a 개수 : 9
#첨자 : [1, 5, 13, 17, 21, 29, 33, 37, 45]
st = 'Have a nice day Have a nice day Have a nice day'
lst=[]
idx=0
cnt=0
while True:
    idx=st.find('a',idx)
    lst.append(idx)
    idx=idx+1
    cnt +=1
    if st.find('a',idx)==-1:
        break
print("a 개수:",cnt);print("첨자 : ",lst)

#  3)find를 사용하여 첫번째, 두번째, 세번째, 네번째 'a'의 위치를 
#   출력하세요.#while구문 사용
str3 = "Have a nice day"
dic={}
idx=0
cnt=0
while True:
    idx = str3.find('a',idx)
    idx = idx +1
    cnt +=1
    dic.update({cnt:idx})
    if str3.find('a',idx)==-1:
        break
for k in dic:
    print("{}번째 'a'의 위치 : {}".format(k,dic[k]))


#질문  choice함수   #choice함수할 때 x변수값을 받아서 하는 게 좋다. choice함수 자체를 사용하면 choice가 계속 돌아갈 수 있다.
from random import choice
while True:
    dice=[1,2,3,4,5,6]
    x = choice(dice)
    if x != 6:
        print(x,end="/")
    else:
        print()
        sel=input("계속하시겠습니까?(Y/n): ")
        if sel == 'n':
            print("프로그램 종료")
            break
        else:
'''
#import random
#d = {'VENEZUELA':'CARACAS', 'CANADA':'TORONTO'}
#country, capital = random.choice(list(d.items()))
# 임의의 키 값: random.choice(list(d.keys()))
# 임의의  밸류 값:random.choice(list(d.values()))
# 임의의 키와 값:random.choice(list(d.items()))
#   

# 4. 메뉴를 자동으로 선택하여 출력하게 만들어 보세요.   
#        menu=list(menu);print(menu) =>['칼국수', '비빔밥', '돼지국밥', '돈까스', '김밥', '라면']
'''
menu={'칼국수':6000,'비빔밥':5500,'돼지국밥':7000,'돈까스':7000,'김밥':2000,'라면':2500}
while True:
    num=input("1.메뉴 자동선택\n2.종료")
    if num =='1':
        x,y=menu.popitem()
        print(x,":",y)
    else:
        print("메뉴출력을 중단합니다.")
        break

from random import choice
menu={'칼국수':6000,'비빔밥':5500,'돼지국밥':7000,'돈까스':7000,'김밥':2000,'라면':2500}
while True:
    num=input("1.메뉴 자동선택\n2.종료")
    if num =='1':
        x,y=choice(list(menu.items()))
        print(x,y)
    else:
        print("메뉴출력을 중단합니다.")
        break
# 3. 계산기를 입력,출력,연산기능으로 나눠서 실행되게 
#    작성해 주세요.
def calc(num1,num2,giho):
    if giho =='+':
        return num1+num2
    elif giho =='-':
        return num1-num2
    elif giho =='*':
        return num1*num2
    elif giho =='/':
        return num1/num2
    else:
        return "계산할 수 없습니다."
def display(num1,num2,giho,result):
    print(num1,giho,num2,'=',result)
def put():
    giho,num1,num2=input("어떤 연산을 할건가요?(+,-,*,/): "),int(input("첫번째 숫자를 입력하세요: "))\
    ,int(input("두번째 숫자를 입력하세요: "))
    result=calc(num1,num2,giho)
    display(num1,num2,giho,result)

put()
'''
# 4. 예제 거꾸로 수를 반환하는 함수를 계산,출력 
#    기능으로 나눠서 작성해 주세요
#    예) 123 => 321
#        if result==0: =>작동이 안됌
#            break
#    return su//10
def reversesu(num):
    a,su=0,0 #while 구문안에 있으면 계속 0으로 리셋되서 1의자리수만 나옴
    while True: 
        a = num%10
        num = num//10
        su=(su+a)*10
        if not num: #if num != 0: 하면 일의 자리 한자리수만 나온다. ??? 왜 안되는지? =>if가 0이 아니게 되었을 때 실행하면 한번만 반복하게 됌
            return su//10 #num이 0이 되었을 때만 실행하시오.//

def Input():
    num=int(input("숫자를 입력하세요: "))
    su=reversesu(num)
    print(su)

Input()