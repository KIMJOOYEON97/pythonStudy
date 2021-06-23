'''
a=int(input("한변의 값을 입력하세요 : "))
import turtle
turtle.forward(a)
turtle.right(120)
turtle.forward(a)
turtle.right(120)
turtle.forward(a)
turtle.right(120)
turtle.mainloop()

a=int(input("길이: "))
import turtle
turtle.speed(1)
turtle.bgcolor("red")
turtle.forward(a)
turtle.left(60)
turtle.forward(a)
turtle.left(60)
turtle.forward(a)
turtle.left(60)
turtle.forward(a)
turtle.left(60)
turtle.forward(a)
turtle.left(60)
turtle.forward(a)
turtle.left(60)
turtle.mainloop()


import turtle
turtle.bgcolor("black")
turtle.pencolor("red")
turtle.color("white")
turtle.speed(2)
turtle.pendown()
turtle.goto(0,-60)
turtle.penup()
turtle.left(120)
turtle.forward(30)
turtle.left(90)
turtle.forward(10)
turtle.circle(30)
turtle.mainloop()


if True:
    print('a')

if False:
    print('b')

x=11
if x>10:
    print("x는 10보다 크다")
if x in (10,11,12):
    print("x는 10,11,12 중 하나에 포함 된다.")
if type(x)is int:
    print('x는 int형 자료이다.')
if x>10 and x!=15:
    print("x는 10보다 크면서 15는 아니다")

userin=int(input("정수 값 입력: "))
if userin%2==0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

x=int(input("정수 입력 : "))
if x%3==0:
    print("3의 배수입니다.")
else:
    print("3의 배수가 아닙니다.")


a=int(input("정수 값을 입력하세요 : "))
b=int(input("정수 값을 또 입력하세요 :"))
if a>b:
    print("{}-{}={}".format(a,b,a-b))
else:
    print("{}-{}={}".format(b,a,b-a))

a=int(input("정수 값을 입력해: "))
b=int(input("정수 값을 입력해주세여..: "))
if (a%2==0 and b%2==0)or(a%2==1 and b%2==1):
    print("{}+{}={}".format(a,b,a+b))
else:
    print("{}*{}={}".format(a,b,a*b))

from random import random
a=int(random()*90+10)
b=int(random()*90+10)
print("a의 값은 {}입니다".format(a))
print("b의 값은 {}입니다".format(b))
userin=int(input("{}+{}=".format(a,b)))
if userin==a+b:
    print("정답입니다.")
else:
    print("오답입니다.")

score=int(input("점수 입력 : "))
if 90<=score<=100:
    print("수입니다.")
elif 80 <= score <90:
    print("우입니다.")
elif 70<= score <80:
    print("미입니다.")
elif 60<= score <70:
    print("양입니다.")
else:
    print("가입니다.")

score=int(input("점수 입력 : "))   #????????????????????????
if 90<=score<=100:
    print("수입니다.")
if 80 <=score<90:
    print("우입니다.")
if 70<=score<80:
    print("미입니다.")
if 60<=score<70:
    print("양입니다.")
else:
    print("가입니다.")

score=int(input("점수 입력 : "))
if 0<=score<=100:
    if 90<=score<=100:
        print("수입니다.")
    elif 80 <= score <90:
        print("우입니다.")
    elif 70<= score <80:
        print("미입니다.")
    elif 60<= score <70:
        print("양입니다.")
    else:
        print("가입니다.")
else:
    print('잘못된 입력 값입니다.')


name=input("이름:")
cm=int(input("키:"))
kg=int(input("몸무게:"))
avg=(cm-100)*0.9
fat=(kg/avg)*100
if fat<100:
    print("{}님의 비만도는 {:.2f}%로 저체중입니다.".format(name,fat))
elif 100<=fat<110:
    print("{}님의 비만도는 {:.2f}%로 정상입니다.".format(name,fat))
elif 110<=fat<120:
    print("{}님의 비만도는 {:.2f}%로 과체중입니다.".format(name,fat))
elif 120<=fat<130:
    print("{}님의 비만도는 {:.2f}%로 비만입니다.".format(name,fat))
elif fat>130:
    print("{}님의 비만도는 {:.2f}%로 고도비만입니다.".format(name,fat))


year=int(input("몇 년도 입니까? :")) #이거 너무 어렵다ㅠ
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("{}년은 윤년입니다.".format(year))
        else:
            print("{}년은 평년입니다.".format(year))
    else:
        print("{}년은 윤년".format(year))   
else:
    print("{}년은 평년입니다.".format(year))
   

for cnt in range(10):
    print("반복 출력")
for cnt in range(10):
    print("{}번째 반복".format(cnt))
for x in range(10):
    print(x)
for x in range(5,10):
    print(x)
for x in range(1,10,2):
    print(x)

for x in range(10,0,-1):
    print(x,end="")
print("")
for char in 'abcde':
    print("\t{}".format(char))

for tup in (1,2,3,4,5):
    print(tup)

for x in range(3):
    for y in range(5):
        print(x,y)

for x in range(1,10):
    for y in range(1,10):
        print("{}*{}={}".format(x,y,x*y))

''' 

for x in range(1,21):
    print(int(x),end=" ")
print("")
for x in range(1,20):
    if x%2==0:
        print(x,end=" ")
print("")
for x in range(100,50,-1):
    if x%2==1:
        print(x,end=" ")
print("")

for x in range(1,51):
    if x%5==0:
        print(x)
    else:
        print(x,end=" ")
print("")

tot=0
for x in range(1,101):
    tot=tot+x
print(tot)
print("")

#]문제 6,7,8번 다시 풀기

from random import randint
c=randint(65,90)
print(chr(c))
c=randint(97,122)
print(chr(c))

for y in range(10):
    for x in range(8):
        c=randint(97,122)
        print(chr(c),end=" ")
print()

for y in range(10):
    for x in range(16):
        z=randint(0,2)
        if z==0:
            c=randint(97,122)
            print(chr(c),end="")
        elif z==1:
            c=randint(65,90)
            print(chr(c),end="")
        elif z==2:
            c=randint(0,9)
            print(c,end="")
    print()