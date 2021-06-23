'''
# 딕셔너리(Dictionary)
# 1. List와 비슷한 자료형. List는 요소(멤버)에 대한 접근시 첨자(Index)를 사용
# 2. 딕셔너리도 첨자를 사용한다. 사용하는 첨자는 "key"를 사용
# 3. 딕셔너리는 key가 가리키는 곳에 값(value-데이터)이 존재함.
#    key값을 사용하는 장점 : 
#           1) 빠른탐색 -탐색속도가 빠름
#           2) 사용하기 편리함.
# 4. 딕셔너리를 정의할 때는 "{}"를 사용함.
# 5. 특정 슬롯을 대해서 참조할 때에 key-value를 입력하거나, 딕셔너리 안에 있는
#    요소를 참조할 경우에 "[]"를 사용한다.
# 
# (형식)
#  변수명 = {}  #비어있는 딕셔너리 선언
#  변수명 = {key1:value1,key2:value2,key3:value3 ...}
# 
#  dict()를 이용해서 선언하는 경우,
#  변수명 = dict([(k1,v1),(k2:v2),(k3,v3),...]) 
# 
#  (접근방식)
#  dic = {key:value}
#  dic[key] = value1
#  print(dic[key])      # value1
dic = {"key":"value"}
print(dic["key"]) 
dic["key"] = "value1"
print(dic["key"]) 

# 예제 1] 딕셔너리에 대한 정의 및 접근방법
dic = {'a':1,'b':2,'c':3}
print(dic['c'])
dic['c'] = 5*dic['b']
print(dic['c'])

# 예제 2] 딕셔너리에 for문을 사용하는 경우
for k in dic:   # 딕셔너리 자료형을 이용한 for문에서는 변수는 "key"값을 저장!!
    print(k)
    print("키값 : {}, 키를 이용한 참조값 : {}".format(k,dic[k]))

# 예제 3] 딕셔너리와 리스트를 같이 사용하는 경우(딕셔너리안에 값을 리스트로 사용)
dl={'음료':['탄산','과일','우유','물'],
    '식사':['김밥','라면','돈까스','비빕밥']}
for key in dl:
    print(dl[key])
    for i in dl[key]:
        print(i,end=' ')
    print()
    for j in range(4):
        print(dl[key][j],end=' ')
    print()

# 예제 4] 리스트 안에 딕셔너리가 있는 경우
ld=[{'name':"홍길동",'age':18,'blood':"A"},
    {'name':"이방원",'age':24,'blood':"B"}]
for dic in ld:
    print(dic['name'],dic['age'],dic['blood'])

# 예제 5] 딕셔너리 안에 딕셔너리가 있는 경우
dd={'홍길동':{'age':18,'blood':"A"},
    '이방원':{'age':24,'blood':"B"}}
for name in dd:
    print(name,dd[name]['age'],dd[name]['blood'])

# 딕셔너리에서 사용하는 함수들
# -update(dict) : 사전형 자료에 값을 추가 (key:value)
# -fromkeys(iter[,value]) :  iter에 리스트, 튜플의 값을 딕셔너리의 키로 사용하는
#                        딕셔너리를 생성하여 반환.
# -get(key[,value]) : 사전형의 키를 사용하여 값을 얻어오는 함수
# -keys() : 사전형자료에서 모든 키를 반환하는 함수
# -values() : 사전형 자료에서 모든 값을 반환하는 함수
# -items() : 사전형의 모든 "키(key):값(value)"의 쌍으로 튜플(*)로 반환
# -pop(key) : 사전형 자료의 키를 통해서 값을 반환한 후에 삭제
# -popitem() : 사전형 자료의 마지막 "키:값" 쌍을 튜플(*)로 반환 후 삭제
# -clear() : 사전형의 모든 "키:값"을 삭제하여 빈 사전형 자료로 만듬. 

# update() 
dic = {'a':1,'b':2,'c':3}
dic.update({'d':4})
print(dic['a'])
print(dic['d'])
print(dic)

# fromkeys(iter,value)
ke = ['a','b','c','d']
dic1 = {}.fromkeys(ke)      # {'a': None, 'b': None, 'c': None, 'd': None}
dic2 = {}.fromkeys(ke,1)    # {'a': 1, 'b': 1, 'c': 1, 'd': 1}
print(dic1)
print(dic2)

# get(key[,value])
dic = {'a':1,'b':2,'c':3}
value = dic.get('b')
print(value)                # 2
print(dic.get('d'))         # None
print(dic.get('d','Not exist key')) # Not exist key
print(dic.get('c','Not exist key')) # 3

# keys()
dic = {'a':1,'b':2,'c':3}
for key in dic.keys():
    print(key,end=' ')
print(type(dic.keys()))
print(dic.keys())
print()

# values()
dic = {'a':1,'b':2,'c':3}
for values in dic.values():
    print(values,end=' ')
print()
print(dic.values())

# items()
dic = {'a':1,'b':2,'c':3}
for key,value in dic.items():   # unpacking
    print("{}:{}".format(key,value),end="\t")
print()

# pop(key)
dic = {'a':1,'b':2,'c':3}
value = dic.pop('b')
print(value)
print(dic)

# popitem()
dic = {'a':1,'b':2,'c':3}
tu1 = dic.popitem()
print(dic)
print(tu1)

# clear()
dic = {'a':1,'b':2,'c':3}
print(dic)
dic.clear()
print(dic)

<<문제>>
1. 이름, 전화번호, 이메일 주소를 키로 사용하는 사전 자료를 생성하시오

2. 리스트형 변수에 1번 문제와 같은 사전 자료가 여러개 생성될 수 있게
  하시오.(입력값을 받아서 자료를 생성)

3. 2번에서 입력한 자료가 출력될 수 있도록 하시오. 
   (출력예시)
   이름 : 홍길동
   전화번호 : 010-xxxx-xxxx
   이메일 : xxxx@xxx.com
'''
# 1
dic = {'이름':"홍길동",'전화번호':"010-xxxx-xxxx",'이메일':"xxxx@xxx.com"}
# 2. 리스트형 변수에 사전자료가 여러개? 
import os
ld = []
while True:
    dic2 = {}
    dic2.update({'이름':input("이름 입력 : ")})
    dic2.update({'전화번호':input("전화번호 입력 : ")})
    dic2.update({'이메일':input("이메일 입력 : ")})
    ld.append(dic2)
    if (input('계속하겠습니까?(Y/n)')=='n'):
        break
    os.system("cls")
    #print(ld)
# 3
for d in ld:
    print("이름 : {}".format(d['이름']))
    print("전화번호 : {}".format(d['전화번호']))
    print("이메일 : {}".format(d['이메일']))
    print()

# <<아래의 내용을 토대로 프로그램을 작성해보세요.>>
# 1. 다음과 같은 메뉴와 가격을 key와 value로 사용하여
# 사전형 자료를 만들어보세요(변수명은 menu)
#  칼국수(6000원), 비빕밥(5500원), 돼지국밥(7000원),
#  돈까스(7000원), 깁밥(2000원), 라면(2500원) 

# 2. 위에서 만든 사전형 자료 menu 변수에서 가격이 6000원 미만에
# 해당하는 메뉴와 가격을 출력하는 코드를 작성하세요. 

# 3. 사용자 입력으로 메뉴와 가격을 입력 받아  menu 변수에 자료를
# 추가 할 수 있도록 하시오.(동일한 메뉴는 가격만 변경)

# 4. 메뉴를 자동으로 선택하여 출력하게 만들어 보세요.   

