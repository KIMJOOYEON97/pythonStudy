'''
#연산자: 프로그램에서 특정한 계산을 위해서 사용하는 기호들을 의미함 
# (1) 산술연산자 
# "+" : 두 피연산자의 더한 결과를 반환 
# "-" : 두 피연산자의 뺀 결과를 반환
# "*" : 두 피연산자의 곱한 결과를 반환
# "/" : 두 피연산자의 나눈 결과를 반환 실수 값
# "//": 두 피연산자의 나눈 결과를 반환 (나누기의 몫을 반환)
# "%" : 두 피연산자의 나눈 결과의 나머지를 반환
# "**" : 좌측 피연산자를 우측 피연산자의 값으로 거듭제곱 처리 값을 반환

#예제1]3과 2를 가지고 위 연산식을 계산 예시들
print("{}+{}={}".format(3,2,3+2))
print("{}-{}={}".format(3,2,3-2))
print("{}*{}={}".format(3,2,3*2))
print("{}/{}={}".format(3,2,3/2))
print("{}//{}={}".format(3,2,3//2))
print("{}%{}={}".format(3,2,3%2))
print("{}**{}={}".format(3,2,3**2))

#"%" 나머지 연산이 사용되는 곳 
# 1) 정수의 짝수/홀수 구할 경우에 사용 2로 나머지 연산했을 때 0==짝수 1==홀수
    # 홀수: 3%2=>1, 5%2=>1, 7%2=>1 
    # 짝수: 2%2=>0, 4%2=>0, 6%2=>0 
# 2)배수 관계 확인할 때 사용 
    #3의 배수 : x%3=>0이면, 3의 배수 
# 3)각 숫자의 자리를 구할 때 사용 
    # 123의 값의 각 자리 수 구하기 
    # 1의 자리:123%10 =>3
    # 10의 자리:(123//10)%10 =>2 
    # 100의 자리: (123//100)%10 =>1 
# 4)범위 내에 숫자를 구할 때 
    # 어떤 값을 넣어도 1~6 사이의 값을 출력 
    # => (x%6)+1 
    #     x%6=>(0,1,2,3,4,5)+1


#(2)비교 연산자 (조건문할 때 중요!!, 참일 경우에만 반복.)
#  : 두 피연산자의 값을 비교하여 "참(True)" 또는 "거짓(False)"을 
#    판별하는 연산자 
# "==": 두 피연산자의 값을 비교. 같으면 "참", 다르면 "거짓"<같다>(대입연산자 좌측에 있는 것과 우측에 있는 것을 대입하겠다)
# "!=": 두 피연산자의 값을 비교. 같으면 "거짓", 다르면 "참"<다르다>(!팩토리얼:반대의 의미)
# ">" : 두 피연산자의 값을 비교(크다). 
#       왼쪽이 크면 "참", 반대면 "거짓"(같아도 거짓)
# "<" : 두 피연산자의 값을 비교(작다). 
#       오른쪽이 크면 "참", 반대면 "거짓"(같아도 거짓)
# ">=": 두 피연산자의 값을 비교(크거나 같다) 
#       왼쪽이 크거나 같으면 "참", 왼쪽이 작으면 "거짓"
# "<=": 두 피연산자의 값을 비교(작거나 같다) 
#       오른쪽이 크거나 같으면 "참", 오른 쪽이 작으면 "거짓"
print(3==2)  #F
print(3!=2)  #T
print(3>2)   #T
print(3<2)   #F
print(3>=2)  #T
print(3<=2)  #F

#(3)논리 연산자(비교 대상이 다르다<=비교 연산자: 값에 대한 비교// 논리 연산자:조건에 대한 참거짓 비교)
# : 두 피연산자의 값(참/거짓)을 비교 비교하여 참/거짓을 판별하는 연산 
# "and" : 논리곱. 두 피연산자가 둘다 "참"이면 참을 반환 
#       둘중 하나라도 거짓이면 "거짓"
# "or"  : 논리합. 두 피연산자 중 하나라도 "참"이면 "참"을 반환 
#       둘다 "거짓"이면 "거짓"
# "not" : 부정. 오른쪽 피연산자의 값이 "참"이면 "거짓"
#         "거짓이면 "참" <반대>

# and : 논리곱 (1=참, 0=거짓)
print((1==1)and(1==1))  #참
print((1==1)and(1==0))  #거짓
print((1==0)and(1==1))  #거짓 *Short cut 연산
print((1==0)and(1==0))  #거짓
# Short cut 연산이란? 이미 결과가 나온 경우. 이후 연산을 하지 않는 것을 의미 
# 불필요한 연산을 안한다(효율성,빠르게 계산하기 위해서). 컴퓨터는 대부분 거짓을 우선으로 봄. 뒤에 안본다.
# 
# or : 논리합 (0이 아닌 값=참(1,2), 0=거짓)
print((1==1)or(1==1))  #참
print((1==1)or(1==0))  #참
print((1==0)or(1==1))  #참
print((1==0)or(1==0))  #거짓 

#not(참 거짓에 대한 결과에 대한 부정)
print(not(1==1))  #F
print(not(1==0))  #T

#(4) 멤버 연산자 
# : 피연산자 내의 멤버의 존재에 대한 질의 
# "in" :왼쪽 피연산자가 오른쪽 멤버 중에 일치하는 값이 존재하면 "참", 그렇지 않으면 "거짓" 
# "not in" :왼쪽 피연산자가 오른쪽 멤버 중에 일치하는 값이 없으면 "참", 일치하면 "거짓"

#in
print(1 in(1,2,3)) #T  ():튜플 []:리스트
print(5 in (1,2,3))#F

#not in
print(1 not in [1,2,3]) #F
print(5 not in [1,2,3]) #T

#(5) 식별 연산자 :두개의 피연산자를 비교하여 객체(대상의 타입,형태) 값이 동일한지 아닌지 구분
# "is" : 두 피연산자의 식별 값을 비교하여 같으면 "참", 다르면 "거짓"
# "is not" : 두 피연산자의 식별 값을 비교하여 다르면 "참", 같으면 "거짓"

# is: 같으면 "참"
print(type(1)is int) #T
print(type(1)is str) #F

# is not: 같지 않으면 "참"
print(type('1')is not int) #T
print(type('1')is not str) #F

#(6) 비트 연산자 : 두 피연산자의 bit값을 가지고 처리하는 연산자들을 의미함.((2진수로 변환하여)bit값으로 연산)
# 
# "&": 두 피연산자의 and bit 연산하는 연산자
#   10 & 6 => 0000 1010 (10)
#           & 0000 0110 (6)
#          =================
#             0000 0010 (2)

#"|" : 두 피연산자의 or bit 연산하는 연산자
# 10 & 6 => 0000 1010 (10)
#         | 0000 0110 (6)
#          =================
#           0000 1110 (14)

# "~" : 우측 피연산자에 대한 not bit 연산하는 연산자 <비트부정>
#        (보수관계: 채우는 값 1의보수는 1을 채웠을 때 채워짐)
#     ~0 => ~ 0000 0000 (0) <8bit>
#        ===================
#             1111 1111 (-1)  <-사인드 비트
#      왜? 사칙연산에서 빼기를 cpu가 계산을 못함. 그러므로 양수에 음수를 더하는 것으로 계산한다.

# "^" : 두 피연산자에 대한 XOR(배타적 논리합) bit연산하는 연산자
#       배타적 논리합(XOR)는 두 피연산장 중 하나가  "참 이면 "참"
#       둘다 참이면 "거짓" ,즉, 둘중 하나만 "참"인 경우 "참" 논리연산자
#       (둘다 값이 같으면 0(거짓), 둘의 값이 다르면 1(참) like.자석)
#   15^10=> 0000 1111 (15) 평문
#           0000 1010 (10) 키
#          ===============         암호화 키값=10
#           0000 0101 (5) 암호문
# 
# "<<": 왼쪽 피연산자의 비트를 오른쪽 연산자의 값만큼 이동(왼쪽) <shift 이동 연산자>
#       2<<2  0000 0010 (2)
#        <<           2
#           ===============    <곱하기2*4=8 원래수*2의 2승> 
#             0000 1000 (8)
# ">>" :왼쪽 피연산자의 비트를 오른쪽 연산자의 값만큼 이동(오른쪽)
#       8>>2  0000 1000 (8)
#          >>         2   
#         ===============      <나누기 8/4=2 원래수/2의 2승>
#             0000 0010 (2)   
#   **쉬프트 연산은 2의 배수관계를 이용한 정수 곱하기, 정수 나누기 <몫만 출력, 나머지 출력X>

#(7) 기타 연산자들 
# "=" : 대입연산자 =>왼쪽 피연산자에 오른쪽 피연산자를 대입(대입=복사한다.)
# (복합 대입 연산자) 
# : 복합 대입 연산자란? 대입 연산자와 산술 연산자를 합쳐서 사용 하는 연산자를 의미함 
# "+=","-=","*=","%=","//="... 등이 존재하고, 
# 의미는 왼쪽 피연산자와 오른쪽 피연산자를 산술 계산한 후에 왼쪽 피연산자에 값을 저장

print(10&2)
print(10|6)
print(~0)
print(~11)
print(15^10)
print(2<<2)
print(8>>2)

a=0
a+=10 # a=a+10  a=10
print(a)
a-=5  # a=a-5   a=5
print(a)
a*=5  # a=a*5   a=25
print(a)
a//=5 # a=a//5  a=5
print(a)
a%=3  # a=a%3   a=2
print(a)
a/=2  # a=a/2   a=1.0
print(a)

# 문제] 다음에 대한 답을 적으세요
# 1) 7>18 거짓
# 2) 5<2  거짓
# 3) 6%3>2 거짓
# 4) 5+5 != 2*5 거짓
# 5) True ==1 참
# 6) 1=='1' 거짓       숫자==문자
# 7) 10//3==10%3 거짓  3==1
# 8) 15%4 in (0,1,2) 거짓 



# 조건식  
# if(조건 분기문) 
# - 조건식이 참인 경우에는 if의 종속문장을 실해 
# - 참이 아닌 경우에는 if의 종속문장을 실행하지 않는다. 
# - if 종속문장을 작성할 경우 "반드시(***)" tab을 통해서 들여쓰기 
#   (파이썬은 들여쓰기 "코드 블럭"을 구분) (같은 위치에 있으면 같은 코드블럭, 다른 위치에 있으면 다름)
# 
# (형식) ":"=내용이 있다
# if(조건식):
#    종속문장1(if)
#    종속문장2(if) 
# (메인프로그램 실행코드)

# if의 들여쓰기 잘못된 경우 예
num = int(input("정수 입력 : "))
if num==1:
print("1입력")  #IndendtationError(한칸이라도 띄어쓴 것이 있으면 이런 에러가 뜬다.)

#정상적인 경우
num = int(input("정수 입력 : "))
if num==1:
    print("1입력")

#예제1]입력값 받아서 홀수 /짝수 구분하는 예제
num1=int(input("정수 입력 : "))
if num1 % 2 ==0:
    print("num1의 변수 값은 짝수입니다.")
    print("num1의 변수 값은 2의 배수입니다.")
if num1 % 2 ==1:
    print("num1의 변수 값은 홀수입니다.")
print("프로그램 종료")
'''
#예제2] 메뉴 선택시 동작 시키는 프로그램

print("======메뉴======")
print("1.Easy Game Start")
print("2.Hard Game Start")
print("3.Exit")
num2=int(input("번호선택>>>"))
if num2==1:
    print("Easy Game Starting.....")
if num2==2:
    print("Hard Game Starting.....")
if num2==3:
    print(" Game Exit")