'''
# 예제3] 지난식나 calc()를 이요하여 계산 결과를 반환값으로 처리하는 함수로 변환

def calc(calc):
    if "+" in calc:
        #더하기 처리 연산
        num1,num2 = calc.split('+')
        num1=int(num1);num2=int(num2)
        return num1+num2
    elif "-" in calc:
        #빼기 처리
        num1,num2 = calc.split('-')
        num1=int(num1);num2=int(num2)
        return num1-num2
    elif "*" in calc:
        #곱하기 처리
        num1,num2 = calc.split('*')
        num1=int(num1);num2=int(num2)
        return num1*num2
    elif "/" in calc:
        # 나누기 처리
        num1,num2 = calc.split('/')
        num1=int(num1);num2=int(num2)
        return num1/num2
    else:
        return False

import os

while True:
    os.system('cls')
    txt = input("계산할 수식을 입력하세요[ex) 5+5]: ") # 5+5
    result = calc(txt)   #함수 호출
    if result != False:  # False 수식을 잘못입력한 경우... 
        if type(result) is not float: #나눗셈결과는 float으로 소수점 2자리처리
            print("계산 결과는 : ",result)
        else:
            print("계산 결과는 : {:.2f}".format(result))
    else:
        print('수식입력 잘못됐습니다.!!\n다시 입력하세요!!')
    sel = input("계속하겠습니까?(Y/n) : ")
    if sel == 'n':
        break
print("프로그램 종료합니다.!!")

# 두수에 대한 한번의 계산식을 입력받아서 결과를 출력하는 코드를 이용
# 다음과 같이 코딩을 해보세요!!
#  - 사용자가 계산식을 입력. 이것을 이용해서 처리
#  - calc()가 인자값으로 두 정수와 계산식(기초: +,-,*,/)을 인자로 받아 처리하는
#   함수를 만들어 동작 시키세요.  

def calc(num1,num2,giho):
    if "+" in giho:
        return num1+num2
    elif "-" in giho:
        return num1-num2
    elif "*" in giho:
        return num1*num2
    elif "/" in giho:
        return num1/num2
    else:
        return False

import os

while True:
    os.system('cls')
    txt = input("계산할 수식을 입력하세요[ex) 5+5]: ") # 5+5
    if '+' in txt:
        su1,su2 = txt.split('+')
        su1=int(su1);su2=int(su2)
        giho = '+'
    elif '-' in txt:
        su1,su2 = txt.split('-')
        su1=int(su1);su2=int(su2)
        giho = '-'
    elif '*' in txt:
        su1,su2 = txt.split('*')
        su1=int(su1);su2=int(su2)
        giho = '*'
    elif '/' in txt:
        su1,su2 = txt.split('/')
        su1=int(su1);su2=int(su2)
        giho = '/'
    else:
        print("수식입력이 잘못됐습니다.\n다시 입력하세요.")
        os.system('pause')
        continue
    result = calc(su1,su2,giho)   #함수 호출
    if result != False:  # False 수식을 잘못입력한 경우... 
        if type(result) is not float: #나눗셈결과는 float으로 소수점 2자리처리
            print("계산 결과는 : ",result)
        else:
            print("계산 결과는 : {:.2f}".format(result))
    sel = input("계속하겠습니까?(Y/n) : ")
    if sel == 'n':
        break
print("프로그램 종료합니다.!!")


# 함수 인자 기본값(default) 설정
#  default 이란? 입력 인자값이 없는 경우에 기본적으로 적용되는 값을 의미함.
# 
# (형식)
# def 함수이름(인자1, 인자2=1):
#     함수정의문장1
#     함수정의문장2 
# 이렇게 정의된 함수가 있는 경우, 인자2는 '1'을 디폴트 값으로 가지게 됨.
# 즉, 인자2는 입력하지 않아도 '1'값을 기본적으로 가진다는 것.      

# 예제4] 함수 인자의 기본값 설정(인자1)
def pr4(arg1=10):
    print(arg1)

# 메인
pr4(10)
pr4(20)
pr4(3)
pr4()

# 인자를 2개 가진 경우(모두 default인자인 경우)
def pr5(arg1=10,arg2=20):
    print(arg1,arg2)
#메인
pr5(100,200)        # 100 200
pr5(100)            # 100 20
pr5(200)            # 200 20
pr5(arg2=200)       # 10 200
pr5()               # 10 20

# 인자가 2개이상, 기본값이 1인 경우 
def pr6(arg1,arg2=20):
    print(arg1,arg2)
#메인
pr6(100,200)    # 100 200
pr6(100)        # 100 20
pr6(200)        # 200 20
# pr6()           # TypeError => pr6의 arg1에 입력값이 존재해야 함. 

# 인자의 기본값이 맨앞에 있는 경우... 
#def pr7(arg1=10,arg2):   #SyntaxError : 기본값 뒤에 일반 인자는 존재X
    print(arg1,arg2)

# 결론은 인자의 기본값은 반드시 일반 인자 뒤에 나와야 한다. 
'''
# [Quiz]
# 1. 짝, 홀수를 구분하는 함수를 작성해 주세요.
def evenodd(num):
    if num%2==0:
        return '짝수'
    else: 
        return '홀수'
# 메인
su = int(input("정수 입력 : "))
result = evenodd(su)
print(result)

# 2. "3"의 배수를 판별하는 함수를 작성해 주세요.
def multi(num):
    if not num%3:
        return True
    else:
        return False
#메인
su2 = int(input("2. 정수 입력 : "))
if multi(su2):
    print("3의 배수입니다.")
else:
    print("3의 배수가 아닙니다.")


# 3. 계산기를 입력,출력,연산기능으로 나눠서 실행되게 
#    작성해 주세요.

# 입력 => 계산 처리 => 출력
def calc(num1,num2,giho):
    if giho == '+':
        return num1 + num2
    elif giho == '-':
        return num1 - num2
    elif giho == '*':
        return num1 * num2
    elif giho == '/':
        return num1 / num2
def Output(num1,num2,giho,result):
    print(num1,giho,num2,"=",result)
def Input():
    num1,giho,num2 = int(input("첫번째 정수 입력 : "))\
        ,input("계산기호 입력(+,-,*,/) : "),int(input("두번째 정수 입력 : "))
    result = calc(num1,num2,giho)
    Output(num1,num2,giho,result)
#메인
Input()

# 4. 예제 거꾸로 수를 반환하는 함수를 계산,출력 
#    기능으로 나눠서 작성해 주세요
#    예) 123 => 321
def reversecode(result):
    tmp, su = 0,0
    while True:
        tmp = result%10
        result = result//10
        su = (su + tmp) *10
        if not result:
            return su //10
def display():
    result,su = 0,0
    result = int(input("4. 정수 입력 : "))
    su = reversecode(result)
    print("변환 전 값 : {} , 변환 후 값 : {}".format(result,su))
#메인
display()

# 5. 예제 친구이름 관리를 함수로 기능을 나눠서 작성해주세요.
#    (1.친구목록보기,
#     2.친구추가,
#     3.친구삭제,
#     4.친구수정,
#     0.종료)
def fr_list(lst):   #친구 목록 보기
    print("========== 친구 목록 보기 ==========")
    if lst != []:
        for i in range(len(lst)):
            print("{} : {}".format(i+1,lst[i]))
    else: print("등록된 친구가 없습니다.")
    









