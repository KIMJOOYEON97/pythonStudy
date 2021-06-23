'''
# 반복문(for, while)
# 
# For구문 
#  : 가장 대표적인 반복 구문 중 하나로 주어진 조건에 따른 회차
#  만큼 반복
# 
# (형식)
# for 변수명 in range(반복횟수):
#     종속문장1(for)
#     종속문장2(for)
# (메인 프로그램 실행 코드 진행)
#

# range() 함수 : 파이썬 내장함수로 정해진 범위의 연속된 값을
#         만드는 함수
# 
# 사용법(range())
#  1. range(종료값)
#    : 0부터 시작해서 종료값 이전까지의 값의 범위를 가짐.
#   ex) range(10)   =>   [0,1,2,3,4,5,6,7,8,9]
#  2. range(시작값,종료값)
#    : 시작값부터 종료값 이전까지의 값의 범위
#   ex) range(5,10) =>   [5,6,7,8,9]
#  3. range(시작값,종료값,증감값)
#    : 시작값부터 종료값 이전까지 값의 증/감값 간격의 값 범위 
#   ex) range(0,10,2) => [0,2,4,6,8]
#       range(10,0,-2)=> [10,8,6,4,2]

# 예제 1] for 예제(range)
for x in range(10):
    print(x,end=' ')  # print()의 end인자값 설정하면 출력후
                      # 마지막에 사용될 문자를 지정할 수 있음.
                      # 사용 : end='문자열'  
print()  

# 예제 2] for문(range()2)
for x in range(5,10):
    print(x,end=' ')
print() # "\n" 문자를 출력하기 위해서

# 예제 3] for문(range()3) - 증가값 
for x in range(0,10,2):
    print(x,end=' ')
print()

# 예제 4] for문(range()4) - 증감값
for x in range(10,0,-2):
    print(x,end=' ')
print()

# 예제 5] for문 - 문자열
Sum = 0
for x in 'string':
    print(x,end='')
    Sum += 1
print();print(Sum)

# 예제 6] for문 - list,tuple, dictionary ... 
i = 0
for x in [1,4,78,'test','A',1.80,100]:
    print(x,end=' ')
    i += 1
print("\n",i,"번 반복함")

# 예제 7] 이중 For구문 : for구문을 중첩해서 사용하는 것
Sum = 0
for x in range(10):
    for y in range(10):
        Sum += 1   # Sum = Sum + 1
print(Sum)

# 중첩For문(이중For문)은 상위 For문 한번 실행할 때에
# 하위 For문은 자신에게 주어진 반복 횟수 만큼 실행.
# (하위 For문은 상위For문의 종속문장이기 때문)
# 이런식으로 반복하기 때문에 위 예제에서 Sum이 100번 동작하고,
# 결과가 100이되는 것임.(상위 1회가 하위 10회인 경우)
# 
# (형식)
# for x in range(반복횟수):
#     for y in range(반복횟수):
#         종속문장1(하위For문)  
#         종속문장2(하위For문)
#     종속문장3(상위For문)
# (메인 실행 코드)

# 예제 8] 이중 For문 예제
Sum = 0
for x in range(1,5,3): # [1,4] 값으로 2번 반복함
    for y in range(5,0,-1): # [5,4,3,2,1] 값으로 5번 반복함
        print("{} 상위 for문의 x의 값, {} 하위For문의 y의 값"\
            .format(x,y))
        Sum += 1
print(Sum,"횟수 만큼 반복함!!!")

# 문제1] 중첩 For문을 이용하여 구구단 표를 작성
# (출력 예시)
#   2 x 1 = 2  
#   2 x 2 = 4
#   2 x 3 = 6
#   2 x 4 = 8
#   ... 
for x in range(2,10): #[2,3,4,5,6,7,8,9]
    print("{}단".format(x))
    for y in range(1,10): #[1,2,3,4,5,6,7,8,9]
        print("{} x {} = {:<3}".format(x,y,x*y))
    print()

# 문제2] 중첩 For문을 이용하여 구구단 표를 작성
# 2 x 1 = 2   3 x 1 = 3   4 x 1 = 4   5 x 1 = 5   6 x 1 = 6   ...
# 2 x 2 = 4   3 x 2 = 6   4 x 2 = 8   5 x 2 = 10  6 x 2 = 12  ...
# 2 x 3 = 6   3 x 3 = 9   4 x 3 = 12  5 x 3 = 15  6 x 3 = 18  ...
# ....        ...         ...         ...         ...         
# 
for x in range(1,10):
    for y in range(2,10):
        print("{} x {} = {:<3}".format(y,x,x*y),end=' ')
    print()
print()
'''
# 문제3) 다음과 같이 출력되게 For구문을 작성하세요.... !!!!
# 상위 For문이 0일때, 하위 For문 : 0 0 0 0 0   
# 상위 For문이 1일때, 하위 For문 : 0 1 2 3 4   
# 상위 For문이 2일때, 하위 For문 : 0 2 4 6 8   
# 상위 For문이 3일때, 하위 For문 : 0 3 6 9 12  
# 상위 For문이 4일때, 하위 For문 : 0 4 8 12 16 
for x in range(5):
    print("상위 For문이 {}일때, 하위 For문 : "\
        .format(x),end='')
    for y in range(5):
        print("{}".format(x*y),end=' ')
    print()
print()

# 문제 4) 이중 For문을 사용하여 다음과 같이 출력되게 
# 만들어 보세요. 
#  1) 1   2   3   4   5
#     6   7   8   9   10
#     11  12  13  14  15
#     16  17  18  19  20
#     21  22  23  24  25

for x in range(5): #[0,1,2,3,4]
    for y in range(1,6): # [1,2,3,4,5]
        print(y+x*5,end="\t")
    print()
print()

# or
Sum = 0
for x in range(5):
    for y in range(5):
        Sum += 1
        print("{}".format(Sum),end="\t")
    print()
print()
#  2) 25  24  23  22  21
#     20  19  18  17  16
#     15  14  13  12  11
#     10   9   8   7   6
#      5   4   3   2   1 
Sum = 25
for x in range(5):
    for y in range(5):
        print("{}".format(Sum),end="\t")
        Sum -= 1
    print()
print()

for x in range(5,0,-1): #[5,4,3,2,1]
    for y in range(5): # [0,1,2,3,4]
        print(x*5-y,end="\t")
    print()
print()

#  3)  1   2   3   4   5
#      2   3   4   5   1
#      3   4   5   1   2
#      4   5   1   2   3
#      5   1   2   3   4 

for x in range(5): #[0,1,2,3,4]
    for y in range(5): # [0,1,2,3,4]
        print((x+y)%5+1,end="\t")
    print()
print()
