# 5. 예제 친구이름 관리를 함수로 기능을 나눠서 작성해주세요.
#    (1.친구목록보기,
#     2.친구추가,
#     3.친구삭제,
#     4.친구수정,
#     0.종료)

#함수를 사용하는 이유: 재사용 =>코드사용을 최소화시킴&유지보수할때 <객체지향적>
'''
def fr_list(lst):   #친구 목록 보기
    print("========== 친구 목록 보기 ==========")
    if lst != []:
        for i in range(len(lst)):
            print("{} : {}".format(i+1,lst[i])) #i+1 =>넘버링
    else: print("등록된 친구가 없습니다.")
def fr_add(lst):    #친구 목록 추가
    name = input("추가할 친구 이름을 입력하세요 : ")
    lst.append(name)
def fr_del(lst):    #친구 목록 삭제
    name = input("삭제할 친구 이름을 입력하세요 : ")
    if name in lst:     #remove는 이름이 없으면 오류 뜸으로
        lst.remove(name)
    else:              
        print("삭제할 친구가 없습니다.")
def fr_mod(lst):    #친구 목록 수정
    name=input("수정할 친구 이름을 입력하세요: ")
    if name in lst:
        idx=lst.index(name)
    else: 
        print("수정할 친구가 없습니다.")
        return   #return= 함수 종료//반복문이 아니라서 continue쓸 수 없다.
    name_mod =input("수정할 이름 입력하세요")
    lst[idx] = name_mod

#메인
import os
fr_lst=[]
while True:
    os.system('cls')
    print("="*15,"친구 관리 프로그램","="*15)
    print("1.친구목록보기")
    print("2.친구추가")
    print("3.친구삭제")
    print("4.친구수정")
    print("0.종료")
    sel = input ("메뉴를 선택해주세요[0~4]: ")
    if sel=='1':
        fr_list(fr_lst)
        os.system('pause')
    elif sel == '2':
        fr_add(fr_lst)
        os.system('pause')
    elif sel == '3':
        fr_del(fr_lst)
        os.system('pause')
    elif sel == '4':
        fr_mod(fr_lst)
        os.system('pause')
    elif sel == '0':
        print("프로그램을 종료하겠습니다.")
        break
    else: #메뉴선택이 잘못되었을 때
        print("메뉴 선택이 잘못되었습니다.")
        os.system('pause')

# 문제) 알바 시급 프로그램 작성 (default 인자값 사용) 
#   시급 : 8500원, 하루 8시간, 한달 30일(기본값)
# 
# 다음과 같이 출력되게 만드세요
# (출력 결과)
# <<시급 계산 프로그램>>
# 1. 기본급
# 2. 일한 날짜 입력
# 번호 입력 >>
# 

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

#풀이***노트 필기할때 넣기
def alba(day=30):
    time=8;price=8500
    re = time * price * day
    return re   #re는 처리된 나머지 결과값.
def display():
    num = input("<<시급 계산 프로그램>>\n1. 기본급\n2.일한 날짜 입력\n번호입력>>")
    if num == '1':
        ret = alba() #result값 받기 #숫자값을 변수에 저장// 나중에 변수에 class를 저장하기도 한다.
    elif num == '2':
        day =int(input("일한 일수 입력 : "))
        ret=alba(day)
    print("당신의 급여는 {:,}원 입니다.".format(ret))

#메인
display()   
'''
# 인자값 처리 방식1 => 연속된 자료를 처리하는 함수의 인자 처리 방식
 
# 예제
def pr(a,b,c):
    print(a)
    print(b)
    print(c)
#메인
pr(10,20,30)     #출력결과 =>10
                            #20
                            #30

#"*"를 이용하여 리스트 또는 튜플과 같은 자료를 연속된 인자의 값으로 처리
# 리스트 또는 튜플의 변수값을 받아서 "unpacking"하는 방식으로 인자를 전달
x=[100,200,300]
y=[10,20]
z=1,2,3,4
pr(*x)      #*를 안치면 argument error 인자 하나 밖에 안넣었다고 나옴 
 # =>100    # a,b,c =[100,200,300] =>*사용 ->unpacking
    #200    # a=100,b=200,c=300
    #300
pr(*y,30)   #자리숫자 맞춰 주기 pr(*y)=>Error
#pr(*z)      #TypeError => 요구하는 인자 개수를 넘었다. 
             # pr() takes 3 positional arguments but 4 were given

#"*"를 이용하여 연속된 자료(리스트,튜플)에 데이터를 인자로 전달이 가능하나
# 인자의 개수와 전달되는 자료의 개수는 같아야 한다.(**) 

# 인자값 처리 방식 2 =>가변 인자 값 처리...
# -고정인자 => 인자값을 반드시 정해진 갑으로 1:1로 인자를 전해야하는 인자(일반) 
                                #일반인자,default(기본값)는 다 고정인자의 값의 형태를 취함
# -가변인자 => 인자값을 정해진 개수로 전달하지 않고, 가변적으로 전달 가능한 인자
                                #packing이 일어난다.=>리스트, 튜플 형태로 만들어서 처리

# 가변인자 설정은 함수 정의시에 매개변수(인자) 앞에 "*"를 사용한다.
 
# 전달된 인자 값들의 합을 구하는 예제
def sum_func(*par):     #(*par)=>packing이 일어난다고 생각
    result = 0
    print(par,type(par))   #전달된 인자값 처리 방식
    for su in par:
        result +=su
    return result 
def display():
    Sum=0
    Sum=sum_func()
    print(Sum)
    Sum=sum_func(10,20,30)
    print("인자가 세개(10,20,30)인 경우의 결과 : ",Sum)   
    Sum=sum_func(10,20,30,40,50)
    print("인자가 다섯개(10,20,30,40,50)인 경우의 결과 : ",Sum)   

#메인
display()

#주의) 인자값 처리함에 있어 고정인자와 가변인자를 동시에 사용하는 경우,
# 고정인자를 먼저 처리하도록 한다. 즉, 가변인자는 마지막에 사용되게 해야 한다
                                 #가변인자는 고정인자(일반인자)뒤에 와야한다.

#연속된 딕셔너리 형태로 만드는것 
# "**"를 사용하는 경우는 딕셔너리에 대한 packing을 시도한다는 의미로 처리
# 
# 예제) 딕셔너리 자료형을 받아서 처리하는 함수
def dic_func(**par):    
    print(par,type(par)) #받는 값=par
    for k in par:
        print("{}:{}".format(k,par[k]))

#메인
dic_func(피카츄='1마리',파이리='2마리',꼬부기='없음')

# 변수의 범위(variable scope) => 변수의 생존(범위,사용범위)
# -전역변수(global) : 상위 영역에서 선언된 변수로 프로그램 전반에 걸친 영향 #맨앞에서 선언되는 변수는 전역변수
#                     (프로그램 종료할 때까기 영항을 주는 변수) 
# -지역변수(local) : 블럭 영역에서 선언된 변수. 블럭 내에서만 영향
#                    (블럭을 나가는 순간 사라지는 변수)  블럭=>들여쓰기 안에서만 영향을 미치는 변수
 
# 예제1)
var=2               # global 전역변수- 최상위위치에서 변수를 선언함.
def func(arg):
    var1 = 1        # local 지역변수    
    global var      # global 전역변수를 블럭영역으로 불러옴/ 블럭내에서는 영향을 준다.
    var = 3         # -> 전역변수가 됌
    print(var1,var,arg) #=> 1 3 2//변수에 해당된 이름이 같으면 가장가까운 지역변수를 선택한다.
#메인
func(var)   # 1 2
#print(var1) #지역변수 var1은 블럭을 벗어나면 사라짐. undefined NameError: name 'var1' is not defined
print(var)  # 2

'''
#[Quiz]
디폴트 매개변수를 이용한 요금 구하는 프로그램 만들기.
기본 요금은 500원 환승이 없거나 환승 1회까지는 기본요금.
1회를 초과하는 환승의 경우 환승 1회마다 요금의 2배씩 증가된다.
[EX) 환승 2회인 경우 : 1000원, 환승 3회일 경우 : 2000원]
[장거리는 10000원으로 처리한다.]
1. 환승 안함
2. 환승 함         #(몇번환승하는지 질의 후 요금 계산)
3. 장거리
<<** 함수화하여 작업하세요>>
함수 처리시 목적지에 대한 내용도 입력 받아서 처리하세요!!
'''

def pay(num,a=500):
    for x in range(1,num):   #(num)하면 3번 환승시 4000원 나옴. x=0,1,2 (3번 반복=>1)a*2=1000 2)2000 3)4000)
        if num==1:          #(1,num) x= 1,2(2번 반복=>1) 1000 2)2000 ) **첫번째까지는 기본요금인것!!
            a=a
        elif a >= 10000:
            a=10000
        else:
            a *= 2
    return "목적지까지 {}번 환승하여 {}원 나왔습니다.".format(num,a)

def display():
    print("1. 환승 안함")
    print("2. 환승 함")
    print("3. 장거리")
    sel= input("메뉴를 선택하세요:")
    if sel =='1':
        result=pay(0)
    if sel =='2':
        num=int(input("몇 번 환승하였습니까? : "))
        result=pay(num)
    if sel =='3':
        result=pay(1,a=10000)
    print(result)
#메인
display()

#풀이
def transfer(dest,su=1,won=500):
    for i in range(1,su):
        won *= 2
        if won >= 10000:
            won = 10000
    return "{}까지 요금: {:,}원 입니다.".format(dest,won)  #반환값이 문자열
def display():
    dest="";su=0
    num =input("1.환승 안함\n2.환승 함\n3.장거리\n번호선택>> ")
    dest=input("목적지 입력: ")
    if num =='1':
        result = transfer(dest) 
    elif num =='2':
        su =int(input("환승 횟 수 입력 : "))
        result =transfer(dest,su)
    elif num =='3':
        result =transfer(dest,won=10000) #or (dest,1,10000)
    else:
        print("메뉴 선택이 잘못됐습니다.")
        return
    print(result)
#메인
display()