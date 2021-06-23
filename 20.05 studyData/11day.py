'''
# Copy 기능
#  -shallow copy: 서로 다른 변수가 같은 위치에 있는 데이터를 가르키는 경우
#  -deep copy: 두개의 변수가 별도의 공간을 가리키는 경우
#  
#  (예)shallow copy - 똑같은 주소위치에 저장. 
lst1 =[1,2,3,4,5]
lst2 =lst1
print("lst1의 값 :",lst1,"lst1의 주소 값: ",id(lst1))
#id()는 변수나 함수의 주소 값을 반환하는 함수
print("lst2의 값 :",lst2,"lst2의 주소 값: ",id(lst2))
lst1[1]='a'
print(lst1)
print(lst2)

# (예) deep copy -데이터에 대한 공간을 별도로 만들어서 복사하는 것/ 같은 공간에 저장 X //각각 개별적 공간에 값을 저장
lst1 = [1,2,3,4,5]
lst2 = list(lst1)
lst1[1] ='a'
print("lst1의 값 : ",lst1,"\tlst1의 주소값: ",id(lst1))
print("lst2의 값 : ",lst2,"\tlst1의 주소값: ",id(lst2))


# 복사기능을 제공하는 copy 모듈을 불러서 사용 가능함.
import copy

lst1=[1,2,3,4,5]
lst2 = copy.deepcopy(lst1)  #deep copy 함수
lst3=lst1
print(lst1,lst2)
print(id(lst1),"\t",id(lst2),"\t",id(lst3))
lst2[0]=100
print(lst1,lst2)

'''
'''
[ Quiz 1 ] : 리스트 초기값 [ 30, 20, 10 ] 설정 후 
아래와 같이 출력 되도록 코드를 작성하세요.

현재 리스트 : [30, 20, 10]
append(40) 후의 리스트 : [30, 20, 10, 40]
pop() 으로 추출한 값 : 40
pop() 후의 리스트 : [30, 20, 10]
sort() 후의 리스트 : [10, 20, 30]
reverse() 후의 리스트 : [30, 20, 10]
'''
'''
lst=[30,20,10]
print("현재 리스트 :{}".format(lst))
lst.append(40)
print("append(40) 후의 리스트 :{} ".format(lst))
print("pop으로 추출한 값 :{}".format(lst.pop()))
print("pop() 후의 리스트 :{}".format(lst))
lst.sort()
print("sort() 후의 리스트 :{}".format(lst))
lst.reverse()
print("reverse() 후의 리스트 :{}".format(lst))
'''
'''
[ Quiz 2 ] : 리스트 초기값 [ 30, 20, 10 ] 설정 후 
아래와 같이 출력 되도록 코드를 작성하세요.

현재 리스트 : [30,20,10]
10 값의 위치 : 2
insert(2,200) 후의 리스트:[30, 20, 200, 10]
remove(200) 후의 리스트:[30,20,10]
extend ([555,666,555])후의 리스트:[30,20,10,555,666,555]
555 값의 개수: 2
'''
'''
lst=[30,20,10]
print("10 값의 위치: {}".format(lst.index(10)))
lst.insert(2,200)
print("insert(2,200) 후의 리스트:{}".format(lst))
lst.remove(200)
print("remove(200) 후의 리스트:{}".format(lst))
lst.extend([555,666,555])
print("extend ([555,666,555])후의 리스트:{}".format(lst))
print("555 값의 개수: {}".format(lst.count(555)))

#  2차(원) 리스트  ---이중 for문
#  : 리스트 안에 멤버 중에 리스트가 존재하는 경우 사용되는 방식
#   리스트 안에 있는 리스트 멤버에 대한 참조 방식

# 예제 1] 2차 리스트 변수 값 참조 
aa=[[1,2,3,4],      #aa[0]
    [5,6,7,8],      #aa[1]
    [9,10,11,12]]   #aa[2]
    # aa 리스트 멤버의 갯수 : 3개 =>[1,2,3,4],[5,6,7,8],[9,10,11,12]  
print(aa)
for x in range(3):  #aa 리스트의 멤버 수
    for y in range(4):   #aa멤버 리스트의 멤버 갯수 =>"4"=>len(aa[x])       #길이 값이 제각각일 때는 len()함수 쓰기
        print(aa[x][y],end="\t")
    print()

#리스트 자체가 하나의 멤버로 저장됌 #리스트 초기화시킬때 clear 사용X 왜냐하면 clear는 공간 자체가 날아가버림
#공간 자체가 날아가지 않고 안에 있는 값만 비워놓는 것// 비어 있는 초기상태로 돌려놓은 상태로 반복하게 됌
# 예제 2] 2차원 리스트 생성 및 출력
ls_1=[];ls_2=[];value=1
for i in range(3):
    for j in range(4):          
        ls_1.append(value)      #i=0, ls_2=[[1,2,3,4]]
                                #i=1, ls_2=[[1,2,3,4],[5,6,7,8]]
        value += 1              #i=2, ls_2=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    ls_2.append(ls_1)
    ls_1=[]                     #ls_1 초기화
print(ls_2)
print(aa)
for x in range(3):  #aa 리스트의 멤버 수
    for y in range(4):   #aa멤버 리스트의 멤버 갯수 =>"4"=>len(aa[x])       #길이 값이 제각각일 때는 len()함수 쓰기
        print(ls_2[x][y],end="\t")
    print()
'''
# 문제 1] numbers = [10, 20, 30, 40, 50, 60, 70]
# 위 리스트의 모든 값을 더한 결과를출력하시오.
Sum=0
aa = [10, 20, 30, 40, 50, 60, 70]
for x in range(7):
    Sum+=int(aa[x])
print(Sum)  

#풀이
Sum=0
numbers = [10, 20, 30, 40, 50, 60, 70]
for x in numbers:
    Sum +=x
print(Sum)
'''
# 문제 2]1 ~ 45 까지 임의의 값을 중복 없이 6개 생성하여 출력하는 코드를작성하시오
from random import random
lst=[a,b,c,d,e,f]
for x in range(6):
    su=int(random()*45)+1
    su=lst
    if a!=b and b!=c and c!=d and d!=e and e!=f :
        print(lst)
'''       
#풀이
from random import random
lotto=[]
cnt=0 #출력 개수
while True:
    rand = int(random()*45)+1
    if rand not in lotto:
        lotto.append(rand)
        cnt +=1
        if cnt ==6:
            break
lotto.sort()
print(lotto)
'''
from random import random
a,b,c,d,e,f=0,0,0,0,0,0
while True:
    su=int(random()*45)+1
    su=a
    break
while True:
    su=int(random()*45)+1
    if a!=b:
        su=b
        break
while True:
    su=int(random()*45)+1
    if a!=b and b!=c:
        su=c
        break
while True:
    su=int(random()*45)+1
    if a!=b and b!=c and c!=d:
        su=d
        break
while True:
    su=int(random()*45)+1
    if a!=b and b!=c and c!=d and d!=e :
        su=e
        break
while True:
    su=int(random()*45)+1
    if a!=b and b!=c and c!=d and d!=e and e!=f :
        su=f
        break
print(a,b,c,d,e,f,sep="/")

# 문제 3]lst_sec= [['홍길동', '남', 36], ['김수양', '여', 32], ['박담소', '남', 28]]
# 위의2차리스트자료를다음과같은형식으로출력하시오.
# 이름: 홍길동
# 성별: 남
# 나이: 36
lst_sec= [['홍길동', '남', 36], ['김수양', '여', 32], ['박담소', '남', 28]]
for i  in range(3):
    for j in range(3):
print("이름 : {}\n 성별: {}\n 나이: {}".format(lst_sec[0][0],lst_sec[0][1],lst_sec[0][2]))
'''
#풀이
lst_sec = [['홍길동', '남', 36], ['김수양', '여', 32], ['박담소', '남', 28]]
for i in range(len(lst_sec)):
    for j in range(1):
        print("이름:{}".format(lst_sec[i][j]))
        j+=1
        print("성별:{}".format(lst_sec[i][j]))
        j+=1
        print("나이:{}".format(lst_sec[i][j]))
    print()
#or
for val in lst_sec:
    print("이름:{}".format(val[0]))
    print("성별:{}".format(val[1]))
    print("나이:{}".format(val[2]))

# 문제 4]구구단을 출력하는 코드를 작성하되, 2차리스트에 결과 값을 저장하고 출력 할 수 있도록하시오. (리스트를 참조해서 불러라)
# 풀이
gugu = []
for x in range(2,10):
    gugu.append([])     #gugu리스트에 비어있는 리스트를 추가
    for y in range(1,10):
        gugu[x-2].append(x*y)
print(gugu)
for x in range(2,10):
    for y in range(1,10):
        print("{} x {}= {:<3}".format(x,y,gugu[x-2][y-1]),end ="")

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
name=[]
print("-"*30)
print("1.친구 리스트 출력")
print("2.친구 추가")
print("3.친구 삭제")
print("4.이름 변경")
print("0.종료")
num=int(input("메뉴를 입력하세요 : "))
if num==1:
    print("#등록한 친구 목록 보기")
    print(name)
elif num==2:
    print("#친구 등록하기(정보는 문제3번 참조)")
    user=input("이름을 입력하세요 : ")
    append.name([user])
    print(name)
elif num==3:
    print("#등록 친구 삭제")
    user=input("이름을 입력하세요 : ")
    remove.name([user])
    print(name)
elif num==4:
    print("#이름 변경")
    index.name([user])
elif num==0:
    print("#프로그램 종료")
print("-"*30)

