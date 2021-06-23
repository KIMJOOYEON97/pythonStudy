'''
# while 구문
# : 조건식이 참인 경우에 반복하는 반복문
# 
# (형식)
# while (조건식):
#     종속문장1
#     종속문장2
# (메인 프로그램 코드 실행)
# 
# 예)
# while x<10:
#     종속문장1
#     종속문장2
#     x = x +1 # X+=1 => 조건식에 변화를 주는 값이 필요함.
# (메인 프로그램 코드 실행) 
# 

# 예제 1] while구문을 이용한 반복문(짝수의 함, 홀수의 합)
i = 1
odd_sum = 0
even_sum = 0
while i <= 10:
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
    i += 1 # i = i + 1
print("짝수의 합 : {}, 홀수의 합 : {}".format(even_sum,odd_sum))

# while ~ else 를 사용
i = 0
while i < 5:
    print("{}번 종속문장 실행".format(i))
    i += 1
else:
    print("조건식이 거짓인 경우에 실행 문장")
print("메인 프로그램 실행 코드")

# while의 무한반복 
# : while 구문의 조건을 항상 참이되게 설정한 후에 반복문 내에 
# 제어를 위한 명령어를 실행하는 반복 구문
#  제어를 실행하는 명령어(반복문에 대한 제어) 
#  1. break => 반복의 종료
#  2. continue => 반복시 조건문으로 이동
# 
# (형식)
# while True:
#     종속문장1
#     종속문장2
#     (종료하기 위한 조건과 명령어 : break)
# 위와 같은 코드에서는 break를 사용하지 않으면 무한반복함.
# 무한히 반복되면서 다음으로 코드 진행되지 않기 때문에 정지한 것
# 같이 보이게 됨. 때문에 반복에서 벗어나기 위해서 
# "break"명령어를 적절히 사용해야 함.
# 
# (break 사용예)
# while True:
#     종속문장1
#     break
#     종속문장2
# (메인 프로그램 코드)
# 
# 프로그램 흐름 : 1) while의 조건식  2)종속문장1 3)break
#                4) 메인 프로그램 코드
# 
# (continue 사용예) => 반복문 종료는 아님. 조건식으로 이동
#
# while True:
#     종속문장1
#     continue
#     종속문장2
# (메인 프로그램 코드)
# 
# 프로그램 흐름 : 1)while의 조건식 2)종속문장1 3)continue
#               4)while의 조건식 5)종속문장1 6)continue 
#               7)while의 조건식 ... 
# 종속문장2는 실행하지 않음    
 

# 예제 2] break와 continue 사용 예제

# break 이용
while True:
    a = int(input("정수 입력[0입력시 종료] : "))
    if a == 0:
        break
    print("입력값 출력 : ",a)

# continue 이용
a = 0
while a < 5:
    a += 1
    if a == 3:
        continue
    print("a = {}".format(a))

# 문제 1] 
# 쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있습니다. 
# 쥐 한 마리가 하루 20g씩 쌀을 먹고 있습니다. 
# 10일 마다 쥐의 수가 2배씩 증가하고 있다면, 
# 며칠 만에 창고의 쌀이 모두 쥐의 먹이가 될까? 
# 또, 이때에 쥐는 총 몇마리가 되어 있을까? 
# (쌀 한통는 1kg, 쥐는 쌀은 먹은 후 2배로 증가하는 조건)
# [결과] : 80일, 512마리
#
rice = 100*1000
mice = 2
day = 1
while True:
    rice -= 20*mice
    if day%10==0:
        mice *=2
    if rice <= 0:
        break
    day += 1
print("{}일만에 쥐는 {}마리가 됨.".format(day,mice))

# 문제2] turtle을 통해서 만든 다각형 그리는 코드를 반복문으로 사용하여 작성
#       (3 ~ 12까지의 값을 입력 받아서 하시오)
# 
import turtle
num = int(input(" 3 ~ 12까지 다각형 그리기 : "))
if num >=3 and num <=12:
    for x in range(num):
        turtle.forward(100)
        turtle.left(360/num)
    turtle.mainloop()
else:
    print("그럴수 없습니다.")

'''
# 문제3] 1 ~ 100까지의 합을 구하는 코드를 작성
Sum = 0
for x in range(1,101):
    Sum += x
print(Sum)

# 문제4] 1부터 1씩 증가하는 값에 대해 누적합을 구할 때 10,000보다 큰 누적합 값에
#       대해 마지막에 더해진 값이 얼마인지 구하시오
x = 1
Sum = 0
while True:
    Sum += x
    if Sum > 10000:
        break
    x += 1
print(x,"는 10000 되기 전에 더한 누적합!!!")

# 문제5] 1부터 100 사이의 소수(prime number)를 출력하고 개수를 구하시오 
#   bool형 자료를 이용한 알고리즘... 
count = 0
for x in range(2,101): 
    flag = True    # True이면 소수
    # 소수 판별... 
    for y in range(2,x):
        if x%y==0:
            flag=False
            break
    if flag:
        print(x,end=" ")    #소수출력
        count += 1
print()
print(count,"개의 소수가 존재함!!!!")

'''
# 문제6] 다음과 같은 모형으로 출력되게 하세요. (단, 파이썬 서식을 사용안함. )
6-1         6-2         6-3         6-4
*           *****           *       *****
**          ****           **        ****
***         ***           ***         ***
****        **           ****          **
*****       *           *****           *
6-5 출력 줄수를 입력하면 다음과 같이 출력
  입력 줄은 홀수이여야만 함. 

홀수 줄수를 입력: 7
   *
  ***
 *****
*******
 *****
  ***
   *
'''

