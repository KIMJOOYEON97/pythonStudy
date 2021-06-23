'''
#List() => 리스트 자료형으로 변환  #리스트는 문자열을 각각 나름의 집합으로 변경시킴
print(list('12345')) #['1','2','3','4','5']
print(list((1,2,3,4,5))) #[1,2,3,4,5]

#tuple()=>튜플 자료형으로 변환
print(tuple('12345'))   #('1','2','3','4','5')
print(tuple([1,2,3,4,5])) #(1, 2, 3, 4, 5)

#dict()=> 사전형 자료로 변환
print(dict((('a',1),('b',2)))) #{'a': 1, 'b': 2}

#set()=>집합형 자료로 변환 #데이터를 한꺼번에 가지고 잇음
print(set('12345'))   #임의로 해당값을 정함{'3', '1', '4', '2', '5'}
print(set([1,2,3,4,5])) #숫자를 정렬{1, 2, 3, 4, 5}



# 예제1] 변수 선언
var1=1
var2,var3=2,3
var4= var5 =4
print(var1,var2,var3,var4,var5)

#예제2] 변수 사용(연산)
su1=100
su2=200
Sum=su1+su2
print(Sum)
# 문자열의 연산처리
Sum2 = str(su1)+str(su2)
print(Sum2)  #100200   문자열에서 더하기는 이어붙이기이다!!

#[문제1]: num1(10)+num(20)=30 출력하세요. 단 10,20,30은 변수를 사용하여 출력
num1,num2=10,20
Sum= num1+num2
print("{}+{}={}".format(num1,num2,num1+num2))
print("num1({})+num2({})={}".format(num1,num2,Sum))


#[문제2] num1=7 num2=5 위 값의 연산 결과(+,-,*,/)를 각각의 변수에 저장한 후 출력 
# (각 연산 결과에 대한 변수를 생성해서 저장하세요.)
num1=7 
num2=5
a=num1+num2 #Sum
b=num1-num2 #Sub
c=num1*num2 #Mul
d=num1/num2 #Div
print("더하기 결과 : {}+{}={}".format(num1,num2,num1+num2))
print("빼기 결과 : {}-{}={}".format(num1,num2,num1-num2))
print("곱하기 결과 : {}*{}={}".format(num1,num2,num1*num2))
print("나누기 결과 : {}/{}={}".format(num1,num2,num1/num2))
print(a,b,c,d)
print("{}\n{}\n{}\n{}".format(a,b,c,d))


#[문제3] 다음과 같이 출력되게 코딩하세요 단, 변수를 사용해 함. 
# 1)Python 100점!!! 
# 2)나는 오늘 행복합니다!!! 
# 3)Python.C언어,JAVA 3과목 점수를 각 변수에 저장 저장된 값을 사용하여 합계와 평균을 구하는 프로그램을 작성
# (평균은 소수점2자리까지)

Python=100;t='!!!'
print("Python {}점{}" .format(Python,t))
a,b,c='나','오늘','행복'
print("{}는 {} {}합니다{}".format(a,b,c,t))
str1='Python 100점!!!'
str2='나는 오늘 행복합니다!!! '
print(str1);print(str2)

Python,C,JAVA=80,76,100
Sum= Python+C+JAVA
avg = Sum/3
print("3과목의 합계 : {} 평균 {:.2f}점".format(Sum, avg))


#[문제4]자료형의 변환 
# su=100,num='100',flt=1.111의 변수를 선언 후에 
# 이 변수를 이용하여 다음과 같은 출력결과가 나오게 코드를 작성하세요 
# 출력결과 200 / 101.111 / 100100

su,num,flt=100,'100',1.111
print(su+int(num))
print(int(num)+flt); print(float(num)+flt)
print(str(su)+num)


#input() -print와 반대 개념으로 문자/숫자를 입력받는 함수 
# -사용자로부터 데이터를 입력받아 변수에 저장가능 
# -값을 입력받아 연산처리해야 하는 경우에 
# ***반드시 형변환 작업이 필요함 
# (input()는 받은 입력값의 자료형 'str'(기본값))

print(input())
print(input("test입력값을 처리합니다. 문자열 입력하세요 : "))


#예제1] 두 수를 입력 받아 합을 출력하는 예제
num1 = input("첫번째 정수 입력 : ")
num2 = input("두번째 정수 입력 : ")
print("형변환전 계산")
print(num1+num2) #문자열이라 이어붙어버림
print("형변환후 계산")
num3 = int(num1)+int(num2)
print(num3)

#예제2]입력 값을 두 개 받아서 출력하는 예제(데이터 타입)
su1=int(input("정수입력 : "))    #받자마자 바로 정수로 받아서 변수에 집어 넣음 
su2=float(input("실수 입력 : "))
print("su1={}".format(type(su1)))
print("su2={}".format(type(su2)))


#예제3] 두 정수를 입력받아 사칙연산 결과를 출력하는 예제
num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번째 정수 입력 : "))
print("num1+num2={}".format(num1+num2))
print("num1-num2={}".format(num1-num2))
print("num1*num2={}".format(num1*num2))
print("num1/num2={:.2f}".format(num1/num2))

#[입력 함수=문제1] 학생 이름과 국어,영어, 수학 점수를 입력받아 출력하세요. 
#(입력예제) 
# 학생 이름 : 홍길동 
# 국어 점수 : 
# 영어 점수 : 
# 수학 점수 :  
# (출력예제)
# =================학생정보===================
# 이름   국어    영어    수학    합계    평균 
# 홍길동   90     90      100    280   93.33

name=input("학생 이름 : ")
a=int(input("국어 점수 : "))
b=int(input("영어 점수 : "))
c=int(input("수학 점수 : "))
Sum=a+b+c
avg=Sum/3
print("{:=^65}".format('학생정보'))
print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}"\
    .format('이름','국어','영어','수학','합계','평균'))
#print("{}\t{}\t{}\t{}\t{}\t{}".format())
print("{:<10}{:<12}{:<12}{:<12}{:<12}{:<8.2f}".format(name,a,b,c,Sum,avg))



#문제2]사용자로부터 이름 , 키 , 체중 값을 입력 받아 비만도를 구하고
#출력하는 코드를 작성하시오
# 비만도 계산 식 : 비만도 (%) = 현재 체중 / 표준 체중 * 100
# 표준체중 계산 식 : 표준 체중 = (현재 키- 100) * 0.9
# 출력예제 : 홍길동님의 비만도는 112.15% 입니다
name=input("이름 : ")
cm=float(input("키 : "))
kg=float(input("체중 : "))
avg=(cm-100)*0.9
fat=kg/avg*100
print("{}님의 비만도는 {:.2f}% 입니다".format(name,fat))


#Turtle 모듈 사용하기: 그림 또는 표를 만드는 모듈 
# (사용방법)
# import turtle => turtle에 있는 모든 내용을 불러옴 
# 
# Turtle에서 사용하는 함수들... 
# -forward(distance) :distance 만틈 앞으로 이동(선을 출력)
# -backword(distance) :distance 만틈 뒤으로 이동(선을 출력) 
# -left(angle):angle 만큼 좌회전 
# -right(angle):angle 만큼 우회전 
# -goto(x,y): 그림의 포인터를 좌표(x,y축만큼)로 이동 
# -color(color):지정한 color 선색을 결정 
# -width(width):지정한 width로 선두께를 결정
# -bgcolor(color):지정한 색으로 배경색을 결정  
# -speed(int): 지정된 int(0~10)값으로 애니메이션 속도 조절 
# -penup(): 화면에 선을 그리지 않게 설정 
# -pendown():화면에 선을 그리게 설정 
# -mainloop():프로그램이 종료되지 않고 유지하게 설정


#삼각형 만들기
import turtle

turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.mainloop()



#문제] input() 사용하여 정삼각형을 그리는 코드 
# (한변의 길이값 입력)
a=int(input("한변의 길이값 입력 : "))
import turtle
turtle.forward(a)
turtle.left(120)
turtle.forward(a)
turtle.left(120)
turtle.forward(a)
turtle.left(120)
turtle.mainloop()


#문제2] input() 사용하여 사각형의 가로,세로 길이를 입력받아 사가경을 그리는 코드
a=int(input("가로길이 입력 : "))
b=int(input("세로길이 입력 : "))
import turtle 
turtle.forward(a)
turtle.left(90)
turtle.forward(b)
turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(b)
turtle.left(90)
turtle.mainloop()

#문제2] input() 사용하여 사각형의 가로,세로 길이를 입력받아 사가경을 그리는 코드
a=int(input("가로길이 입력 : "))
b=int(input("세로길이 입력 : "))
import turtle 
turtle.forward(a)
turtle.left(360/4)
turtle.forward(b)
turtle.left(360/4)
turtle.forward(a)
turtle.left(360/4)
turtle.forward(b)
turtle.left(360/4)
turtle.mainloop()


#문제3]input() 사용하여 한변의 길이 값을 입력받고, 해당 길이의 정육각형을 그리는 코드 작성

a=int(input("한변의 길이값 입력 : "))
import turtle
turtle.forward(a)
turtle.left(360/6)
turtle.forward(a)
turtle.left(360/6)
turtle.forward(a)
turtle.left(360/6)
turtle.forward(a)
turtle.left(360/6)
turtle.forward(a)
turtle.left(360/6) 
turtle.forward(a)
turtle.left(360/6) 
turtle.mainloop()
'''

#문제3]input() 사용하여 한변의 길이 값을 입력받고, 해당 길이의 정육각형을 그리는 코드 작성

a=int(input("한변의 길이값 입력 : "))
import turtle
turtle.speed(8)
turtle.forward(a)
turtle.right(60)
turtle.forward(a)
turtle.right(60)
turtle.forward(a)
turtle.right(60)
turtle.forward(a)
turtle.right(60)
turtle.forward(a)
turtle.right(60)
turtle.forward(a)
turtle.right(60)
turtle.mainloop()
