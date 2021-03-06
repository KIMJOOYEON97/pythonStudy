# 서식문자(제어문자)
# : 서식문자는 문자열에서 특정 값을 표현하는 문자 양식
# 
#   C언어     python      내용
#   %s          {}        서식문자 위치에 문자열을 출력
#   %d          {}        서식문자 위치에 정수를 출력
#               {:b}      표현식(0b)이 없는 2진수
#   %o          {:o}      표현식(0o)이 없는 2진수
#   %x          {:x}      표현식(0x)이 없는 2진수
#   %f          {:f}      서식문자 위치에 실수를 출력
#   %.3f        {:.3f}    소수점 3자리까지 출력
#   %6d         {:6}      6자리의 고정자리 값 출력
 

# 문자열과 정수 출력
print("%s : %d" %("나이",30))       #c언어 서식문자 사용
print("{} : {}" .format('나이',30)) #python서식문자 사용

# 실수 출력 예
print("%f, %.2f" %(1.2345,1.2345))
print("{:f}, {:.2f}" .format(1.2345,1.2345))

# 진법 출력 예제
print("%o, %x, %X" %(10,10,10))
print("{:b}, {:o}".format(10,10))
print("{:x}, {:X}".format(10,10))

# 고정길이 출력
print("|%5d|" % 123)
print("|%5s|" % 'abc')
print("|{:5}|".format(123))     #오른쪽 정렬
print("|{:5}|".format('abc'))   #왼쪽 정렬
print("{:5}".format(123))

# 고정길이 출력 - 정렬
print("|%5d|" % 123)      #+양수:오른쪽 정렬(기본값) 
print("|%-5s|" % 'abc')   #-음수:왼쪽 정렬

print("|{:<5}|".format(123))     #부등호가 "작다"이면 왼쪽 정렬 (모든등호의 기준은 왼쪽)
print("|{:>5}|".format('abc'))   #부등호가 "크다"이면 오른쪽 정렬
print("|{:^5}|".format('abc'))   #가운데 정렬

# 고정길이 출력 - 여백채우기
# 숫자여백 (C언어의 체계에서는 문자 불가)
print("|%05d|" %123) #값이 바뀌지않는 범위내에서만 12300(X)
print("|{:05}|".format(123))

#문자 여백
print("|{:_>5}|".format('abc'))     #__abc
print("|{:-^5}|".format('abc'))     #-abc-
print("|{:*^7}|".format('abc'))     #**abc**

# 정수, 실수의 단위 구분(천단위로 ","를 찍는 것을 의미함) <C언어에서는 지원X)
print("{:,}".format(1000000000))
print("{:,.2f}".format(1000000000))

#문제 pdf 28p
print("{:^70}".format('파이썬 쇼핑몰'))
print("{:3}: {:63}".format('번호','1078718855'))
print("{:3}: {:63}".format('주소','서울시 종로구 종로3가'))
print("{:3}: {:63}".format('성명','김사장'))
print("{:3}: {:63}".format('전화','070-1234-5678'))
print("{:-<70}".format('-'))
print("{:^20}{:^15}{:^10}{:^15}".format('품명','단가','수량','금액'))
print("{:-<70}".format('-'))
print("{:^16}{:10,}{:12}{:>25,}".format('블루투스 이어폰', 85000, 1, 85000))
print("{:^25}{:8,}{:12}{:>25,}".format('USB3.0 8G', 8000, 1, 8000))
print("{:-<70}".format('-'))
print("{:<62}{:,}".format('소 계',93000))
print("-"*70)
print("{:<60}{:,}".format('청구금액',85000+8000))
print("{:<59}{:,}".format('받은금액',100000))
print("{:<61}{:,}".format('거스름돈',100000-sum([85000,8000])))
print("-"*70)

#변수(Variable) : 다양한 데이터를 저장하는 공간(메모리) 
#                저장된 갑은 언제든지 다시 사용이 가능하고, 
#                경우에 따라서 기존 데이터를 덮어 씌울수도 있다.
# # ex. 주머니- 쌀을 담으면 쌀주머니 돈을 집어넣으면 돈주머니 
# >뭘 집어넣느냐에 따라 달라지는 것이다. 
# (파이썬이 자동으로 메모리 관리하는 기능이 있기때문=만능주머니)
#  <-> 상수: 변화되는 데이터

# 변수의 작명규칙(명명법)
# 1. 영문자, 숫자, 언더바(_)로 구성됨(한글도 가능)  *특수문자불가능(?*(X))
# 2. 영문 대소문자를 구분 ex)sum, Sum, sUm, suM 다 다른 변수
# 3. 변수명의 시작은 숫자를 사용하면 안됨. 
# ex) 밥1, rice_1,_abc  / 1abc(X)
# 4. 변수명 중간에 공백이 있으면 안됨. ex) vari able(X)
# 5. python의 예약어는 사용이 불가능
#    예약어란? 프로그램이 미리 사용하고 있는 단어
#    => 명령어

# 변수의 정의(선언)
#   변수명 = 값 (변수 하나인 경우)
#   변수명1, 변수명2 = 값1, 값2 (변수명1=값1, 변수명2=값2)  
#   변수명1 = 변수명2 = 값1 (변수명1=값1, 변수명2=값1)

x = 10
y = 20
z = x+y
s = "문자열"
print("x={},y={},z={}\n{}".format(x,y,z,s))

x,y,z=1,1.0,'1'
print(x);print(y);print(z)
# ; 해당명령줄이 여기서 끝났다. 명령어 끝
print(type(x))     # type()는 데이터의 자료형(타입)을 표기
print(type(y))
print(type(z))
print('')  #NULL => 문자가 없다는 의미의 문자
print(x+y,type(x+y)) #정수 + 실수의 계산 및 타입/ 묵시적 형변환 정수+실수했을 경우 실수  
print(x*y,type(x*y)) #곱하기도 마찬가지 *숫자끼리만 가능*
#print(x+z,type(x+z))   #TypeError

# 변수의 자료형
# 1. 정수(int): 양수, 0, 음수로 구성된 숫자
# 2. 실수(float): 소수점 이하의 값들이 표시되는 숫자
# 3. 문자열(str): 따옴표를 사용하여 표시되는 문자들
# 4. booL 형(booL): 참(True)또는 거짓(False)로 표시되는 값
# ----------------기본 자료형----------------------------
# 5. 리스트(List): 정수, 실수, 문자열 등 여러 자료형을 나열한 집합형 
#                   (값의 집합 자료)
# 6. 튜플(tuple):  정수, 실수, 문자열 등 여러 자료형을 나열한 집합형 
#                   (리스트와 거의 같은 성질 단, 값이 변경X)
# 7. 사전(dictionary): 정수, 실수 문자열 등 여러 자료형을 나열한 집합
#                   (키와 값의 쌍으로 만들어지는 자료들의 집합)
# ---------5~7 시퀸스 자료형 값을 순서대로 처리하고 관리---
# 
# 
# 자료형의 변환 함수(명시적 형변환)
# booL() 부울형 자료로 변환. (C언어에는 없음)
# int() 정수형 자료로 변환.
# float() 실수형 자료로 변환
# str() 문자형 자료로 변환
# tuple() 튜플형 자료로 변환
# List() 리스트형 자료로 변환
# dict() 딕셔너리형 자료로 변환
# set() 집합 자료로 변환
 
# booL형
print(bool(1))   #t
print(bool(0))   #f
print(bool(-1))  #t
print(bool(''))  #f
print(bool(' ')) #t
print(bool('a')) #t
print(bool([]))    #f
print(bool([-1]))  #t
# booL형은 값이 존재하면 True, 정수0, ''(NULL),[]빈자료인경우에는 False


#int() 자료 변환 -숫자형 문자
print(int(1.0))
print(int(1.1))
print(int('1'))
#print(int('1.0')) #정수로 변환할려고 했는데 실수를 입력해서  ValueError

#int() 함수의 확장사용
print(int('0xA',16))  #base=10 : 숫자를 10진수로 읽어드림 16:16진수값에 맞게 변환 시켜줌
print(int('0b1010',2))
print(int('A',16))
print(int('1010',2))
#진수값으로 변환시켜서 보여줌

#float() 자료의 변환
print(float(1))
print(float('1'))
print(float('1.0'))

#문자형 str() 자료의 변환
print(str(1))
print(str(0))
print(str(-1))
print(str(True))
print(str([]))
print(str([-1]))




