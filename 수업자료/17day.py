'''
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
def fr_add(lst):    #친구 목록 추가
    name = input("추가할 친구 이름을 입력하세요 : ")
    lst.append(name)
def fr_del(lst):    #친구 목록 삭제
    name = input("삭제할 친구 이름을 입력하세요 : ")
    if name in lst:
        lst.remove(name)
    else:print("삭제할 친구가 없습니다.")
def fr_mod(lst):    #친구 이름 수정
    name = input("수정할 친구 이름을 입력하세요 : ")
    if name in lst:
        idx=lst.index(name)
    else: 
        print("수정할 친구가 없습니다.")
        return
    name_mod = input("수정할 이름 입력하세요 : ")
    lst[idx] = name_mod


#메인
import os

fr_lst=[]
while True:
    os.system('cls')
    print("="*15, " 친구 관리 프로그램 ","="*15)
    print(" 1. 친구 목록 보기")
    print(" 2. 친구 추가")
    print(" 3. 친구 삭제")
    print(" 4. 친구 수정")
    print(" 0. 종료")
    sel = input("메뉴를 선택해주세요[0-4]: ")
    if sel == '1':
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
    else:
        print("메뉴 선택이 잘 못됐습니다.")
        os.system('pause')

# 문제) 알바 시급 프로그램 작성  (default 인자값 사용)
#   시급 : 8500원, 하루 8시간, 한달 30일(기본값)
# 
# 다음과 같이 출력되게 만드세요
# (출력 결과)
# <<시급 계산 프로그램>>
# 1. 기본급
# 2. 일한 날짜 입력
# 번호 입력 >>
def alba(day=30):
    time=8;price=8500
    re = time * price * day
    return re
def display():
    num=input("<<시급 계산 프로그램>>\n1. 기본급\n2.일한 날짜 입력\n번호입력>>")
    if num == '1':
        ret = alba()
    elif num == '2':
        day = int(input("일한 일수 입력 : "))
        ret = alba(day)
    print("당신의 급여는 {:,}원 입니다.".format(ret))
#메인
display()

# 인자값 처리 방식1 => 연속된 자료를 처리하는 함수의 인자 처리 방식

# 예제
def pr(a,b,c):
    print(a)
    print(b)
    print(c)
# 메인
pr(10,20,30)

# "*"를 이용하여 리스트 또는 튜플과 같은 자료를 연속된 인자의 값으로 처리
# 리스트 또는 튜플의 변수값을 받아서 "unpacking"하는 방식으로 인자를 전달
x = [100,200,300]
y = [10,20]
z = 1,2,3,4
pr(*x)              # a,b,c = [100,200,300]   => *사용
                    # a=100, b=200, c=300
pr(*y,30)
# pr(*z)    # TypeError: pr() takes 3 positional arguments but 4 were given

# "*"를 이용하여 연속된 자료(리스트, 튜플)에 데이터를 인자로 전달이 가능하나
# 인자의 개수와 전달되는 자료의 개수는 같아야 한다.(**) 

# 인자값 처리 방식 2 => 가변 인자 값 처리...
# -고정인자 => 인자값을 반드시 정해진 값으로 1:1 로 인자를 전해야하는 인자(일반)
# -가변인자 => 인자값을 정해진 개수로 전달하지 않고, 가변적으로 전달 가능한 인자
# 
# 가변이자 설정은 함수 정의시에 매개변수(인자) 앞에 "*"를 사용한다.

# 전달된 인자 값들의 합을 구하는 예제
def sum_func(*par):
    result = 0
    print(par,type(par))    # 전달된 인자값 처리 방식
    for su in par:
        result += su
    return result 
def display():
    Sum = 0
    Sum = sum_func()
    print(Sum)
    Sum = sum_func(10,20,30)
    print("인자가 세개(10,20,30)인 경우의 결과 : ",Sum)
    Sum = sum_func(10,20,30,40,50)
    print("인자 값 다섯개(10,20,30,40,50)인 경우의 결과 : ",Sum)

# 메인
display()

# 주의) 인자값 처리함에 있어 고정인자와 가변인자를 동시에 사용하는 경우,
# 고정인자를 먼저 처리하도록 한다. 즉, 가변인자는 마지막에 사용되게 해야 한다.

# "**"를 사용하는 경우는 딕셔너리에 대한 packing을 시도한다는 의미로 처리
# 
# 예제) 딕셔너리 자료형을 받아서 처리하는 함수
def dic_func(**par):
    print(par,type(par))
    for k in par:
        print("{}:{}".format(k,par[k]))

# 메인
dic_func(피카츄='1마리',파이리='2마리',꼬부기='없음')

# 변수의 범위(variable scope) => 변수의 생존
# -전역변수(global) : 상위 영역에서 선언된 변수로 프로그램 전반에 걸친 영향
#                   (프로그램 종료할 때까지 영향을 주는 변수) 
# -지역변수(local) : 블럭 영역에서 선언된 변수. 블럭 내에서만 영향
#                   (블럭을 나가는 순간 사라지는 변수)

# 예제1)
var = 2             # global
def func(arg):
    var1 = 1        # local
    global var      # global명령어를 통해서 전역변수를 블럭영역으로 불러옴.
    var = 3
    print(var1,var,arg)
# 메인
func(var)
# print(var1) # 지역변수 var1은 블럭을 벗어나면 사라짐. NameError: undefined
print(var) 


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
def transfer(dest,su=1,won=500):
    for i in range(1,su):
        won *= 2
        if won >= 10000:
            won = 10000
    return " {} 까지 요금 : {:,}원 입니다.".format(dest,won)
def display():
    dest="";su=0
    num = input("1.환승 안함\n2.환승 함\n3.장거리\n번호선택>> ")
    dest = input("목적지 입력 : ")
    if num == '1':
        result = transfer(dest)
    elif num == '2':
        su = int(input("환승 횟 수 입력 : "))
        result = transfer(dest,su)
    elif num == '3':
        result = transfer(dest,1,10000)
    else:
        print("메뉴 선택이 잘못됐습니다.")
        return
    print(result)
# 메인
display()

 

