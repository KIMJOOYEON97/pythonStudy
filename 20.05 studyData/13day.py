# 딕셔너리(Dictionary)
# 1. list와 비슷한 자료형. list는 요소(멤버)에 대한 젒근시 첨자(Index)를 사용
# 2. 딕셔너리도 첨자를 사용한다. 사용하는 첨자는 "key"를 사용
# 3. 딕셔너리는 key가 가르키는 곳에 값(value-데이터)이 존재함.
#    key값을 사용하는 장점: 
#               1)빠른 탐색 - 탐색속도가 빠름
#               2)사용하기 편리함.
# 4. 딕셔너리를 정의할 때는 "{}"를 사용함.
# 5. 특정 슬롯을 대해서 참조할 때에  key-value를 입력하거나, 
#    딕셔너리 안에 있는 요소를 참조할 경우에 "[]"를 사용한다. 
# 
# (형식)
#  변수명 ={} #비어있는 딕셔너리 선언
#  변수명  ={key1:value1,key2:value2,key3:value3}      #value는 어떤 자료형이 와도 ok
#  
#  dict()를 이용해서 선언하는 경우,
#  변수명 = dict([(k1,v1),(k2,v2),(k3,v3),....]) 튜플형태로 묶어줌
# 
# (접근방식)
# dic = {key:value}
# dic[key]=value1
# print(dic[key])       #value1
dic = {"key":"value"}
print(dic["key"]) 
dic["key"] = "value1"
print(dic["key"]) 

# 예제1] 딕셔너리에 대한 정의 및 접근방법       #숫자(index)가 아니라 key값을 가지고 첨자 판단
dic = {'a':1,'b':2,'c':3}
print(dic['c'])
dic['c']=5*dic['b']
print(dic['c'])

#예제2] 딕셔너리에 for문을 사용하는 경우
for k in dic:   #딕셔너리 자료형을 이용한 for문에서는 변수는 "key"값을 저장!!
    print(k)
    print("키값: {}, 키를 이용한 참조값: {}".format(k,dic[k]))

#예제3] 딕셔너리와 리스트를 같이 사용하는 경우(딕셔너리안에 값을 리스트로 사용)
dl = {'음료':['탄산','과일','우유','물'],
      '식사':['김밥','라면','돈까스','비빔밥']}
for key in dl:
    print(dl[key])
    for i in dl[key]:  #리스트이다.
        print(i,end=" ")
    print()
    for j in range(4):
        print(dl[key][j],end=' ') #리스트이 첨자를 이용
    print()

#예제4] 리스트 안에 딕셔너리가 있는 경우   리스트 안에 있는 딕셔너리를 키와 밸류를 이용해서 참조한 것
ld=[{'name':"홍길동",'age':18,'blood':"A"},
    {'name':"이방원",'age':24,'blood':"B"}]
for dic in ld:
    print(dic['name'],dic['age'],dic['blood'])

#예제5] 딕션너리 안에 딕셔너리가 있는 경우 #이차리스트와 비슷
dd={'홍길동':{'age':18,'blood':"A"},
    '이방원':{'age':24,'blood':"B"}}
for name in dd:
    print(name,dd[name]['age'],dd[name]['blood'])

# 딕셔너리에서 사용하는 함수들 
# -update(dict): 사전형 자료에 값을 추가 (key:value) /dict-딕셔너리 형태의 데이터
# -fromkeys(iter[,value]): iter에 리스트, 튜플의 값을 딕셔너리의 키로 사용하는              #키값만 가져와서 딕셔너리를 만듬
#                       딕셔너리를 생성하여 반환   []의미 - 만들어도 되고 안 만들어도 돼고
# -get(key[,value]): 사전형의 키를 사용하여 값을 얻어오는 함수
# -keys(): 사전형자료에서 모든 키를 반환하는 함수
# -values(): 사전형자료에서 모든 값을 반환하는 함수
# -items(): 사전형의 모든 "키(key):값(value)"의 쌍으로 튜플(*중요*)로 반환  
                                # dict()를 이용해서 선언하는 경우,
                                #  변수명 = dict([(k1,v1),(k2,v2),(k3,v3),....]) 튜플형태로 묶어줌
# -pop(key): 사전형 자료의 키를 통해서 값을 반환한 후에 삭제  #키값이 반드시 있어야한다.
# -popitem(): 사전형 자료의 마지막 "키:값" 쌍을 튜플(*중요*)로 반환후 삭제 #pop()과 items()를 섞은 형태
# -clear(): 사전형의 모든 "키:값"을 삭제하여 빈 사전형 자료로 만듬.

# update()    리스트 append와 유사
dic = {'a':1,'b':2,'c':3}
dic.update({'d':4})
print(dic['a'])
print(dic['d'])
print(dic)

# fromkeys(iter,value)
ke =['a','b','c','d']#키값으로 사용될 리스트
dic1={}.fromkeys(ke)    #{'a': None, 'b': None, 'c': None, 'd': None} 키만 가지고 있는 딕셔너리 선언
dic2={}.fromkeys(ke,1)  #{'a': 1, 'b': 1, 'c': 1, 'd': 1} 숫자값을 가지고 있는 딕셔너리
print(dic1)
print(dic2)

#get(ket[,value])
dic = {'a':1,'b':2,'c':3}
value = dic.get('b')
print(value)            # 2
print(dic.get('d'))     # None 
print(dic.get('d','Not exist key'))     # Not exist key 없으면 value에 입력한 것을 반환
print(dic.get('c','Not exist key'))     # 3 키값이 있으면 키값에 해당하는 것을 반환
print(dic) #{'a': 1, 'b': 2, 'c': 3}

#keys() -키값만 뺄때
dic = {'a':1,'b':2,'c':3}
for key in dic.keys():
    print(key,end=' ')
print(type(dic.keys()))     # a b c <class 'dict_keys'> 'dict_keys':딕셔너리 내에 있는 것, 리스트랑 비슷함
print(dic.keys())           # dict_keys(['a', 'b', 'c']) 리스트라면 값이 하나씩 들어감

#values()  - 밸류값만 뺄때
dic = {'a':1,'b':2,'c':3}
for values in dic.values():
    print(values,end=' ')
print()
print(dic.values())         # dict_values([1, 2, 3])

#items()
dic = {'a':1,'b':2,'c':3}
for key,value in dic.items():      #unpacking key,value=a,1
    print("{}:{}".format(key,value),end="\t")
print()

#pop(key)  key값이 반드시 들어가야함
dic = {'a':1,'b':2,'c':3}
value = dic.pop('b')
print(value)
print(dic)
#value = dic.pop() #키값을 받지 못했어요 = pop expected at least 1 arguments

#popitem()
dic = {'a':1,'b':2,'c':3}
tu1 = dic.popitem()
print(dic)  #{'a': 1, 'b': 2}
print(tu1)  #('c', 3)튜플형태로 반환

#clear()
dic = {'a':1,'b':2,'c':3}
print(dic)
dic.clear()
print(dic)

#1.이름, 전화번호, 이메일주소를
# 키로사용하는사전자료를생성하시오. (while 사용해서 계속 입력 받기)
#2.리스트형 변수에 1번문제와 같은 사전자료가 여러 개 생성될 수 있도록 하시오.
#3.2번에서 입력한 자료가 출력될 수 있도록하시오.
'''
ke='이름','전화번호','이메일주소'
user={}.fromkeys(ke)
n=input("이름을 입력하세요: ")
c=input("전화번호를 입력하세요: ")
e=input("이메일주소를  입력하세요: ")
for x in range(len(ke)):
    print(ke,n)
    print(ke,c)
    print(ke,e)
'''
'''
#풀이
#1
dic ={'이름': "홍길동","전화번호":"010-xxxx-xxxx","이메일":"xxxx@xxxx.com"}
#2. 리스트형 변수에 사전자료가 여러개? =>리스트 안에 딕셔너리가 있는 경우
import os
ld=[]
while True:
    dic2={}
    dic2.update({'이름':input("이름 입력 : ")})
    dic2.update({'전화번호':input("전화번호 입력 : ")})
    dic2.update({'이메일':input("이메일 입력 : ")})
    ld.append(dic2)
    if(input('계속하겠습니까?(Y/N)'))=="N":
        break
    os.system("cls")   #위로가나 밑으로 가나 상관 없음
    #print(ld)    
#3
for d in ld:        #딕셔너리형 데이터
    print("이름: {}".format(d['이름']))
    print("전화번호: {}".format(d['전화번호']))
    print("이메일: {}".format(d['이메일']))
    print()
'''
# <<아래의 내용을 토대로 프로그램을 작성해보세요.>>
# 1. 다음과 같은 메뉴와 가격을 key와 value로 사용하여
# 사전형 자료를 만들어보세요(변수명은 menu)
#  칼국수(6000원), 비빕밥(5500원), 돼지국밥(7000원),
#  돈까스(7000원), 깁밥(2000원), 라면(2500원) 
menu={'칼국수':6000,'비빔밥':5500,'돼지국밥':7000,'돈까스':7000,'김밥':2000,'라면':2500}

# 2. 위에서 만든 사전형 자료 menu 변수에서 가격이 6000원 미만에
# 해당하는 메뉴와 가격을 출력하는 코드를 작성하세요. 
for key,value in menu.items():
    if value < 6000:
        print(key,value)

# 3. 사용자 입력으로 메뉴와 가격을 입력 받아  menu 변수에 자료를
# 추가 할 수 있도록 하시오.(동일한 메뉴는 가격만 변경)
while True:
    menu={'칼국수':6000,'비빔밥':5500,'돼지국밥':7000,'돈까스':7000,'김밥':2000,'라면':2500}
    me=input("메뉴를 입력하세요: ")
    p=int(input("가격을 입력하세요: "))
    menu.update({me:p})
    print(menu)
    a=input("추가를 그만하시겠습니까?(y/n)")
    if a=='n':
        break


# 4. 메뉴를 자동으로 선택하여 출력하게 만들어 보세요.   
from random import random

