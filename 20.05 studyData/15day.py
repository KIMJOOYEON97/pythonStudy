# strip(): 양쪽에 있는 공배 또는 문자를 제거 #웹프로그램 할때 양끝에 문자가 이상한 것 붙을 때 보안상 제거.
st="   파이썬   "
print("[{}]".format(st))
print("[{}]".format(st.strip()))

st2="파이썬파"
print(st2)
print(st2.strip("파"))  #이썬
print(st2.lstrip("파")) #이썬파
print(st2.rstrip("파")) #파이썬

st3="---파이썬---" #글자가 다른 글자가 나오기 전까지. 
print(st3)
print(st3.strip("-"))       #파이썬
print(st3.lstrip("-"))      #파이썬---
print(st3.rstrip("-"))      #---파이썬

#replace()함수 사용
st="2015-06-05"
#   0123456789 (index)
print(st)   
print(st.replace('2015','2020'))    #2020-06-05
print(st[0:4])      #2015           #특정 위치를 지정
print(st.replace(st[0:4],'2020'))   #2020-06-05 #2015의 값을 슬라이싱으로 지정
#find와 replace같이 써도 좋음//replace만 써도 됌 replace가 find의 찾는 역할도 함으로.

#split(str) : 특정문자(str)를 기준으로 문자열을 나누는 함수 =>리스트 저장
st ="Never Ever Give Up"
a=st.split()    #공백을 기준으로 나눔
print(st)
print(a,type(a))    #['Never', 'Ever', 'Give', 'Up'] <class 'list'>

st2 = "하나:둘:셋"
st3 = "1,2,3"
b=st2.split(":")
c=st3.split(",")
print(b,type(b))    #['하나', '둘', '셋'] <class 'list'>
print(c,type(c))    #['1', '2', '3'] <class 'list'>

st4 = "하나둘셋넷"
d = st4.split()     #split은 무조건 list에 저장한다.
print(d,type(d))    #['하나둘셋넷'] <class 'list'> 하나의 리스트 선언.

# splitlines() : 개행(\n)을 기준으로 문자열을 나누는 함수 => 저장은 리스트  #문장이나 문단 단위로 쓸 수 있다
st ="Never\nEver\nGive\nUp"     #하나의 문장을 기준으로 데이터를 리스트로 빼낼 수 있다 cf)split:문자열
print(st)
print(st.splitlines()) #['Never', 'Ever', 'Give', 'Up']


''' ''' """ """ #싱글쿼터나 더블쿼터 파이썬에서 같은 것으로 쓰임
#왜 주석이 되었을까?
# 여러줄 문자열 처리    #여러줄의 값을 가지고 있는 문자열이 된다. #enter=개행문자가 숨겨져있다./눈에 보이진 않아도 개행\n이 들어감
st = """Never Ever Give Up  
Never Ever Give Up
Never Ever Give Up
Never Ever Give Up
Never Ever Give Up"""
print(st)
a = st.splitlines()
print(a)       
#['Never Ever Give Up  ', 'Never Ever Give Up', 'Never Ever Give Up', 'Never Ever Give Up', 'Never Ever Give Up']

#join(): 지정된 문자열을 기준으로 문자열로 데이터를 결합 <->split()과 반대되sms 개념
st ='123'
print(st.join('%%'))    # %123% '%%'두개 사이를  st가 매꾼 것
print('%'.join(st))     # 1%2%3  st가 % 사이를 매꾼 것
#앞에 있는 문자(결합할때 사용할 문자)를 참조(.)해서 넘겨진 것
lst1 = ["","123","456"]
print("".join(lst1))                        #123456
print("-".join(lst1),type("-".join(lst1)))  #-123-456 <class 'str'>

# st="2015-06-05"
lst =['2015','06','05'] #join을 사용하면 문자열로 만들 수 있다.
st ="-".join(lst)
print(st)       # 2015-06-05 #split을 사용하면 데이터를 반대로 뽑아낼 수 있다.
'''
#Python 문자열 실습 문제
#문제1. input() 함수로 이름과 나이 값을 입력 받을 때 한번에 입력
#      받아 처리하고 출력하는 코드를 작성하시오. 
user = input("이름과 나이를 입력하세요 예) 이름,나이 :")
a= user.split(",")
print("이름: {} 나이: {}".format(a[0],a[1]))
#풀이
text = input("이름과 나이를 입력 (예] 홍길동 18) : ")
name,age=text.split() #**uppacking
print("이름: {}, 나이: {}살".format(name,age))
'''
#문제2. input() 함수로 입력 받은 수의 더하기,빼기,곱하기,나누기의 
#      간단한 수식을 처리할 수 있도록 코드를 작성하시오.
#      예) 계산식을 입력하세요 : 5+5 
#          계산 결과 : 10
'''
while True:
    user=input("계산식을 입력하세요 예)5+5 : ")
    if  user.count("+")==1:
        a,b =user.split("+")
        a= int(a);b= int(b)
        print("{}+{}\n계산결과 : {}".format(a,b,a+b))
    elif user.count("-")==1:
        a,b=user.split("-")
        a= int(a);b= int(b)
        print("{}-{}\n계산결과 : {}".format(a,b,a-b))
    elif user.count("*")==1:
        a,b=user.split("*")
        a= int(a);b= int(b)
        print("{}*{}\n계산결과 : {}".format(a,b,a*b))
    elif user.count("/")==1:
        a,b=user.split("/")
        a= int(a);b= int(b)
        print("{}/{}\n계산결과 : {}".format(a,b,a/b))

#풀이
import os

while True:
    os.system('cls')
    calc=input("계산할 수식을 입력하세요 [ex)5+5] : ") #5+5
    if "+" in calc:
        #더하기 처리 연산
        num1,num2 = calc.split('+') #문자열로 num1과 num2로 나옴
        num1=int(num1);num2=int(num2)
        print("계산 결과는 : ",num1+num2)
    elif "-" in calc:
        #뻬기 처리
        num1,num2 = calc.split('-') #문자열로 num1과 num2로 나옴
        num1=int(num1);num2=int(num2)
        print("계산 결과는 : ",num1-num2)
    elif "*" in calc:
        #곱하기 처리
        num1,num2 = calc.split('*') #문자열로 num1과 num2로 나옴
        num1=int(num1);num2=int(num2)
        print("계산 결과는 : ",num1*num2)
    elif "/" in calc:
        #나누기 처리
        num1,num2 = calc.split('/') #문자열로 num1과 num2로 나옴
        num1=int(num1);num2=int(num2)
        print("계산 결과는 : {:.2f}" .format(num1/num2))
    else:
        print("수식입력 잘못됐습니다.")
        print("다시 입력해주세요!!")
    sel = input("계속하겠습니까?(Y/n) : ")
    if sel=='n':
        break
print("프로그램 종료합니다.")

# 함수(function) 
# : 프로그램에서 사용할 기능을 미리 정의해서 구현한 것
#   (또다른 의미에서의 작은 프로그램)
# 
#python의 함수 정의(생성)
# def 함수이름([인자list]):
#     '''''' 기술내용 '''''' 
#     함수 기능에 대한 정의1
#     함수 기능에 대한 정의2 
#     ...
# 
# -함수 사용에 있어서 설명이 필요한 겨우, 함수 내부에 주석을 사용하여 기술함. 
# -함수를 만들 때에 함수의 기능을 바로 알 수 있는 이름으로 정의하길 권장함.
# -미리 만들어 놓은 함수를 호출할 때는,"함수 이름([인자...])"#인자값은 하나이상일 수 있음.
# -정의 생성된 함수의 반환값이 있는 경우,"return"명령어를 사용 #return은 함수를 종료하면서 return다음값을 넘겨줌/ 없으면 종료함
#  함수에 반환값이 있을 수도 있고, 없을 수도 있다. 있는 경우 "return 반환값" cf)index의 반환값을 받았던 것 처럼
#  없는 경우에 "return"."return" 명령어가 실행되면, 함수는 종료.
# -함수에 필요하면 인자값을 전달할 수 있다. 전달된 인자값은 함수 정의시에 만든
# "메개변수"에 그 값이 저장된다. 이후에 함수 정의부에서 해당 내용을 가지고 
# 동작시키면 된다.(변수에 값이 전달된 것처럼 처리하면 됨.)

#예제1] 사용자가 입력한 값을 출력하는 함수를 구현

def pr():
    import os
    os.system("cls")
    txt=input("입력값 : ")
    print()
    print("입력한 내용은 : ",txt)
    os.system('pause')
pr()
#함수를 호출하면 프로그램의 정의부로 가서 실행이 된다.
 
# 실습 - 입력값을 받아서 사칙연산하는 프로그램 함수를 사용.
#       그 함수의 이름은 calc()로 구현해 보세요.
#       (메인에서 calc()호출하면 모든 동작이 가능하도록 설정) 

def calc():
    import os
    while True:
        os.system('cls')
        calc=input("계산할 수식을 입력하세요 [ex)5+5] : ") #5+5
        if "+" in calc:
            #더하기 처리 연산
            num1,num2 = calc.split('+') #문자열로 num1과 num2로 나옴
            num1=int(num1);num2=int(num2)
            print("계산 결과는 : ",num1+num2)
        elif "-" in calc:
            #뻬기 처리
            num1,num2 = calc.split('-') #문자열로 num1과 num2로 나옴
            num1=int(num1);num2=int(num2)
            print("계산 결과는 : ",num1-num2)
        elif "*" in calc:
            #곱하기 처리
            num1,num2 = calc.split('*') #문자열로 num1과 num2로 나옴
            num1=int(num1);num2=int(num2)
            print("계산 결과는 : ",num1*num2)
        elif "/" in calc:
            #나누기 처리
            num1,num2 = calc.split('/') #문자열로 num1과 num2로 나옴
            num1=int(num1);num2=int(num2)
            print("계산 결과는 : {:.2f}" .format(num1/num2))
        else:
            print("수식입력 잘못됐습니다.")
            print("다시 입력해주세요!!")
        sel = input("계속하겠습니까?(Y/n) : ")
        if sel=='n':
            break
    print("프로그램 종료합니다.")

calc()
'''
# 예제2] 함수의 인자값 사용 - 사용자가 입력한 값을 출력하는 함수를 구현 
#       사용자로부터 입력 받은 값을 인자값으로 처리하는 함수
def pr2(str1): #(str1):인자 메개변수 arguement
    print("입력한 내용은 : ",str1)

#메인
txt = input("입력값 : ")
print()
pr2(txt)

#함수는 본연의 기능만 담는 것이 가장 좋다
#실습 - 입력값을 받아서 사칙연산하는 프로그램 함수를 사용하여 동작하게 만드세요.
#   함수 명은 "calc([문자열인자값])"로 사용하세요.
def calc(calc):
    if "+" in calc:
        #더하기 처리 연산
        num1,num2 = calc.split('+') #문자열로 num1과 num2로 나옴
        num1=int(num1);num2=int(num2)
        print("계산 결과는 : ",num1+num2)
    elif "-" in calc:
        #뻬기 처리
        num1,num2 = calc.split('-') #문자열로 num1과 num2로 나옴
        num1=int(num1);num2=int(num2)
        print("계산 결과는 : ",num1-num2)
    elif "*" in calc:
        #곱하기 처리
        num1,num2 = calc.split('*') #문자열로 num1과 num2로 나옴
        num1=int(num1);num2=int(num2)
        print("계산 결과는 : ",num1*num2)
    elif "/" in calc:
        #나누기 처리
        num1,num2 = calc.split('/') #문자열로 num1과 num2로 나옴
        num1=int(num1);num2=int(num2)
        print("계산 결과는 : {:.2f}" .format(num1/num2))
    else:
        print("수식입력 잘못됐습니다.")
        print("다시 입력해주세요!!")

#메인
import os

while True:
    os.system('cls')
    txt = input("계산할 수식을 입력하세요[ex) 5+5]: ") # 5+5
    calc(txt)   #함수 호출
    sel = input("계속하겠습니까?(Y/n) : ")
    if sel == 'n':
        break
print("프로그램 종료합니다.!!")
