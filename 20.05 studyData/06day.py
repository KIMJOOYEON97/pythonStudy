'''
# 예제 3] 입력값을 받아서 입력값이 1이면, "1입력"출력 
#     10보다 큰 값을 입력하면, "10보다 큰 값을 입력했습니다." 
#     10보다 작은 값을 입력하면, "10보다 작은 값을 입력했습니다"
num3 = int(input("정수 입력 : "))
if num3==1:
    print("1입력")
if num3>10:
    print("10보다 큰 값을 입력했습니다.")
if num3 !=1 and num3 <10:
    print("10보다 작은 값을 입력했습니다.")
#10을 입력하면 아무것도 실행하지 않음

# 예제 4] 멤버연산자, 식별연산자를 이용한 if
x=15 #변수선언
if x in (10,11,15):
    print("x변수의 값은 Members에 속해 있습니다.")
if type(x) is int:  #int인지 아닌지 타입 구분
    print("x변수의 값을 INT형 자료입니다.")

#if~else 조건 구문 
# :의미는 조건문이 참이면, if의 종속문장을 실행, 
# 조건문이 거짓이면,else의 종속문장을 실행.(else:참이 아닌 나머지)

#(형식)
# if(조건식):
#   종속문장1(if)
#   종소문장2(if)
# else:
#   종속문장1(else)
#   종속문장2(else)
#(메인 프로그램 코드 진행)  
 
#예제 5] 입력값을 받아서 받은 입력값이 10보다 크고 15보다 작은 경우 "10보다 크고 15보다 작은 값입력", 
# 이외의 값에 대해서 "범위를 벗어난 값 입력!!"출력하는 예제 //#and연산자 둘다 충족/ or둘중 하나
num5=int(input("정수입력 : "))
if num5 >10 and num5<15:
    print("10보다 크고 15보다 작은 값입력")
else:
    print("범위를 벗어난 값 입력!!")

#예제 6] 수 입력 받아 100이면 "100입력", 이외는 "100이외의 값 입력"
num6=int(input("정수입력 : "))
if num6==100:
    print("100입력")
else:
    print("100이외의 값 입력")

# pass 명령어 
# :if나 함수 등 종속문장을 사용하여 정의, 기술해야 하는 경우 
#  나중에 정의하고 사용할 목적으로 현재는 그냥 진행하게 하는 명령어 (내 파트의 코드가 정상적으로 작동하는지 확인) 

#예)
a= 0
if a==0:
    pass #나중에 코드를 입력할 예정,주석으로 설명
    print(a) #실행을 안하는 것은 아니다. indendtion error가 안뜸
print(a)

#if 구문 문제
# 1. 입력 받은 데이터가 3의 배수인 경우 출력하는 코드 작성
# 2. 절대값 구하는 프로그램을 만드세요   ??
# 3. 수를 입력 받아 짝수, 홀수 를 구분하여 출력하는 프로그램 작성
# 4. 두 수를 입력받아 큰 수를 출력하는 프로그램을 작성
# 5. 세 수를 입력받아 큰 수를 출력하는 프로그램을 작성
# 6. 두 수를 입력받아 큰 수가 짝수이면 출력하는 프로그램을 작성
# 7. 두 수를 입력 받아 합이 짝수이고, 3의 배수인 수를 출력하는 프로그램을 작성

#1
x=int(input("정수 입력 : "))
if x%3==0:
    print("입력한 데이터 \"{}\" 3의 배수 입니다".format(x))
else:
    print("입력한 데이터 \"{}\"는 3의 배수가 아닙니다." .format(x))
#2
x2=int(input("수입력[절대값] :"))
if x2<0:
    print(x2*-1)
else:
    print(x2)
#풀이
if x2 <0: x2=-x2;print("입력한 값의 절대값은 {}입니다.".format(x2))
else:print("입력한 값의 절대값은 {}입니다.".format(x2))
#3
x3=int(input("정수 입력:"))
if x3%2==0:
    print("짝수입니다.")
if x3%2==1:
    print("홀수입니다.")
#else:print("입력값 {}는 홀수입니다.".format(x3))

#4 if~else 구문을 쓰기는 애매하다. 두번씩 실행할 가능성이 높기때문
a=int(input("정수 입력 : "))
b=int(input("정수 입력 : "))
if a>b:
    print("{}가 {}보다 크다" .format(a,b))
if a<b:
    print("{}가 {}보다 크다" .format(b,a))
if a==b:
    print("두 수의 크기는 같다.")
#5 
A=int(input("1정수 입력 : "))
B=int(input("2정수 입력 : "))
C=int(input("3정수 입력 : "))
if A>B and A>C:
    print("가장 큰 정수:{}".format(A))
if B>A and B>C:
    print("가장 큰 정수:{}".format(B))
if C>B and C>A:
    print("가장 큰 정수:{}".format(C))
#6 
X=int(input("1정수 입력 : "))
Y=int(input("2정수 입력 : "))
if X>Y and X%2==0:
    print("{}는 가장 큰 정수이면서 짝수입니다.".format(X))
if Y>X and Y%2==0:
    print("{}는 가장 큰 정수이면서 짝수입니다.".format(Y))

#7 
num1=int(input("1정수 입력 : "))
num2=int(input("2정수 입력 : "))   #Sum =num1 + num2
if (num1+num2)%2==0 and (num1+num2)%3==0:
    print("입력한 두수의 합은 {}, 짝이면서 3의 배수입니다.".format(num1+num2))
else:
    print("두 수를 입력 받아 합이 짝수이고, 3의 배수인 수가 아닙니다.")


#다중 if 구문
# :if조건문이 참이 아니면, 다른if구문(elif) 조건문을 비교,
# 이것도 참이 아니면, 최종적으로 else구문에 있는 종속문장을 실행 
# //if 조건문은 하나임-조건에 부합되는 하나만 실행/ 첫번째 조건이 부합되면 첫번째만 함. 두번째 조건을 제시 f)else는 나머지
# 
# (형식)
# if(조건식):
#   종속문장1(if)
#   종속문장2(if)
# elif(조건식):
#   종속문장1(elif)
#   종속문장2(elif)
# ...(elir n개 생성가능)->1000개도 가능
# else:
#   종속문장1(else)
#   종속문장2(else)
# (메인 프로그램 코드 실행)
# 사용용도 =>메뉴, 등급, 동등한 위치에서 비교 등으로 사용... 
# 
# 중복 if 구문 / 논리연산을 쓰는 것과 유사 //선행조건이 참이거나 거짓이어야한다.
#                                   else에도 if를 넣으면 중복 if문이다.//조건 안에서 또다른 조건을 비교
# :if구문 안에 또다른 if구문을 만드는 형태
#  첫번째 if가 참 또는 거짓인 경우, 종속문장에 if 구문을 추가하여 
#  두번째 if구문을 보는 형태...
# 
# (형식)
# if (조건식1): 
#   종속문장1(첫번째if) 
#   if(조건식2):
#       종속문장1(두번째if)
#   종속문장2(첫번쩨if)
# (메인 프로그램 코드 실행)

# 예제7] 두 수를 입력 받아 큰 수가 짝수면 출력
num1=int(input("첫번째 정수 입력 : "))
num2=int(input("두번째 정수 입력 : "))
if num1>num2:
    if num1%2==0:
        print("num1({})는 큰 수 이면서 짝이다".format(num1))
    else:
        print("num1({})는 큰 수 이면서 홀수이다.".format(num1))
elif num2>num1:
    if num2%2==0:
        print("num2({})는 큰 수 이면서 짝이다".format(num2))
    else:
        print("num2({})는 큰 수 이면서 홀수이다.".format(num2))
else:
    print("num1({})과 num2({})는 같다".format(num1,num2))

#문제1].사용자로부터이름, 키, 체중값을입력받아비만도를구하고 //등급이 적혀잇음
# 결과를출력할때비만도값100을기준으로100 미만이면저체중, 
# 100 이상110 미만은정상, 110 이상120 미만과제중, 120 이상130 미만비만, 130 이상은고도비만으로출력하시오.
#비만도계산식: 비만도(%) = 현재체중/ 표준체중* 100
#표준체중계산식: 표준체중= (현재키–100) * 0.9
#출력예제: 홍길동님의비만도는112.15% 로과체중입니다.
x=input("사용자이름:")
y=float(input("사용자 키:"))
z=float(input("사용자 몸무게:"))
avg=(y-100)*0.9
fat=z/avg*100
if fat <100:
    print("{}님의 비만도는 {:2f}%로 저체중입니다." .format(x,fat))
elif 100<=fat<110 :
    print("{}님의 비만도는 {:2f}%로 정상입니다." .format(x,fat))
elif 110<=fat<120 :
    print("{}님의 비만도는 {:2f}%로 과체중입니다." .format(x,fat))
elif 120<=fat<130 :
    print("{}님의 비만도는 {:2f}%로 비만입니다." .format(x,fat))
elif fat>=130 :
    print("{}님의 비만도는 {:2f}%로 고도비만입니다." .format(x,fat))
'''
#풀이
x=input("사용자이름:")
y=float(input("사용자 키:"))
z=float(input("사용자 몸무게:"))
avg=(y-100)*0.9
fat=z/avg*100
if fat<100:
    level ="저체중"
elif fat>=100 and fat<110:
    level ="정상"
elif fat>=110 and fat<120:
    level ="과체중"
elif fat>=120 and fat<130:
    level ="비만"
else:
    level:"고도비만"
print("{}님의 비만도는 {:.2f}%로 {}입니다.".format(x,fat,level))

#문제2].turtle을사용하여3 ~ 10 까지의값을입력받아삼각형부터십각형까지그릴수있는코드를작성하시오.
# (위입력값의범위를초과하는경우“그릴수없습니다.” 라는메시지를출력)
import turtle
a=int(input("몇 각형을 그리겠습니까? : "))
if a==3:
    turtle .forward(50)
    turtle .left(360/3)
    turtle .forward(50)
    turtle .left(360/3)
    turtle .forward(50)
    turtle .left(360/3)
    turtle .mainloop()
elif a==4:
    turtle .forward(50)
    turtle .left(360/4)
    turtle .forward(50)
    turtle .left(360/4)
    turtle .forward(50)
    turtle .left(360/4)
    turtle .forward(50)
    turtle .left(360/4)
    turtle .mainloop()
elif a==5:
    turtle .forward(50)
    turtle .left(360/5)
    turtle .forward(50)
    turtle .left(360/5)
    turtle .forward(50)
    turtle .left(360/5)
    turtle .forward(50)
    turtle .left(360/5)
    turtle .forward(50)
    turtle .left(360/5)
    turtle .mainloop()
elif a==6:
    turtle .forward(50)
    turtle .left(360/6)
    turtle .forward(50)
    turtle .left(360/6)
    turtle .forward(50)
    turtle .left(360/6)
    turtle .forward(50)
    turtle .left(360/6)
    turtle .forward(50)
    turtle .left(360/6)
    turtle .forward(50)
    turtle .left(360/6)
    turtle .mainloop()
elif a==7:
    turtle .forward(50)
    turtle .left(360/7)
    turtle .forward(50)
    turtle .left(360/7)
    turtle .forward(50)
    turtle .left(360/7)
    turtle .forward(50)
    turtle .left(360/7)
    turtle .forward(50)
    turtle .left(360/7)
    turtle .forward(50)
    turtle .left(360/7)
    turtle .forward(50)
    turtle .left(360/7)
    turtle .mainloop()
elif a==8:
    turtle .forward(50)
    turtle .left(360/8)
    turtle .forward(50)
    turtle .left(360/8)
    turtle .forward(50)
    turtle .left(360/8)
    turtle .forward(50)
    turtle .left(360/8)
    turtle .forward(50)
    turtle .left(360/8)
    turtle .forward(50)
    turtle .left(360/8)
    turtle .forward(50)
    turtle .left(360/8)
    turtle .forward(50)
    turtle .left(360/8)
    turtle .mainloop()
elif a==9:
    turtle .forward(50)
    turtle .left(360/9)
    turtle .forward(50)
    turtle .left(360/9)
    turtle .forward(50)
    turtle .left(360/9)
    turtle .forward(50)
    turtle .left(360/9)
    turtle .forward(50)
    turtle .left(360/9)
    turtle .forward(50)
    turtle .left(360/9)  
    turtle .forward(50)
    turtle .left(360/9)
    turtle .forward(50)
    turtle .left(360/9)
    turtle .forward(50)
    turtle .left(360/9)
    turtle .mainloop()
elif a==10:
    turtle .forward(50)
    turtle .left(360/10)
    turtle .forward(50)
    turtle .left(360/10)
    turtle .forward(50)
    turtle .left(360/10)
    turtle .forward(50)
    turtle .left(360/10)
    turtle .forward(50)
    turtle .left(360/10)
    turtle .forward(50)
    turtle .left(360/10)
    turtle .forward(50)
    turtle .left(360/10)
    turtle .forward(50)
    turtle .left(360/10)
    turtle .forward(50)
    turtle .left(360/10)
    turtle .forward(50)
    turtle .left(360/10)
    turtle .mainloop()        
else:
    print("그릴 수 없습니다.")
#풀이
#num==7
#turtle. forward(100)
#turtle. lefr(360/num)


#문제3]윤년을구하는코드를작성하시오.
#-4의배수는윤년이된다. 그외는평년
#-4의배수면서100의배수인경우는평년이다. 그외는윤년
#-4 그리고100의배수이면서400의배수인경우윤년이다.
Y=int(input("년도를 입력하세요 : "))
if Y%4==0:
    if Y%100==0:
        print("{}년은 평년입니다.".format(Y))
        if Y%400==0:
             print("{}년은 윤년입니다.".format(Y))
    else:
        print("{}년은 윤년입니다.".format(Y))
else:
    print("{}년은 평년입니다.".format(Y))

'''
풀이
if Y%4==0:
    if Y%100==0:
        if Y%400==0:
             print("{}년은 윤년입니다.".format(Y))
        else:
            print("{}년은 평년입니다.".format(Y))
    else:
        print("{}년은 윤년입니다.".format(Y))
else:
    print("{}년은 평년입니다.".format(Y))
'''