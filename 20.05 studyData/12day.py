'''
#(실습)
#위에서 학습한 내용을 토대로 다음과 같은 내용을 프로그램하세요.
#  
#  아래와 같은 메뉴를 만들고, 친구 이름을 관리하는 코드를 작성
#  (리스트를 사용해서 작성하세요) 
 
 -------------------------
 1. 친구 리스트 출력         #등록한 친구 목록 보기
 2. 친구 추가                #친구 등록하기(정보는 문제3번 참조)            
 3. 친구 삭제                #등록 친구 삭제
 4. 이름 변경                #이름 변경
 0. 종료                     #프로그램 종료
 메뉴를 선택하세요 : 2
 이름을 입력하시오 : 홍길동
 -------------------------   
''' 
'''
import os

fr=[]
idx=0
while True:
    os.system("cls")  #화면이 깔끔하게 
    print("-"*30)
    print("1. 친구 리스트 출력")    #현재는 리스트에 저장되어 있어서 종료되면 날아감. 데이터베이스 연동하면 저장됌
    print("2. 친구 추가")           #친구 이름 말고 다른 것을 넣는 것도 한번 해보기^^
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("0. 종료")
    print("-"*30)
    sel =input("메뉴를 선택하세요 : ")   #정수화 하지않는다. 잘못 입력했을 때 value에러 막기위해
    if sel == '1':
        print(fr) #친구리스트 출력/ for구문 사용도 가능
        os.system('pause')  #결과 값을 보여주는 것
    elif sel == '2':
        name=input("이름을 입력하시오: ") #친구 추가
        fr.append(name)
        os.system('pause')
    elif sel =='3':
        name=input("삭제할 친구 이름 입력하시오: ")
        if name in fr:
            fr.remove(name) #remove는 리스트에 없으면 오류가 뜬다. ->리스트 안에 있는지 먼저 검증=> if구문
        else:
            print("삭제할 친구가 없습니다.")    #함수의 요구사항 먼저보고 오류를 막자
        os.system('pause')
    elif sel =='4':
        name=input("변경할 대상 이름 입력하시오 : ")  #대상을 찾는것
        if name in fr:
            idx = fr.index(name)
        else:
            print("수정할 친구가 없습니다.")
            os.system('pause')
            continue #continue하면 메뉴로 돌아감(조건문으로 이동, 밑에 있는 것 출력)
        mod_name = input("변경할 이름을 입력하세요 : ") #변경하 이름 받음
        fr[idx]=mod_name    #insort를 사용해도 됌.
        os.system('pause')

    elif sel== '0':
        print("프로그램 종료!!")
        break    #종료
    else:
        print("메뉴선택 오류!!!")
        print("다시 입력하세요.")
        os.system("pause") #키를 입려하기 전까지 일시정지. system 명령어 cls를 사용하면 정리함 pause를 사용해서 정리하기 전의 모습 보여줌
'''
#  튜플(tuple) 
# : 리스트와 비슷한 자료형으로 튜플 안에 다양한 형태의 값을 사용할 수 있음
# 
# (형식)
# 튜플변수명 =(value1,value2,value3,.....)    #튜플은 값이 변경 불가능하기 때문에 비어있는 튜플 만들지X
# 
# 리스트와 튜플의 차이점
# 1. 리스트는"[]"를 사용하지만, 튜플은 "()"를 사용한다.
# 2. 리스트는 그 값을 생성, 삭제, 수정이 가능하지만,
#    튜플은 그 값을 바꿀 수 없음(중요!!)  //새롭게 선언하는 건 가능하나 값 변경은 안됌
# 3. 튜플은 멤버(요수)의 값이 1개인 경우 반드시 뒤에 ","를 붙여야 한다.
#    예] tu =(1,)  , tu=(1)(X) => 튜플이 아니라 그냥 int
# 4. 튜플은 가장 외각에 있는 "()"는 생략이 가능함
#    예] tu = 10,20,30 =>튜플인데 소괄호를 생략한 것
# 
# 튜플의 인덱싱
# :튜플도 리스트와 같이 인덱싱을 통해서 값에 접근
# 
# 예] 
# 인덱스 값(+)    0  1  2  3  4  5  6  7  8 
# 인덱스 값(-)   -9 -8 -7 -6 -5 -4 -3 -2 -1
#   튜플        ( 1, 2, 3, 4, 5, 6, 7, 8, 9)
# 
# 튜플의 슬라이싱(slicing)
# : 튜플의 특정 범위의 값에 접근하기 위한 방법으로 리스트와 동일하게 사용
 
# 예제1] 튜플의 정의 및 사용
tu = (1,2,3,4,5)
print(tu,type(tu))
print(tu[0])        #1
print(tu[1])        #2
print(tu[-1])       #5
print(tu[0:3])      #(1,2,3)
print(tu[3:])       #(4,5)

tu1 ='문자열',100,123.456
print(tu1,type(tu1))        # ('문자열', 100, 123.456) <class 'tuple'>
tu2 =(10)
print(tu2,type(tu2))        # 10 <class 'int'>
tu3=(10,)
print(tu3,type(tu3))        # (10,) <class 'tuple'>
tu4=10,
print(tu4,type(tu4))        # (10,) <class 'tuple'>

# 예제2] 튜플의 특성 =>변경되지 않는 시퀸스
tu =(1,2,3,4,5)
# tu[0]=100     #TypeError:튜플은 생성된 값을 변경X
# 'tuple' object does not support item assignment
#안에 있는 내용 변경을 허용하지 않는다. =>값을 수정할 수 없다.//인덱스 참조 슬라이싱은 괜찮은데
print(tu) 
# 값을 수정하는 방법   1)새롭게 만들던지 2)리스트로 바꾸던지

# 튜플의 결합1(병합) =>시퀸스 자료형 가능
a= 1,2,3
b= 4,5,6
c=a+b
print(c,type(c)) 

# 튜플의 결합2(확장)
tu1 = 10,20,30
tu2 = 40,50,60
tu1 = tu1+tu2       #새로운 tu1이 만들어짐 
print(tu1,type(tu1))

# 튜플을 리스트 변경
lst = list(tu1)
print(tu1) #(10, 20, 30, 40, 50, 60) 튜플
print(lst) #[10, 20, 30, 40, 50, 60] 리스트

# 리스트를 튜플로 변경
tu=tuple(lst)
print(tu,type(tu)) 

# packing 과 unpacking =>시퀸스 자료 전체에 해당 copy도 마찬가지
# : 튜플과 같은 자료형으로 묶어서 사용하는 것을 packing
# 반대로 묶여진 튜플과 같은 자료형을 나눠서 사용하는 것을 unpacking
# 
# 예](1,2),(3,4)
# packing   => pack = ((1,2),(3,4))  #끝에 있는 소괄호 생략 가능 (1,2),(3,4)
# unpacking => a,b = pack   #a=(1,2) ,b=(3,4)

print("packing")
tup1=(1,2),(3,4) #(1,2)(3,4)를 하나로 묶어서 tup1이라는 pack을 만듬
print(tup1)
print(tup1[0]);print(tup1[1])

print("unpacking")
x,y=tup1    # x, y =(1,2), (3,4)  =>여러 개의 변수를 한번에 선언하는것 unpacking을 이용한 것
print(x)
print(y)

#예제3]
pack = 1,2,'패킹'
a,b,c=pack
print(pack)     #패킹
print(a,b,c)    #언패킹  

# 튜플의 함수 =>추가, 제거, reverse등등 이런 리스트 함수 사용 불가.(값을 변경하지 않고 수정하지않는 것만 가능)
# -index(value) : 튜플에 있는 값에 해당하는 멤버의 인덱스 값을 반환
# -count(value) : 튜플에 있는 값의 개수를 반환

#예제4]
tu = (100,200,'함수',100,'개수')  #해당 값 없으면 error뜨는 것 똑같음
print(tu.index(200))    #1     
print(tu.index(100))    #0          T.index(value, [start, [stop]]) 
print(tu.count(100))    #2

# pdf page 39
# 문제 1.numbers = (10, 20, 30, 40, 50, 60, 70)
# 위 튜플 자료에서 30과 40을 따로 num1, num2 변수에 할당하시오. 
numbers = (10, 20, 30, 40, 50, 60, 70)
num1 =numbers[2]
num2 =numbers[3]
print(num1, num2)
num1= numbers.index(30)
num2= numbers.index(40)
print(numbers[num1],numbers[num2])
#풀이
numbers = (10, 20, 30, 40, 50, 60, 70)
idx1=numbers.index(30)
idx2=numbers.index(40)
num1 = numbers[idx1]
num2 = numbers[idx2]
print(num1, num2)

# 문제 2.menu = (('칼국수', 6000), ('비빔밥', 5500), ('돼지국밥', 7000))
# 위 자료의 값을 다음의 양식처럼 출력하시오.
#칼국수-6,000원
#비빔밥-5,500원
#돼지국밥–7,000원
menu = (('칼국수', 6000), ('비빔밥', 5500), ('돼지국밥', 7000))
a,b,c=menu
print("{}-{:,}원\n{}-{:,}원\n{}-{:,}원".format(a[0],a[1],b[0],b[1],c[0],c[1]))
#풀이 - 이차원 리스트 사용
for x in range(len(menu)):
    print("{} - {:,}원".format(menu[x][0],menu[x][1]))
print()
#or
for val in menu:
    print("{} - {:,}원".format(val[0],val[1]))
print()
#or
for x in range(len(menu)):
    for y in range(1):
        print(menu[x][y],end=' ')
        y+=1
        print("-{:,}원" .format(menu[x][y]))

'''
# [ Tuple 종합 문제 ]
1. 여러 개의 값을 패킹시킨 후 저장되어 있는 값을 빼내어 
  출력 하시오. (5개 값 저장)
( Tuple의 값을 리스트에 저장하시오. 단, Len함수를 이용)
2.아래와 같이 출력 시키시오
----------------------------------------------------
     (Tuple)          (List)
    회사정보     :   삼성전자
    제품명       :    Galaxy
    가격정보     :    100원
    출시일       :    미정
----------------------------------------------------
3. 위에서 출력 한 내용을 업데이트 하시오. 
[ 단, Index, Insert, Remove 함수를 전부 사용할 것 ]
가 격 : 100 -> 110
출시일 : 미정 -> 이번 달 말
'''

#1
tu=('(Tuple)','회사정보','제품명','가격정보','출시일')
lst=['(List)','삼성전자','Galaxy','100원','미정']
lst1=list(tu)
#풀이
#1
tut=(200602,'화요일','python',31.5,6000)
lst1=[]
for i in range(len(tut)):
    lst1.append(tut[i])
print(lst1)

#2
print("-"*50)
for x in range(len(tu)):
    print("{:^15}:{:^15}".format(tu[x],lst[x]))
print("-"*50)
#풀이
tu ='회사정보','제품명','가격정보','출시일'
lst=['삼성전자','Galaxy','100원','미정']
print("-"*40)
print(" "*5,"(Tuple)\t\t(List)")
for i in range(len(tu)):
    print(" "*5,"{}\t:\t{}".format(tu[i],lst[i]))
print("-"*40)
#3
idx1=lst.index('100원')
num1=lst[idx1]
lst.remove(num1)
lst.append('110원')

idx2=lst.index('미정')
num2=lst[idx2]
lst.remove(num2)
lst.insert(idx2,'이번 달 말')

print("-"*50)
for x in range(len(tu)):
    print("{:^15}:{:^15}".format(tu[x],lst[x]))
print("-"*50)
#풀이
tu ='회사정보','제품명','가격정보','출시일'
lst=['삼성전자','Galaxy','100원','미정']
a = lst.index("100원")
b = lst.index("미정")
lst.remove("100원")
lst.remove("미정")
lst.insert(a,"110원")
lst.insert(b,"이번 달 말")
print("-"*40)
print(" "*5,"(Tuple)\t\t(List)")
for i in range(len(tu)):
    print(" "*5,"{}\t:\t{}".format(tu[i],lst[i]))
print("-"*40)

# 딕셔너리 - 시퀸스 자료형. - 지금까지 나왔던 특징 똑같다.
# index가 아니다. index를 사용하지 않고 key값(=카테고리 안에서 찾음)을 사용
# 사전 - 'a'와 관련된 것 카테고리로 나눠져서 찾음
# 자료에 대한 직관적인 값을 찾기가 쉽다. 의미있는 key값을 가지고 찾아서 쉽고 빠르게 값을 찾을 수 있음
# key와 value값 동시에 넣음
# 나머지는 거의 비슷 결합이나 그런 것 비슷, 튜플과 다르게 값변경 가능
#  