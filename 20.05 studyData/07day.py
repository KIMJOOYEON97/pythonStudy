'''
# 반복문(for,while)

# for구문: 가장 대표적인 반복 구문 중 하나 주어진 조건에 따른 회차만큼 반족
# 
# (형식)
# for 변수명 in range(반복횟수):
#   종속문장1(for)
#   종속문장2(for)
# (메인 프로그램 실행 코드 진행)

# range 파이썬 기본 내장 함수
# range() 함수 : 파이썬 내장함수로 정해진 범위의 연속된 값을 만드는 함수
# 
# 사용법(range()) *종료값은 안 나온다!!!
# 1. range(종료값):0부터 시작해서 종료값 *이전까지의 값의 범위를 가짐.
# ex)range(10) => [0,1,2,3,4,5,6,7,8,9]    10(반복횟수,반복회차)개의 숫자를 만들어냄
#  in(멤버연산자) range()=(집합묶음)
# 2.range(시작값, 종료값): 시작값부터 종료값 *이전까지의 값의 범위
# ex)range(5,10) => [5,6,7,8,9]
# 3.range(시작값, 종료값, 증감값): 시작값부터 종료값 *이전까지 값의 증/감값 간격의 값 범위 
# 증감값:증가 또는 감소값
# ex)range(0,10,2) => [0,2,4,6,8] *10은 아니다
#    range(10,0,-2) => [10,8,6,4,2] *0은 아니다

#예제1] for 예제(range)
for x in range(10):  #x in range(10)-조건문 x가 [0,1,2,3,4,5,6,7,8,9]안에 들어가야 실행한다.
    print(x,end=' ')  #print()의 end인자값 설정하면 출력후 마지막에 사용될 문자를 지정할 수 있음. 
                      #사용 : end='문자열'
print()
for x in range(10):
    print(x)
print()

#예제2] for문(range()2)
for x in range(5,10):
    print(x,end=' ')
print() #"\n"문자를 출력하기 위해서

# 예제3] for문(range()3) -증가값
for x in range(0,10,2):
    print(x,end=" ")
print() #이것은 반복문이 아니다. 반복문에 속해있지X

#예제4]for문(range()4) -증감값
for x in range(10,0,-2):
    print(x, end=" ")
print()

# 예제5] for문- 문자열 (자바에도 잇음)
Sum=0
for x in 'string':
    print(x,end="") #end="" : Null
    Sum += 1        #반복구문이 등장할때마다 1씩 증가.
print();print(Sum)

# 예제6] for문 - List, tuple, dictionary... 
i=0
for x in [1,4,78,'test','A',1.80,100]:
    print(x,end=" ")
    i += 1
print("\n",i,"번 반복함")

#이중for문 중요! -데이타처리를 table식으로 하기때문에.(이차원에서 표그릴때,데이터 처리할때)
#               / 3중 4중 for문 있지만 그림이나 그래프 그릴 때 씀  
#                 +a 최소화하기위해서 변수값 이용(turtle 예시)
#이중 for구문 : for구문을 중첩해서 사용하는 것
             #자전거 앞바퀴가 크다. 그래서 작은 뒷바퀴가 더 많이 돈다
             # 상위  for 문 한번 실행할 때 하위 for문 10번 실해한다./like톱니바퀴
# 예제7]
Sum=0
for x in range(10):
    for y in range(10):
        Sum += 1  # Sum = Sum + 1
        print(x,y)
print(Sum)

# 중첩for문(이중for문)은 상위 For문 한번 실행할 때에 
#                       하위 For문은 자신에게 주어진 반복 횟수 만큼 실행. 
#                       (하위 for문은 상위 for문의 종속문장) 
# 이런 식으로 반복하기 때문의 위 예제에서 Sum이 100번 동작하고 결과가 100이 되는 것임.(상위 1회가 하위 10회인 경우)
#  
# (형식)
# for x in range(반복횟수):     #range아니여도 됌, list, 문자열 다 가능
#   for y in range(반복횟수):
#           종속문장1(하위for문) 
#           종속문장2(하위for문) 
#   종속문장3(상위for문)
# (메인 실행 코드)

# 예제 8] 이중 for문
Sum=0
for x in range(1,5,3): #[1,4] 값으로 2번 반복함
    for y in range(5,0,-1): #[5,4,3,2,1] 값으로 5번 반복함
        print("{}는 상위 For문의 x의 값,{}는 하위 for문의 y의 값" .format(x,y))
        Sum +=1
print(Sum,"횟수 만큼 반복함!!!")


# 문제 1] 중첩 For문을 이용하여 구구단 표를 작성
# (출력예시)
#   2 x 1 = 2  
#   2 x 2 = 4
#   2 x 3 = 6
#   2 x 4 = 8
#   ...
Sum=0
for x in range(2,10):           #[2,3,4,5,6,7,8,9]
    print(x,"단")
    for y in range (1,10):      #[1,2,3,4,5,6,7,8,9]
        print("{}x{}={}".format(x,y,x*y))
        Sum+=1
    print()
print(Sum,"횟수 만큼 반복함.")
'''
#문제 2] 중첩 For문을 이용하여 구구단 표를 작성 #기준점에 따라 달라짐 ?다시보기
# 2 x 1 = 2   3 x 1 = 3   4 x 1 = 4   5 x 1 = 5   6 x 1 = 6   ...
# 2 x 2 = 4   3 x 2 = 6   4 x 2 = 8   5 x 2 = 10  6 x 2 = 12  ...
# 2 x 3 = 6   3 x 3 = 9   4 x 3 = 12  5 x 3 = 15  6 x 3 = 18  ...
# ....        ...         ...         ...         ...         
for x in range(1,10):
    for y in range(2,10):
        print("{}x{}={}".format(y,x,x*y), end="\t") #print("{}x{}={:<3}".format(y,x,x*y), end=" ")
    print()

#문제 3] 다음과 같이 출력되게 For구문을 작성하세요...!
# 상위 For문이 0일때, 하위 For문 : 0 0 0 0 0   
# 상위 For문이 1일때, 하위 For문 : 0 1 2 3 4   
# 상위 For문이 2일때, 하위 For문 : 0 2 4 6 8   
# 상위 For문이 3일때, 하위 For문 : 0 3 6 9 12  
# 상위 For문이 4일때, 하위 For문 : 0 4 8 12 16 
for x in range(5):
    print("상위 For문이 {}일때 하위 For문 : ".format(x), end="")
    for y in range(5):
        print(x*y,end=" ")  #print("{}".format(x*y),end="")
    print()
print()

# 문제 4) 이중 For문을 사용하여 다음과 같이 출력되게 ????
# 만들어 보세요. 
#  1) 1   2   3   4   5
#     6   7   8   9   10
#     11  12  13  14  15
#     16  17  18  19  20
#     21  22  23  24  25 

'''
for x in range(5): #[0,1,2,3,4]
    for y in range(1,6): #[1,2,3,4,5]
        print(y+x*5,end="\t")
    print()
print()

#or
Sum=0
for x in range(5): #[0,1,2,3,4]
    for y in range(5): #[0,1,2,3,4]
        Sum+=1
        print("{}".format(Sum),end="\t")
    print()
print()
'''
#2)
# 25  24  23  22  21  
# 20  19  18  17  16  
# 15  14  13  12  11  
# 10  9   8   7   6   
# 5   4   3   2   1
Sum=0
for x in range(25,0,-5):
    for y in range(5):
        Sum +=1
        print("{}".format(Sum),end="\t")
    print()
print()
'''
Sum=25
for x in range(5):
    for y in range(5):
        print("{}".format(Sum), end="\t")
        Sum -=1
    print()
print()

for x in range(5,0,-1): #[5,4,3,2,1]
    for y in range(5): #[0,1,2,3,4]
        print(x*5-y,end="\t")
    print()
print()
'''
#3)
# 1   2   3   4   5     
# 2   3   4   5   1   
# 3   4   5   1   2   
# 4   5   1   2   3   
# 5   1   2   3   4
#  if 사용가능한 것과 다른 것 2개
Sum=0
for x in range(1,6):
    print(x, end=" ")
    for y in range(4):
        print(Sum,end=" ")
    print()
print()

Sum=4
for x in range(5):
    for y in range(5):
        Sum+=1
        print("{}".format(Sum%5+1),end="\t")
    print()
print()
'''
for x in range(5): #[0,1,2,3,4]
    for y in range(5): #[0,1,2,3,4]
        print((x+y)%5+1,end="\t")
    print()
print()

Sum=4
for x in range(5):
    for y in range(5):
        Sum+=1
        print("{}".format(Sum%5+1),end="\t")
    print()
print()

'''
'''
# turtle을통해서만든다각형그리는코드를반복문을사용하여작성하시오.(3 ~ 12 까지의값을입력받아서하시오)
import turtle
a = int(input("몇각형을 그리겠습니까? : "))
for x in range(a):
    turtle .forward(100)
    turtle .left(360/a)
'''
# #