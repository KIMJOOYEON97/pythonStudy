'''
# 예제 3] 입력값을 받아서 입력값이 1이면, "1입력"출력
#       10보다 큰 값을 입력하면, "10보다 큰 값을 입력했습니다."
#       10보다 작은 값을 입력하면, "10보다 작은 값을 입력했습니다."
num3 = int(input("정수 입력 : "))
if num3 == 1:
    print("1입력")
if num3 > 10:
    print("10보다 큰 값을 입력했습니다.")
if num3 !=1 and num3 < 10:
    print("10보다 작은 값을 입력했습니다.")

# 예제 4] 멤버연산자, 식별 연산자를 이용한 if
x = 15
if x in (10,11,15):
    print("x변수의 값은 Members에 속해 있습니다.")
if type(x) is int :
    print("x변수의 값은 INT형 자료입니다.")

# if ~ else 조건 구문
# : 의미는 조건문이 참이면, if의 종속문장을 실행, 
#  조건문이 거짓이면, else의 종속문장을 실행. 
# 
# (형식)
# if (조건식):
#     종속문장1(if)
#     종속문장2(if)
# else:
#     종속문장1(else)
#     종속문장2(else)
# (메인 프로그램 코드 진행) 

# 예제 5] 입력값을 받아서 받은 입력값이 10보다 크고,
#  15보다 작은 경우 "10보다 크고 15보다 작은 값 입력", 
#  이외의 값에 대해서 "범위를 벗어난 값 입력!!" 출력하는 예제
num5 = int(input("정수 입력 : "))
if num5 > 10 and num5 < 15:
    print("10보다 크고 15보다 작은 값 입력!!")
else:
    print("범위를 벗어난 값 입력!!")

# 예제 6] 수 입력 받아 100이면 "100입력", 
# 이외는 "100이외의 값 입력"
num6 = int(input("정수 입력 : "))
if num6 == 100:
    print("100입력")
else:
    print("100이외의 값 입력")

# pass 명령어
#  : if나 함수 등 종속문장을 사용하여 정의, 기술해야 하는 경우 
# 나중에 정의하고 사용할 목적으로 현재는 그냥 진행하게 하는 명령어 

# 예)
a = 0
if a == 0:
    pass  #나중에 코드를 입력할 예정, 주석으로 설명
print(a)


# if구문 문제
# 1. 입력 받은 데이터가 3의 배수인 경우 출력하는 코드 작성
nu1 = int(input("정수 입력 : "))
if nu1 %3 == 0: print("입력한 데이터 \"{}\"는 3의 배수입니다.".format(nu1))
else: print("입력한 데이터 \"{}\"는 3의 배수가 아닙니다.".format(nu1))
# 2. 절대값 구하는 프로그램을 만드세요.
nu2 = int(input("정수 입력[절대값] : "))
if nu2 < 0: nu2=-nu2;print("입력한 값의 절대값은 {} 입니다."\
    .format(nu2))
else:print("입력한 값의 절대값은 {} 입니다.".format(nu2)) 
# 3. 수를 입력받아 짝수, 홀수를 구분하여 출력하는 프로그램 작성 
nu3 = int(input("정수 입력[짝수/홀수] : "))
if nu3 % 2 == 0:print("입력값  {} 는 짝수 입니다.".format(nu3))
else:print("입력값 {} 는 홀수 입니다.".format(nu3))
# 4. 두수를 입력 받아 큰 수를 출력하는 프로그램을 작성
num1 = int(input("첫번째 정수 : "))
num2 = int(input("두번째 정수 : "))
if num1 > num2 : print("{}가 {}보다 크다".format(num1,num2))
if num1 == num2: print("두수의 크기는 값다")
if num1 < num2 : print("{}가 {}보다 크다".format(num2,num1))
# 5. 세수를 입력 받아 큰 수를 출력하는 프로그램을 작성
su1 = int(input("첫번째 정수 입력 : "))
su2 = int(input("두번째 정수 입력 : "))
su3 = int(input("세번째 정수 입력 : "))
if su1 > su2 and su1 > su3: print("가장 큰 정수:{}".format(su1))
if su1 < su2 and su2 > su3: print("가장 큰 정수:{}".format(su2))
if su3 > su2 and su1 < su3: print("가장 큰 정수:{}".format(su3))
# 6. 두수를 입력 받아 큰 수가 짝수이면 출력하는 프로그램을 작성
nu61 = int(input("첫번째 정수 : "))
nu62 = int(input("두번째 정수 : "))
if nu61 > nu62 and nu61 % 2 == 0:
    print("{}는 가장 큰 정수이면서 짝수입니다.".format(nu61))
if nu61 < nu62 and nu62 % 2 == 0:
    print("{}는 가장 큰 정수이면서 짝수입니다.".format(nu62))
# 7. 두수를 입력 받아 합이 짝수이고, 3의 배수인 수를 출력하는 
#    프로그램을 작성 
num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번째 정수 입력 : "))
Sum = num1 + num2
if Sum % 2 ==0 and Sum % 3 == 0 :
    print("입력한 두수의 합은 {}, 짝이면서 3의 배수입니다."\
        .format(Sum))

# 다중 if 구문
# : if 조건문이 참이 아니면, 다른 if구문(elif) 조건문을 비교,
# 이것도 참이 아니면, 최종적으로 else구문에 있는 종속문장을 실행
# 
# (형식)
# if (조건식1):
#     종속문장1(if)
#     종속문장2(if)
# elif (조건식2):
#     종속문장1(elif)
#     종속문장2(elif)
# ... (elif는 n개 생성 가능... )
# else:
#     종속문장1(else)
#     종속문장2(else)
# (메인 프로그램 코드를 실행)
#  사용용도 => 메뉴, 등급, 동등한 위치에서 비교 등으로 사용... 
# 
# 중복 if구문
# : if 구문 안에 또 다른 if구문을 만드는 형태
#  첫번째 if가 참 또는 거짓인 경우, 종속문장에 if구문을 추가하여
#  두번째 if구문의 조건을 보는 형태...  
# 
# (형식)
# if (조건식1):
#     종속문장1(첫번째 if)
#     if(조건식2):
#         종속문장1(두번째 if)
#     종속문장2(첫번째 if)
# (메인 프로그램 실행 코드)
#      

# 예제 7] 두수를 입력 받아 큰수가 짝수면 출력
num1=int(input("첫번째 정수 입력 : "))
num2=int(input("두번째 정수 입력 : "))
if num1 > num2:
    if num1 % 2 == 0:
        print("num1({})는 큰 수이면서 짝이다.".format(num1))
    else:
        print("num1({})는 큰 수이면서 홀수이다.".format(num1))
elif num2 > num1 :
    if num2 % 2 == 0:
        print("num2({})는 큰 수이면서 짝이다.".format(num2))
    else:
        print("num2({})는 큰 수이면서 홀수이다.".format(num2))
else:
    print("num1({})과 num2({})는 같다.".format(num1,num2))
'''

#1번
name = input("이름을 입력하세요 : ")
kie = float(input("{} 님의 키(cm)를 입력 하세요 : "\
    .format(name)))
wei = float(input("{} 님의 몸무게(kg)를 입력하세요 : "\
    .format(name)))
std = (kie - 100)*0.9
fat = wei/std * 100
if fat < 100 :
    level = "저체중"
elif fat >= 100 and fat < 110:
    level = "정상"
elif fat >= 110 and fat < 120:
    level = "과체중"
elif fat >= 120 and fat < 130:
    level = "비만"
else:
    level = "고도비만" 
print("{}님의 비만도는 {:.2f}% 로 {} 입니다."\
    .format(name,fat,level))

# 2
import turtle
num = int(input(" 3 ~ 10 까지의 값을 입력(다각형그리기) : "))
if num == 3:
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.mainloop()
elif num == 4:
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.mainloop()
elif num == 5:
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.mainloop()
elif num == 6:
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.mainloop()
elif num == 7:
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.mainloop()
elif num == 8:
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.mainloop()
elif num == 9:
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.mainloop()
elif num == 10:
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.forward(100)
    turtle.left(360/num)
    turtle.mainloop()
else: 
    print("그릴 수 없습니다.")

# 3
year = int(input("년도를 입력하세요 : "))
if year%4 == 0:
    if year%100==0:
        if year%400==0:
            print(year,"년도는 윤년입니다.")
        else:
            print(year,"년도는 평년입니다.")
    else:
        print(year,"년도는 윤년입니다.")
else:
    print(year,"년도는 평년입니다.")

