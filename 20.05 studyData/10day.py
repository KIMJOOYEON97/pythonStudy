# ASCII코드
# 미국 표준 문자 코드로 7bit(0~127)로 하나의 문자를 표현할 수 있음.
# ASCII코드는 통신상 기본 문자 코드로 사용되고 있음.
#  
# (특징)
# 1. 프린트 가능한 문자 총 95자, 나머지 33개 문자는 프린트가 불가능한 문자.
#    프린트 가능한 문자의 시작 0x20(32)->"공백"부터 시작, 0x7e(126)까지 임.
# 2. 숫자는 0x30(48)="0"에서 부터 0x39(57)="9"까지 값을 가진 10개의 코드
# 3. 영문 대문자 0x41(65) =>"A"에서부터 0x5A(90)="Z"
# 4. 영문 소문자 0x61(97) =>"a"에서 0x7A(122)="z"까지
# 5. ASCII코드는 문자이나 숫자(정수)로 표현이 가능함.
# 
# 숫자를 문자(ASCII)변경하는 함수 : chr() (character의 약자)
# :chr()는 "()"안에 ASCII코드의 숫자값을 전달하면 문자로 출력

print(chr(0x41))
print(chr(65)) #"A"

#문제5]'A'~'Z'까지의 임의 문자 3자리를 출력하는 코드를 작성하세요.!!
from random import random
for x in range(3):
    print(chr(int(random()*26)+65),end="")
print()
#풀이
from random import random,randint,randrange

for x in range(3):
    ch = int(random()*26)+65 #65~90
    print(chr(ch),end=" ")
print()


# LIST -sequence자료의 특성이기도 한다. 조금씩 차이가 나는 부분만 기억해두자
# 리스트 자료형이란?
#  -데이터 목록을 다루는 자료형 (책의 목차리스트와 비슷, 실제 데이터의 위치, 변수와 유사)
#  -리스트를 정의할 때는 "[]"를 사용함.
#  -리스트 안에는 어떤 종류의 자료형이든 상관없니 저장 가능.(자료들의 집합)
#
#list 자료형의 기본 사용(정의) 
# 
# (정의)
# 변수명 =[]        #비어있는 리스트를 선언(변수선언과 비슷)
# 변수명 =[value1,value2,value3,value4,.....]
# (value들의 타입은 상관없이 가능) 
# 
# (list()를 이용한 리스트 생성)
#  변수명 = list()  #비어있는 리스트를 선언
#  변수명 = list("Hello")   #['H','e','l','l','o']
#  변수명 = list(range(5))  #[0,1,2,3,4]
 
#예제1] 리스트의 선언 및 값에 대한 처리
lst = [1,2,3,4,5,6,7,8]
print(lst,type(lst))        #[1,2,3,4,5,6,7,8]<class 'list'>
# 생성된 리스트에 대한 특정 값 참조: 인덱스(index)값을 이용
# 인덱싱 방법: 변수명[인덱스값]   #주의)인덱스 값은 시작값이 0부터 시작
print(lst[0]);print(lst[3])    #0번에 속하는 1출력/ 3번에 속하는 4출력

# 인덱싱을 이용한 list값 변경
lst[0] = lst[5]   #부분적으로 인덱스의 값을 변경할 수 있다.
print(lst[0])
print(lst) 

# 리스트 자료의 길이(요소[멤버]의 갯수):len() 자료의 길이값을 알아오는 함수(요수(멤버)의 갯수)
print("lst의 길이:",len(lst))       # 8 즉, 요소[멤버]개수를 출력

# 리스트의 결합1(병합)
lst2=[9,10]
print(lst+lst2)    #리스트가 합쳐저서 확장됌.=병합 //문자열 붙여질때랑 똑같음///문자열도 sequence 자료
lst3= lst+lst2      #[6,2,3,4,5,6,7,8] +[9,10] =>[6,2,3,4,5,6,7,8,9,10]
print(lst3) 

# 리스트의 결합2(확장)
lst = lst+lst2      # lst +=lst2
print(lst)          #[6,2,3,4,5,6,7,8,9,10]

# 리스트의 반복
print(lst2*3)       #[9,10,9,10,9,10]

# max(),min()
# lst=[6,2,3,4,5,6,7,8,9,10]
print(max(lst))        # 10
print(min(lst))        # 2
'''
# 변수를 선언하여 3개의 정수를 입력받아 합을 출력하는 코딩
# 출력결과>> "합계 = xx " "합계"도 변수로 저장하여 사용
a=int(input("정수를 입력하세요: "))
b=int(input("정수를 입력하세요: "))
c=int(input("정수를 입력하세요: "))
d= "합계 ="
lst=[d,a,b,c]
print(lst,a+b+c)
#풀이
a=int(input("첫번째 정수를 입력하세요: "))
b=int(input("두번째 정수를 입력하세요: "))
c=int(input("세번째 정수를 입력하세요: "))
d = "합계"
Sum=a+b+c
print("{}={}".format(d,sum))


#예제2] 리스트의 멤버를 변수처럼 사용
lst =[0,0,0,'합계']
lst[0]=int(input("첫번째 정수를 입력하세요: "))
lst[1]=int(input("두번째 정수를 입력하세요: "))
lst[2]=int(input("세번째 정수를 입력하세요: "))
Sum = lst[0] + lst[1] +lst[2]
print("{} = {}".format(lst[3],Sum))
'''
#list 인덱싱
# :인덱스 값을 이용한 참조
#  
#       lst =[ 1, 2, 3, 4, 5, 6, 7, 8]
# 양의 index:  0  1  2  3  4  5  6  7 
# 음의 index: -8 -7 -6 -5 -4 -3 -2 -1

#예제] list인덱스
lst =[ 1, 2, 3, 4, 5, 6, 7, 8]
# (+)  0  1  2  3  4  5  6  7 
# (-) -8 -7 -6 -5 -4 -3 -2 -1
print("lst[]",lst)
print("lst[-1] : ",lst[-1])
print("lst[-2] : ",lst[-2])
print("lst[-3] : ",lst[-3])

# slicing방식을 이용한 시퀸스 객체(자료) 접근
# slicing이란? 리스트와 같은 시퀸스 자료 값들의 범위로 접근하기 위해서 사용하는 방법으로 
# 시퀸스 자료의 일부를 잘라서 새롭게 생성하는 것을 의미함
# 
# (형식)
#  변수명[시작인덱스:끝인덱스] 
#  변수명[시작인덱스:끝인덱스:증감값]     #range와 유사/ *끝인덱스 이전까지
# 
# 예] lst = [ 1, 2, 3, 4, 5, 6]
#    index    0  1  2  3  4  5     
#     (-)    -6 -5 -4 -3 -2 -1
# 
#   lst[0:3] => [1,2,3], lst[0,3,2] =[1,3] 

#예제4]slicing을 이용한 리스트 함수에 대한 접근
lst =[1,2,3,4,5,6]
print(lst[0:3])         #[1,2,3]
print(lst[0:3:2])       #[1,3]
print(lst[5:0:-3])      #[6,3]

# 인덱스 생략
print(lst[:3])          #시작인덱스 생략 =>[1,2,3]
print(lst[3:])          #종료인덱스 생략 =>[4,5,6]

#슬라이싱 후 새로운 리스트 생성
slc1 = lst[3:6]         #[4,5,6]  #6쓴 이유 = 6이전까지 출력
print(slc1)
slc2 = lst[1:5:3]       #[2,5]
print(slc2)
slc3 = lst[5::-1]       #[6,5,4,3,2,1]  끝값을 생략
print(slc3)
slc4 = lst[-3:-1]       #[4,5]
print(slc4)

# 리스트 함수들... 
#  - append(value) : 리스트 끝에 값을 추가(멤버 추가) 
#  - extend(iter) : 리스트 끝에 list,tuple,dict의 값을 하나씩 추가
#  - insert(idx,value) : idx(인덱스)에 있는 인덱스 위치에 특정값을 추가하는 함수

#  - pop([idx]) : 인덱스를 지정하지 않으면, 마지막 인덱스 값을 반환후 삭제. //반환값=넘겨주는 값
#               인덱스 값을 지정하면, 해당 인덱스 값을 반환 후 삭제

#  - remove(value) : 특정 값을 찾아서 삭제하는 함수 
#  - clear() : 리스트의 모든 멤버를 삭제하고, 빈 리스트로 만드는 함수
#  - count(value) : 리스트 내에 특정 값의 개수를 반환하는 함수
#  - index(value) : 리스트 내에 특정 값의 인덱스 값을 반환하는 함수 
#  - reverse() : 리스트의 멤버의 순서를 뒤집어서 나열하는 함수
#  - sort([reverse=False]) : 리스트의 값을 오름차순(False), 
#                           내림차순(True) 정렬해주는 함수 

# append(): 리스트 끝에 값을 추가(멤버 추가=요소가 된다.)
lst1=[1,2,3,4,5,6,7,8]
lst1.append('a') #문자 'a'
print(lst1)
lst1.append([9,10])     #[1, 2, 3, 4, 5, 6, 7, 8, 'a', [9, 10]]
print(lst1)
print(lst1[-1])         #멤버의 자료형태가 여러개 리스트 멤버의 수는 10개. **마지막 멤버가 [9,10]=1개

#extend(): 리스트 뒤에 추가할 리스트,튜플,딕셔너리 자료<시퀸스 자료형>를 멤버에 개별적 추가/ **하나씩 빼서 넣어준다 멤버 5개 추가됌
lst1=[1,2,3,4,5,6,7,8]
lst1.extend(['a','b','c','d','e'])  #[1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', 'c', 'd', 'e']
print(lst1)

#insert(idx,value) : idx인덱스 위치에 값을 추가 //어느위치에 집어넣을 수 있는지 정할 수 잇음
lst1=[1,2,3,4,5,6,7,8]
lst1.insert(3,'a')  #3번 위치에 있던 것은 뒤로 밀림 ***사라지지 않는당!
print(lst1)

#pop(): 맨뒤에 있는 멤버 반환후 삭제,
#       idx값을 넣으면 해당 인덱스 값을 반환 후 삭제
lst1=[1,2,3,4,5]
a = lst1.pop()          # a = 5, lst=>[1,2,3,4]
print(a)
print(lst1)
b = lst1.pop(2)
print(b)                # b = 3, lst=>[1,2,4]
print(lst1)

#remove(value): value에 있는 내용을 검색 후 삭제 검색시에 없으면 Error를 반환
lst1=[1,2,3,2,5,6,2,8]
lst1.remove(2)          #첫번째 2가 삭제됨.
print(lst1)
lst1.remove(2)          #두번째 2가 삭제됨.
print(lst1)
lst1.remove(2)          #세번째 2가 삭제됨.
print(lst1)
#lst1.remove(2)         #Error <value error not in x>

#clear()
lst1=[1,2,3,4,5]
lst1.clear()
print(lst1)

#count(value) : 특정 값의 개수를 출ㄹ력
lst1=[1,2,3,2,5,6,2,8]
su = lst1.count(2)
print(lst1)
print("2의 값을 가진 멤버의 개수 : ",su)
#su = lst1.count(10)해도 Error 안뜨고 개수가 0이라고 나옴

#index(value) :특정 값의 인덱스 값을 출력
lst1 =[1,2,3,4,5,6]
idx =lst1.index(4)
print("4값의 인덱스 위치값은: ",idx)
# idx =lst1.index(10)                 #value error: 10 is not in list #remove() index() 사용할 때 해당값이 있는지 꼭 확인!
# print("10값의 인덱스 위치값은: ",idx) 

#reverse(): 리스트의 멤버의 순서를 반전(정렬X)//위치만 반전시키는 것
lst1=[9, 10, 3, 2, 6, 1, 7, 8, 4, 5]
print("reverse() 사용전: ",lst1)
lst1.reverse()
print("reverse() 사용후: ",lst1)

#sort() : 리스트를 정렬하는 함수
#       -오름차순(작은 값=>큰 값) => reverse=False(생략)=>기본값//안 쓰면 오름차순 정리함
#       -내림차순(큰 값=>작은 값) => reverse=True
lst1.sort()
print("lst1을 오름차순 정렬:",lst1)
lst1.sort(reverse=True)
print("lst1을 내림차순 정렬:",lst1)

# sort 사용시 주의사항
# 1. 숫자 형식 또는 문자형식은 불리해서 정렬해야 한다. (같이사용해서 정렬X)
#    (숫자는 숫자낄리 문자는 문자끼리...)
# 2. 정수와 실수는 같은 숫자이기 때문에 정렬이 가능함. (정수와 실수는 같이사용해서 정렬O)
# 
# 3. 정렬된 리스트를 새롭게 만들고 싶은 경우, sorted()를 사용 (sorted라는 함수를 사용하면 새로운 리스트를 만듬) 
#    lst2 = sarted(lst1)  #lst1에 있는 것들을 정렬해서 lst2라는 새로운 것을 만듬
#    lst3 = sorted("I am a student".split()) #split()=문자열을 분리함
#       #['I' 'am' 'a' 'student']
#    lst4 = sorted("I am a student".split(),key=str.lower)  key=str.lower >대소문자 구분X 소문자로 취급해서 보겠다
#       #['a','am','I','student']
lst1 = [9, 10, 3, 2, 6, 1, 7, 8, 4, 5]
lst2 = sorted(lst1)  
lst3 = sorted("I am a student".split()) 
print(lst2)
print(lst3)
lst4 = sorted("I am a student".split(),key=str.lower)  
print(lst4)

# **split() 문자열을 분리하는 함수
# :"()" 안에 아무것도 널어주지 않으면, 공백(스페이스,탭,엔터 등)을
# 기준으로 문자열을 나눠서 사용함. 만약 split(';')을 사용하면,';'을 
# 기준으로 문자열을 나누겠다는 의미.