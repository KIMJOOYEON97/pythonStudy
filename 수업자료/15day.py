'''
# strip() : 양쪽에 있는 공백 또는 문자를 제거
st = "   파이썬   "
print("[{}]".format(st))
print("[{}]".format(st.strip()))

st2 = "파이썬파"
print(st2)
print(st2.strip("파"))
print(st2.lstrip("파"))
print(st2.rstrip("파"))

st3 = "--1-파이썬-1--"
print(st3)
print(st3.strip("-"))
print(st3.lstrip("-"))
print(st3.rstrip("-"))

# replace()함수 사용
st = "2015-06-05"
#     0123456789 (index)
print(st)
print(st.replace('2015','2020'))
print(st[0:4])
print(st.replace(st[0:4],'2020'))

# split(str) : 특정 문자(str)를 기준으로 문자열을 나누는 함수 => 리스트저장
st = "Never Ever Give Up"
a = st.split()
print(st)
print(a,type(a))

st2 = "하나:둘:셋"
st3 = "1,2,3"
b = st2.split(':')
c = st3.split(',')
print(b,type(b))
print(c,type(c))

st4 = "하나둘셋넷"
d = st4.split()
print(d,type(d))

# splitlines() : 개행('\n')를 기준으로 문자열을 나누는 함수 => 저장은 리스트
st = "Never\nEver\nGive\nUp"
print(st)
print(st.splitlines())

# 여러줄 문자열 처리
st = """Never Ever Give Up
Never Ever Give Up
Never Ever Give Up
Never Ever Give Up
Never Ever Give Up"""
print(st)
a = st.splitlines()
print(a)

# join() : 지정된 문자열을 기준으로 문자열로 데이터를 결합
st = '123'
print(st.join('%%'))
print('%'.join(st))
lst1 = ["","123","456"]
print("".join(lst1))
print("-".join(lst1),type("-".join(lst1)))

# st = "2015-06-05"
lst = ['2015','06','05']
st = "-".join(lst)
print(st)

#Python 문자열 실습 문제
#문제1. input() 함수로 이름과 나이 값을 입력 받을 때 한번에 입력
#      받아 처리하고 출력하는 코드를 작성하시오. 
text = input("이름과 나이를 입력 (예] 홍길동 18 ) : ")
name,age = text.split()
print("이름 : {} , 나이 : {}살".format(name,age))

#문제2. input() 함수로 입력 받은 수의 더하기,빼기,곱하기,나누기의 
#      간단한 수식을 처리할 수 있도록 코드를 작성하시오.
#      예) 계산식을 입력하세요 : 5+5 
#          계산 결과 : 10
#  
import os

while True:
    os.system('cls')
    calc = input("계산할 수식을 입력하세요[ex) 5+5]: ") # 5+5
    if "+" in calc:
        #더하기 처리 연산
        num1,num2 = calc.split('+')
        num1=int(num1);num2=int(num2)
        print("계산 결과는 : ",num1+num2)
    elif "-" in calc:
        #빼기 처리
        num1,num2 = calc.split('-')
        num1=int(num1);num2=int(num2)
        print("계산 결과는 : ",num1-num2)
    elif "*" in calc:
        #곱하기 처리
        num1,num2 = calc.split('*')
        num1=int(num1);num2=int(num2)
        print("계산 결과는 : ",num1*num2)
    elif "/" in calc:
        # 나누기 처리
        num1,num2 = calc.split('/')
        num1=int(num1);num2=int(num2)
        print("계산 결과는 : %.2f" % (num1/num2))
    else:
        print("수식입력 잘못됐습니다.")
        print("다시 입력해주세요!!")
    sel = input("계속하겠습니까?(Y/n) : ")
    if sel == 'n':
        break
print("프로그램 종료합니다.!!")


# 함수(function)
# : 프로그램에서 사용할 기능을 미리 정의해서 구현한 것
#   (또 다른의미에서의 작은 프로그램)
# 
#python의 함수 정의(생성)
# def 함수이름([인자list]):
#     
#     함수 기능에 대한 정의1
#     함수 기능에 대한 정의2
#     .... 
# 
# -함수 사용에 있어서 설명이 필요한 경우, 함수 내부에 주석을 사용하여 기술함.
# -함수를 만들 때에 함수의 기능을 바로 알 수 있는 이름으로 정의하길 권장함.
# -미리 만들어 놓은 함수를 호출할 때는, "함수 이름([인자...])" 으로 호출  
# -정의 생성된 함수의 반환값이 있는 경우, "return" 명령어를 사용
#  함수에 반환값이 있을 수도 있고, 없을 수도 있다. 있는 경우 "return 반환값"
#  없는 경우에 "return". "return" 명령어가 실행되면, 함수는 종료.
# -함수에 필요하면 인자값을 전달할 수 있다. 전달된 인자값은 함수 정의시에 만든
#  "매개변수"에 그 값이 저장된다. 이후에 함수 정의부에서 해당 내용을 가지고 
#  동작시키면 된다. (변수에 값이 전달된 것처럼 처리하면 됨.)     

# 예제1] 사용자가 입력한 값을 출력하는 함수를 구현
def pr():
    txt=input("입력값 : ")
    print()
    print("입력한 내용은 : ",txt)

pr()

# 실습 - 입력값을 받아서 사칙연산하는 프로그램 함수를 사용. 
#      그 함수의 이름은 calc()로 구현해 보세요.
#      (메인에서 calc()호출하면 모든 동작이 기능하도록 설정) 
 
def calc():
    import os

    while True:
        os.system('cls')
        calc = input("계산할 수식을 입력하세요[ex) 5+5]: ") # 5+5
        if "+" in calc:
            #더하기 처리 연산
            num1,num2 = calc.split('+')
            num1=int(num1);num2=int(num2)
            print("계산 결과는 : ",num1+num2)
        elif "-" in calc:
            #빼기 처리
            num1,num2 = calc.split('-')
            num1=int(num1);num2=int(num2)
            print("계산 결과는 : ",num1-num2)
        elif "*" in calc:
            #곱하기 처리
            num1,num2 = calc.split('*')
            num1=int(num1);num2=int(num2)
            print("계산 결과는 : ",num1*num2)
        elif "/" in calc:
            # 나누기 처리
            num1,num2 = calc.split('/')
            num1=int(num1);num2=int(num2)
            print("계산 결과는 : %.2f" % (num1/num2))
        else:
            print("수식입력 잘못됐습니다.")
            print("다시 입력해주세요!!")
        sel = input("계속하겠습니까?(Y/n) : ")
        if sel == 'n':
            break
    print("프로그램 종료합니다.!!")

calc()

# 예제2] 함수의 인자값 사용 - 사용자가 입력한 값을 출력하는 함수를 구현
#     사용자로부터 입력 받은 값을 인자값으로 처리하는 함수
def pr2(str1):
    print("입력한 내용은 : ",str1)

#메인
txt = input("입력값 : ")
print()
pr2(txt)
'''
# 실습 - 입력값을 받아서 사칙연산하는 프로그램 함수를 사용하여 동작하게 만드세요. 
#     함수 명은 "calc([문자열인자값])"로 사용하세요.    


def calc(calc):
    if "+" in calc:
        #더하기 처리 연산
        num1,num2 = calc.split('+')
        num1=int(num1);num2=int(num2)
        print("계산 결과는 : ",num1+num2)
    elif "-" in calc:
        #빼기 처리
        num1,num2 = calc.split('-')
        num1=int(num1);num2=int(num2)
        print("계산 결과는 : ",num1-num2)
    elif "*" in calc:
        #곱하기 처리
        num1,num2 = calc.split('*')
        num1=int(num1);num2=int(num2)
        print("계산 결과는 : ",num1*num2)
    elif "/" in calc:
        # 나누기 처리
        num1,num2 = calc.split('/')
        num1=int(num1);num2=int(num2)
        print("계산 결과는 : %.2f" % (num1/num2))
    else:
        print("수식입력 잘못됐습니다.")
        print("다시 입력해주세요!!")
    
import os

while True:
    os.system('cls')
    txt = input("계산할 수식을 입력하세요[ex) 5+5]: ") # 5+5
    calc(txt)   #함수 호출
    sel = input("계속하겠습니까?(Y/n) : ")
    if sel == 'n':
        break
print("프로그램 종료합니다.!!")

