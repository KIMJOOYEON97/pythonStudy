'''
Sum=0
for x in 'string':
    print(x,end="") #end="" : Null
    Sum += 1        #반복구문이 등장할때마다 1씩 증가.
print();print(Sum)


Sum=0
for x in range(10):
    for y in range(10):
          # Sum = Sum + 1
        print(x,y)
        Sum += 1
    print("-"*40)
print(Sum)

i=0
while i<5:
    print("{}번 종속문장 실행".format(i))
    i +=1
else:
    print("조건식이 거짓인 경우에 실행 문장") #반복구문 다 실행한다음에 한번실행. 만약 거짓인 경우 이것만 실행)
print("메인 프로그램 실행 코드")

i=5
while i<5:
    print("{}번 종속문장 실행".format(i))
    i +=1
else:
    print("조건식이 거짓인 경우에 실행 문장") #반복구문 다 실행한다음에 한번실행. 만약 거짓인 경우 이것만 실행)
print("메인 프로그램 실행 코드")

#break
while True:
    a=int(input("정수 입력[0입력시 종료] : "))
    if a==0:
        break  #조건식을 나감 반복을 멈춤
    a+=1
    print("입력값 출력 : ",a)

#continue 이용
a=0
while a < 5: #0~5까지 5번 반복 
    if a==3:  #a==3이면 참이 됨으로 바로 조건식으로 이동해서 3이 출력X //나가지 않지만 조건식을 반복해서 본다
        continue
    a+=1
    print("a={}".format(a))

a=0
while a < 8: #0~5까지 5번 반복 
    if a==5:  #a==3이면 참이 됨으로 바로 조건식으로 이동해서 3이 출력X //나가지 않지만 조건식을 반복해서 본다
        continue
    a+=1
    print("a={}".format(a))
'''
from random import random,randint
while True:
    x=randint(1,6) 
    if x==1:
        break
    print(x,end =" ")

lst1 =[1,2,3,4,5]
lst2 =lst1
print("lst1의 값 :",lst1,"lst1의 주소 값: ",id(lst1))
#id()는 변수나 함수의 주소 값을 반환하는 함수
print("lst2의 값 :",lst2,"lst2의 주소 값: ",id(lst2))
lst1[1]='a'
print(lst1)
print(lst2)

# (예) deep copy -데이터에 대한 공간을 별도로 만들어서 복사하는 것/ 같은 공간에 저장 X //각각 개별적 공간에 값을 저장
lst1 = [1,2,3,4,5]
lst2 = list(lst1)
lst1[1] ='a'
print("lst1의 값 : ",lst1,"\tlst1의 주소값: ",id(lst1))
print("lst2의 값 : ",lst2,"\tlst2의 주소값: ",id(lst2))

import copy

lst1=[1,2,3,4,5]
lst2 = copy.deepcopy(lst1)  #deep copy 함수
lst3=lst1
print(lst1,lst2)
print(id(lst1),"\t",id(lst2),"\t",id(lst3))
lst2[0]=100;lst1[0]=300
print(lst1,lst2,lst3)


# strip() : 양쪽에 인자로 전달 받은 문자열을 제거   *()소괄호 안에 들어가는 값이 인자
#           인자값이 없는 경우, 공백을 제거
st='     python string     '
print("[{}]".format(st))    #[     python string     ]
st1=st.strip()              #.format도 문자열 함수 이다.
print("[{}]".format(st1))   #[python string]
print()
print(st1,"study")

# lstrip()
st2 =st.lstrip()
print("[{}]".format(st2))   #[python string     ]
print()
print(st2,"study")

# rstrip()
st3 =st.rstrip()
print("[{}]".format(st3))   #[     python string]
print()
print(st3,"study")

from random import choice
dice =[1,2,3,4,5,6] 
x= choice(dice)
print(x) #dice 리스트 내에 있는 멤버중 하나를 추출하여 출력 
'''
def paycalc(s=8500,d=8,m=30):
    tot=s*d*m
    print("{:,}원".format(tot))

import os
while True:
    os.system('cls')
    print("1. 기본급")
    print("2. 일한 날짜 입력")
    sel=input("번호 입력 >> ")
    if sel=='1':
        paycalc()
        os.system('pause')
    elif sel=='2':
        um=int(input("일한 날짜를 입력하세요: "))
        paycalc(m=um)
        os.system('pause')
    else:
        print("잘못된 선택입니다.") 

def alba(day=30):
    time=8;price=8500
    re = time * price * day
    return re   #re는 처리된 나머지 결과값.

def display():
    import os
    while True:
        os.system('cls')
        num = input("<<시급 계산 프로그램>>\n1. 기본급\n2.일한 날짜 입력\n0.종료\n번호입력>>")
        if num == '1':
            ret = alba() #result값 받기 #숫자값을 변수에 저장// 나중에 변수에 class를 저장하기도 한다.
            print("당신의 급여는 {:,}원 입니다.".format(ret))
            os.system('pause')
        elif num == '2':
            day =int(input("일한 일수 입력 : "))
            ret=alba(day)
            print("당신의 급여는 {:,}원 입니다.".format(ret))
            os.system('pause')
        elif num == '0':
            print("종료합니다.")
            os.system('pause')
            break
        else:
            print("잘못된 입력입니다.")
            os.system('pause')

#메인
display()

#다음 조건을 보고 회원가입을 위한 프로그램 코드를 작성 하시오
# -아이디는 반드시 10자리 이상
# -패스워드는 반드시 8~16자리 사이
# -패스워드에 아이디가 포함되면 안됨
# -패스워드에는 담음의 특수문자가 반드시 하나 이상 포함(~,!,@,#,$,%,^,&,*,_,?)

# menu=[['칼국수',6000],['비빔밥',5500],['돼지국밥',7000],['돈까스',7000],['김밥',2000],['라면',2500]]   
# 사용자 입력으로 메뉴와 가격을 입력받아 menu변수에 자료를 추가 할 때 
# 기존에 동일한 메뉴가 존재하는 경우 가격만 변경되도록 코드를 작성
#TypeError: 'list' object cannot be interpreted as an integer
# 진짜 오지게 시간 들엇음 
menu=[['칼국수',6000],['비빔밥',5500],['돼지국밥',7000],['돈까스',7000],['김밥',2000],['라면',2500]]
s=input("변경할 메뉴 입력 : ")
p=int(input("변경할 가격입력 : "))
flag = 0
for i in range(len(menu)):
    for j in range(1):
        if menu[i][j]==s:
            value = menu[i]
            menu.remove(value)
            menu.append([s,p])  
        j += 1
    i += 1
if flag == 0:
    menu.append([s,p])
print(menu)


menu={'칼국수':6000,'비빔밥':5500,'돼지국밥':7000,'돈까스':7000,'김밥':2000,'라면':2500}  

tot = 0;lst=[]
while True:
    import os
    os.system('cls')
    print("'칼국수',6000\n'비빔밥',5500\n'돼지국밥',7000\n'돈까스',7000\n'김밥',2000\n'라면',2500")
    s=input("메뉴를 입력하세요:")
    if s not in menu:
        print("다시입력하세요")
        os.system('pause')
        continue
               #메뉴를 잘못 입력했을 경우 ex) 칼수국 했을 때 다시입력하세요라고 나오게 하는 방법
    p=menu[s]
    lst.append(s)
    tot=tot +p
    sel=input("계속하시겠습니까?(Y/n)")
    if sel != 'n':
        continue
    else:
        print(lst,"총 가격 :",tot,"원")
        os.system('pause')
        break
'''
menu=[['칼국수',6000],['비빔밥',5500],['돼지국밥',7000],['돈까스',7000],['김밥',2000],['라면',2500]]
tot = 0;lst=[]
while True:
    import os
    os.system('cls')
    print("'칼국수',6000\n'비빔밥',5500\n'돼지국밥',7000\n'돈까스',7000\n'김밥',2000\n'라면',2500")
    s=input("메뉴를 입력하세요:")
    for i in range(len(menu)):
        if s not in menu[i]:
            print("다시입력하세요")
            os.system('pause')
    for x in range(len(menu)):
        if menu[x][0]==s:
            p = menu[x][1]       
    tot += p

    lst.append(s)
    
    sel=input("계속하시겠습니까?(Y/n)")
    if sel != 'n':
        continue
    else:
        print(lst,"총 가격 :",tot,"원")
        os.system('pause')
        break

# 사용자가 입력한 정수 값에 대해 2진수로 변환하여 출력하는 코드를 작성하시오  
user =int(input("수를 입력하세요: "))
print(bin(user))
#100~51까지의 정수 값 중 홀수 해당하는 값 만을 출력하는 코드를 작성하시오
lst =[]
for x in range(51,101):
    if x%2 != 0:
        lst.append(x)
    x +=1
print(lst)

lst =[]; x=51
while x<101 and x>=51:       #while x<101 and x>51:  왜 빈 리스트만 뜰까?
    if x%2 != 0:
        lst.append(x)
    x +=1
print(lst)
