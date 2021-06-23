'''
#break
while True:
    a=int(input("정수 입력[0입력시 종료] : "))
    if a==0:
        break  #조건식을 나감 반복을 멈춤
    print("입력값 출력 : ",a)

#continue 이용
a=0
while a < 5: #0~5까지 5번 반복
    a+=1
    if a==3:  #a==3이면 참이 됨으로 바로 조건식으로 이동해서 3이 출력X //나가지 않지만 조건식을 반복해서 본다
        continue
    print("a={}".format(a))

count=0
for x in range(2,101):
    flag = True  #True이면 소수 
    #소수 판별... 
    for y in range(2,x):
        if x%y==0:
            flag=False
            break
    if flag:
        print(x,end=" ")  #소수출력
        count += 1
print()
print(count,"개의 소수가 존재함!!")

#중복 while 중복 for구문이랑 비슷 대신 조건이 다름. (while:회차가 정하기 어려울때)
# 문제 1] 1)변수선택: 쌀, 한쌍의 쥐,날짜
# 쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있습니다. 
# 쥐 한 마리가 하루 20g씩 쌀을 먹고 있습니다. 
# 10일 마다 쥐의 수가 2배씩 증가하고 있다면, 
# 며칠 만에 창고의 쌀이 모두 쥐의 먹이가 될까? 
# 또, 이때에 쥐는 총 몇마리가 되어 있을까? 
# (쌀 한통는 1kg, 쥐는 쌀은 먹은 후 2배로 증가하는 조건)
# [결과] : 80일, 512마리

#문제 3,4,5는 for로도 가능
# 문제2] turtle을 통해서 만든 다각형 그리는 코드를 반복문으로 사용하여 작성
#       (3 ~ 12까지의 값을 입력 받아서 하시오)

# 문제3] 1 ~ 100까지의 합을 구하는 코드를 작성

# 문제4] 1부터 1씩 증가하는 값에 대해 누적합을 구할 때 10,000보다 큰 누적합 값에
#       대해 마지막에 더해진 값이 얼마인지 구하시오

# 문제5] 1부터 100 사이의 소수(prime number)를 출력하고 개수를 구하시오 
# booL형 자료를 이용한 알고리즘... flag기법
'''

'''
# 문제6] 다음과 같은 모형으로 출력되게 하세요. (단, 파이썬 서식을 사용안함. ) 서식문자사용X
#6-1         6-2         6-3         6-4
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
x=0
star="*"
et=" "
while True:
    line=int(input("홀수 줄을 입력하세요: "))
    for x in range(line):
        flag=True
        x+=1
        empty=line-x
        if x%2==0:
            flag=False
            continue
        if flag:
            print(empty//2*et,end='');print(x*star)
        if x == line:
            flag=False
            continue
        else: print(et*x,end='');print(empty//2*star)

            