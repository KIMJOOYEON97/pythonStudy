'''
# 서식문자(제어문자)
# : 서식문자는 문자열에서 특정 값을 표현하는 문자 양식
# 
#    C언어      python      내용
#     %s         {}         서식문자 위치에 문자열을 출력
#     %d         {}         서식문자 위치에 정수를 출력
#                {:b}       표현식(0b)이 없는 2진수
#     %o         {:o}       표현식(0o)이 없는 8진수
#     %x         {:x}       표현식(0x)이 없는 16진수
#     %f         {:f}       서식문자 위치에 실수를 출력  
#     %.3f       {:.3f}     소수점 3자리까지 출력
#     %6d        {:6}       6자리의 고정자리 값 출력

# 문자열과 정수 출력
print(" %s : %d " % ('나이',30))        #C언어 서식문자 사용
print(" {} : {} ".format('나이',30))    # python서식문자 사용

# 실수 출력 예
print("%f, %.2f" % (1.2345,1.2345))
print("{:f}, {:.2f}".format(1.2345,1.2345))

# 진법 출력 예제
print("%o, %x, %X" % (10,10,10))
print("{:b}, {:o}".format(10,10))
print("{:x}, {:X}".format(10,10))

# 고정길이 출력
print("|%5d|" % 123)
print("|%5s|" % 'abc')
print("|{:5}|".format(123))
print("|{:5}|".format('abc'))

# 고정길이 출력 - 정렬
print("|%5d|" % 123)        # 양수는 오른쪽 정렬
print("|%-5s|" % 'abc')     # 음수는 왼쪽 정렬

print("|{:<5}|".format(123))    # 부등호가 "작다"이면 왼쪽정렬
print("|{:>5}|".format('abc'))  # 부등호가 "크다"이면 오른쪽정렬
print("|{:^5}|".format('abc'))  # 가운데 정렬

# 고정길이 출력 - 여백채우기
# 숫자 여백
print("|%05d|" % 123)
print("|{:05}|".format(123))

# 문자 여백
print("|{:_>5}|".format('abc'))     # __abc
print("|{:-^5}|".format('abc'))     # -abc-
print("|{:*^7}|".format('abc'))     # **abc**

# 정수, 실수의 단위 구분(천단위로 ","를 찍는 것을 의미함)
print("{:,}".format(1000000000))
print("{:,.2f}".format(1000000000))


# pdf 28page
print("{:^62}".format("파이썬 쇼핑몰"))
print("{:3}: {}".format("번호",1078718855))
print("{:3}: {}".format("주소",'서울시 종로구 종로3가'))
print("{:3}: {}".format("성명",'김사장'))
print("{:3}: {}".format("전화",'070-1234-5678'))
print("-"*68)
print("{:^22}{:^12}{:^12}{:^14}".format("품명","단가","수량","금액"))
print("-"*68)
print("{:^18}{:12,}{:12,}{:18,}".format("블루투스 이어폰",85000,1,85000))
print("{:^25}{:12,}{:12,}{:18,}".format("usb3.0 8G",8000,1,8000))
print("-"*68)
print("{:4}{:61,}".format("소 계",85000+8000))
print("-"*68)
print("{:4}{:59,}".format("청구금액",85000+8000))
print("{:4}{:59,}".format("받은금액",100000))
print("{:4}{:59,}".format("거스름돈",100000-(85000+8000)))
print("-"*68)

# 변수(Variable) : 다양한 데이터를 저장하는 공간(메모리)
#               저장된 값은 언제든지 다시 사용이 가능하고,
#               경우에 따라서 기존 데이터를 덮어 씌울수도 있다.
# 
# 변수의 작명규칙(명명법)
# 1. 영문자,숫자,언더바(_)로 구성됨(한글도 가능)
# 2. 영문 대소문자를 구분  ex)sum, Sum, SUM, sUm, suM 다 다른변수 
# 3. 변수명의 시작은 숫자를 사용하면 안됨. 
# ex) 밥1, rice_1, _abc, 1abc(X)
# 4. 변수명 중간에 공백이 있으면 안됨. ex) vari able(X), vari_able(o)
# 5. python의 예약어는 사용이 불가능
#   예약어란? 프로그램이 미리 사용하고 있는 단어
#          => 명령어    

# 변수의 정의(선언)
#   변수명 = 값   (변수 하나인 경우)
#   변수명1, 변수명2 = 값1, 값2 (변수명1=값1, 변수명2=값2)
#   변수명1 = 변수명2 = 값1 (변수명1=값1, 변수명2=값1) 

x = 10
y = 20
z = x + y
s = "문자열"
print("x={},y={},z={}\n{}".format(x,y,z,s))

x,y,z = 1,1.0,'1'
print(x);print(y);print(z)
print(type(x))  # type()는 데이터의 자료형(타입)을 표기
print(type(y))
print(type(z))
print('')   # NULL => 문자가 없다는 의미의 문자
print(x+y,type(x+y))  # 정수 + 실수의 계산 및 타입
print(x*y,type(x*y))
# print(x+z)              #TypeError

# 변수의 자료형
# 1. 정수(int) : 양수, 0 , 음수로 구성된 숫자
# 2. 실수(float) : 소수점 이하의 값들이 표시되는 숫자
# 3. 문자열(str) : 따옴표를 사용하여 표시되는 문자들
# 4. bool형(bool) : 참(True) 또는 거짓(False)로 표시되는 값
# --------기본 자료형--------------
# 5. 리스트(list) : 정수,실수,문자열 등 여러 자료형을 나열한 집합
#                 (값의 집합 자료)
# 6. 튜플(tuple) :  정수,실수,문자열 등 여러 자료형을 나열한 집합
#                 (리스트와 거의 같은 성실 단, 값이 변경 X)
# 7. 사전(dictionary) : 정수, 실수 문자열 등 여러 자료형을 나열한 집합
#                 (키와 값의 쌍으로 만들어지는 자료들의 집합) 
 
# 자료형의 변환 함수
# bool()    부울형 자료로 변환.
# int()     정수형 자료로 변환.
# float()   실수형 자료로 변환.
# str()     문자형 자료로 변환. 
# tuple()   튜플형 자료로 변환.
# list()    리스트형 자료로 변환
# dict()    딕셔너리형 자료로 변환
# set()     집합 자료로 변환 

# bool형
print(bool(1))      # True
print(bool(0))      # False
print(bool(-1))     # True
print(bool(''))     # False
print(bool(' '))    # True
print(bool('a'))    # True
print(bool([]))     # False
print(bool([-1]))   # True
# bool형은 값이 존재하면 True, 정수 0, ''(NULL), [](빈자료)인 
# 경우는 거짓으로 판별. 
'''
# int() 자료 변환
print(int(1.0))
print(int(1.1))
print(int('1'))
# print(int('1.0'))  # ValueError

# int()함수의 확장 사용
print(int('0xA',16))
print(int('0b1010',2))
print(int('A',16))
print(int('1010',2))

# float() 자료의 변환
print(float(1))         # 1.0
print(float('1'))       # 1.0
print(float('1.0'))     # 1.0

#문자형(str()) 자료의 변환
print(str(1))           # '1'
print(str(0))           # '0'
print(str(-1))          # '-1'
print(str(True))        # 'True'
print(str([]))          # '[]'
print(str([-1]))        # '[-1]'

