'''
# 예제3] 지난시간 calc()를 이용하여 계산 결과를 반환값으로 처리하는 함수로 변환
# calc=문자열 받는 것
def calc(calc):
    if "+" in calc:
        #더하기 처리 연산
        num1,num2 = calc.split('+') #문자열로 num1과 num2로 나옴
        num1=int(num1);num2=int(num2)
        return num1+num2
    elif "-" in calc:
        #뻬기 처리
        num1,num2 = calc.split('-') #문자열로 num1과 num2로 나옴
        num1=int(num1);num2=int(num2)
        return num1-num2
    elif "*" in calc:
        #곱하기 처리
        num1,num2 = calc.split('*') #문자열로 num1과 num2로 나옴
        num1=int(num1);num2=int(num2)
        return num1*num2
    elif "/" in calc:
        #나누기 처리
        num1,num2 = calc.split('/') #문자열로 num1과 num2로 나옴
        num1=int(num1);num2=int(num2)
        return num1/num2
    else:
        return False    #이걸 하면 수식이 잘못되었습니다.

import os

while True:
    os.system('cls')
    txt = input("계산할 수식을 입력하세요[ex) 5+5]: ") # 5+5
    result = calc(txt)   #함수 호출
    if result != False:  #False 수식을 잘못입력한 경우
        if type(result) is not float:   #나눗셈 결과는 float으로 소수점 2자리까지 처리
            print("계산결과는 : ",result)
        else:
            print("계산 결과는 : {:.2f}".format(result))
    else:
        print("수식입력 잘못됐습니다!!\n 다시 입력하세요!!")
    sel = input("계속하겠습니까?(Y/n) : ")
    if sel == 'n':
        break
print("프로그램 종료합니다.!!") 

# 두수에 대한 한번의 계산식을 입력받아서 결과를 출력하는 코들르 이용
# 다음과 같이 코딩을 해보세요!
# -사용자가 계산식을 입력. 이것을 이용해서 처리
# -calc()가 인자값으로 두 정수와 계산식(기초:+,-,*,/)을 인자로 받아 철하는
#       함수를 만들어 동작시키세요. 

#풀이
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
        return False    #이걸 하면 수식이 잘못되었습니다.
#이런 형태로 만들어야 재사용하는게 가능 함수는 작으면 작을 수록 좋다. 기능이 많으면 한계점이 많아진다.
import os

while True:
    os.system('cls')
    txt = input("계산할 수식을 입력하세요[ex) 5+5]: ") # 5+5
    if '+' in txt:
        su1,su2=txt.split('+')
        su1=int(su1);su2=int(su2)
        giho='+'
    elif'-' in txt:
        su1,su2=txt.split('-')
        su1=int(su1);su2=int(su2)
        giho='-'
    elif'*' in txt:
        su1,su2=txt.split('*')
        su1=int(su1);su2=int(su2)
        giho='*'  
    elif'/' in txt:
        su1,su2=txt.split('/')
        su1=int(su1);su2=int(su2)
        giho='/'          
    else:
        print("수식입력 잘못됐습니다!!\n 다시 입력하세요!!")
        os.system('pause')
        continue
    result =calc(su1,su2,giho)
    if result != False:  #False 수식을 잘못입력한 경우
        if type(result) is not float:   #나눗셈 결과는 float으로 소수점 2자리까지 처리
            print("계산결과는 : ",result)
        else:
            print("계산 결과는 : {:.2f}".format(result))

    sel = input("계속하겠습니까?(Y/n) : ")
    if sel == 'n':
        break
print("프로그램 종료합니다.!!") 

# 함수 인자 기본값(default) 설정
# default 이란? 입력 인자값이 없는 경우에 기본적으로 적용되는 값을 의미함.
# 
# (형식)
# def  함수이름(인자1, 인자2=1): #넘겨주기 전에 이미 인자의 초기값을 넣어주는 것
#       함수정의문장1
#       함수정의문장2
# 이렇게 정의된 함수가 있는 경우, 인지2는 '1'을 디폴트 값으로 가지게 됨
# 즉, 인자2는 입력하지 않아도 '1'값을 기본적으로 가진다는 것.

# 예제4] 함수 인자의 기본값 설정(인자1)
def pr4(arg1=10):
    print(arg1)

# 메인 
pr4(10)     #10
pr4(20)     #20
pr4(3)      #3
pr4()       #10

# 인자를 2개 가진 경우(모두 default인자인 경우)
def pr5(arg1=10,arg2=20):
    print(arg1,arg2)
#메인
pr5(100,200)    # 100 200
pr5(100)        # 100 20     
pr5(200)        # 200 20
pr5(arg2=200)   # 10 200
pr5()           # 10 20

#입력값은 인자의 순서대로 넘어간다. / 특정 인자 값을 바꾸고 싶으면 인자명=바꾸고 싶은 숫자 
#                                   like 변수명 정의하듯

# 인자가 2개이상, 기본값이 1인 경우
def pr6(arg1,arg2=20):
    print(arg1,arg2)
#메인
pr6(100,200)    #100 200    
pr6(100)        #100 20 
pr6(200)        #200 20
# pr6()           #TypeError =>pr6의 arg1에 입력값이 존재해야 함.
                  #pr6() missing 1 required positional argument: 'arg1'
#기본인자 값이 없을 경우 일반 인자값을 반드시 넣어줘야한다.

# 인자의 기본값이 맨앞에 있는 경우...
#def pr7(arg1=10,arg2): 
#SyntaxError(문법에러): 기본값 뒤에 일반 인자는 존재x /non-default argument follows default argument
#    print(arg1,arg2)    #인자 기본값은 일반인자 앞에 있으면 안된다. 일반인자가 모두 선언된 다음에 디폴트가 나와야함.

# 결론은 인자의 기본값은 반드시 일반 인자 뒤에 나와야 한다.



# [Quiz]    #함수에서 함수를 불러올 수 있다. 단, 순서대로
# 1. 짝, 홀수를 구분하는 함수를 작성해 주세요.

# 2. "3"의 배수를 판별하는 함수를 작성해 주세요.

# 3. 계산기를 입력,출력,연산기능으로 나눠서 실행되게 
#    작성해 주세요.

# 4. 예제 거꾸로 수를 반환하는 함수를 계산,출력 
#    기능으로 나눠서 작성해 주세요
#    예) 123 => 321

#1. 풀이랑 합침..
def evenodd(num):
    if num%2==0:
        return '짝수'       #bool형 True/False로도 구분 가능
    else:
        return '홀수'

user=int(input("정수를 입력하세요[짝/홀 구분]: "))
result = evenodd(user)
print(result)

#2
def thr(arg):
    if arg%3==0:
        print("3의 배수입니다.")
    else:
        print("3의 배수가 아닙니다.")

user=int(input("수를 입력하세요[3의 배수 구분]: "))
thr(user)

#풀이
def multi(num):
    if not num%3:
        return True
    else:
        return False
#메인
su2 = int(input("2. 정수 입력 : "))
if multi(su2):
    print("3의 배수 입니다.")
else:
    print("3의 배수가 아닙니다.")

'''
#3
'''
def putn():
    usern=input("수을 입력하세요[ex)5+5] : ")
    if "+" in usern:
        num1,num2=usern.split('+')
        num1=int(num1);num2=int(num2)
        giho='+'
        return num1,num2,giho
    if "-" in usern:
        num1,num2=usern.split('-')
        num1=int(num1);num2=int(num2)
        giho='-'
        return num1,num2,giho
    if "*" in usern:
        num1,num2=usern.split('*')
        num1=int(num1);num2=int(num2)
        giho='*'
        return num1,num2,giho
    if "/" in usern:
        num1,num2=usern.split('/')
        num1=int(num1);num2=int(num2)
        giho='/'
        return num1,num2,giho
    
def calc(result):
    if "+" in result:
        return num1+num2
    elif "-" in result:
        return num1-num2
    elif "*" in result:
        return num1*num2
    elif "/" in result:
        return num1/num2
    else:
        return False 
def pr():
    print(result)

import os
while True:
    os.system('cls')
    putn()
    result = num1,num2,giho
    calc()
    pr()
    os.system("pause")

#풀이
#입력 =>계산 처리=>출력
def calc(num1,num2,giho):
    if "+" == giho:
        return num1+num2
    elif "-" == giho:
        return num1-num2
    elif "*" == giho:
        return num1*num2
    elif "/" == giho:
        return num1/num2    
def Output(num1,num2,giho,result):
    print(num1,giho,num2,"=",result)
def Input():
    num1,giho,num2 = int(input("첫번째 정수입력: "))\
        ,input("계산기호 입력(+,-,*,/): "), int(input("두번째 정수입력: "))
    result =calc(num1,num2,giho)        #순서가 중요하다. 앞에서 변수 정의를 해줘야함.
    Output(num1,num2,giho,result)
#메인
Input()
'''
#4
#풀이
def reversecode(result):
    tmp,su=0,0
    while True:
        tmp= result%10 #1의 자리 수
        result= result//10
        su =(su+tmp)*10
        if not result: #result가 0이되면 참
            return su//10  #곱한 값을 나눠줌
def display():
    result, su = 0,0
    result = int(input("4.정수 입력: "))
    su = reversecode(result)
    print("변환 전 값 : {},변환 후 값: {} ".format(result,su))
#메인
display()

# 5. 예제 친구이름 관리를 함수로 기능을 나눠서 작성해주세요. #12day.py 참고
#    (1.친구목록보기,
#     2.친구추가,
#     3.친구삭제,
#     4.친구수정,
#     0.종료)

def see():
    print(lst)
def add(user):
    lst.append(user)
def de(user):
    lst.remove(user)
def cy(user):
    if user not in lst:
        print("삭제할 친구가 없습니다.")
    else:
        nname=input("수정할 이름을 입력하세요.")
        idx = lst.index(user)
        lst.remove(user)
        lst.insert(idx, nname)
def end():
    print("프로그램 종료합니다.")

print('1.친구목록보기')
print('2.친구추가')
print('3.친구삭제')
print('4.친구수정')
print('0.종료')
lst=[]
while True:
    sel=input("메뉴를 입력하세요: ")
    if sel =='1':
        see()
    elif sel =='2':
        name=input("이름을 입력하세요: ")
        add(name)
    elif sel =='3':
        name=input("이름을 입력하세요: ")
        de(name)
    elif sel =='4':
        name=input("이름을 입력하세요: ")
        cy(name)
    elif sel =='0':
        end()
    else:
        print("메뉴를 잘못입력했습니다.")