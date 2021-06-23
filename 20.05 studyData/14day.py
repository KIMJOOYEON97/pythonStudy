'''
# <<아래의 내용을 토대로 프로그램을 작성해보세요.>>
# 1. 다음과 같은 메뉴와 가격을 key와 value로 사용하여
# 사전형 자료를 만들어보세요(변수명은 menu)
#  칼국수(6000원), 비빕밥(5500원), 돼지국밥(7000원),
#  돈까스(7000원), 깁밥(2000원), 라면(2500원) 
menu={'칼국수':6000,'비빔밥':5500,'돼지국밥':7000,'돈까스':7000,'김밥':2000,'라면':2500}

# 2. 위에서 만든 사전형 자료 menu 변수에서 가격이 6000원 미만에
# 해당하는 메뉴와 가격을 출력하는 코드를 작성하세요. 
for me in menu: #키값이 변수 me에 저장
    if menu[me] <6000:
        print("{}:{}원".format(me,menu[me]))

# 3. 사용자 입력으로 메뉴와 가격을 입력 받아  menu 변수에 자료를
# 추가 할 수 있도록 하시오.(동일한 메뉴는 가격만 변경)
add_menu=input("메뉴를 입력하세요: ")
add_value = int(input("메뉴 가격을 입려가세요 : "))
if add_menu in menu:   #추가하고자 하는 메뉴가 메뉴에 있는지 확인. #특정 위치에 있는지 없는 지 확인!!!!=>멤버연산자
    menu[add_menu] = add_value  #첨자를 이용한 딕셔너리 접근
else:
    menu.update({add_menu:add_value})
print(menu)

# 4. 메뉴를 자동으로 선택하여 출력하게 만들어 보세요.   =>화면에 출력하는 것이 기본값/출력 안하는 것이 선택
sel=input("메뉴를 출력하겠습니까?(Y/n)")
if sel =='Y' or sel !='n':  #sel !='n' 중요함
    for me in menu:
        print(me,menu[me],'원')
    print()
'''
# python의 문자열 =>얘도 시퀸스 자료형이라 인덱싱 사용가능
# : 파이썬에서 사용하는 문자열 처리
# 
# (특징)
# (1) 인덱싱을 이용한 참조 가능
st='python string'
#   0123456789...(index값)
print(st[0])    #'p'
print(st[7])    #'s'
# (2) 슬라이싱을 이용한 참조  cf)사전형은 인덱스번호가 없어서 슬라이싱이 안되었음
print(st[:6])   #python   #시작과 끝 인덱스 생략 가능
print(st[7:])   #string
# (3) 문자열의 반복문(for)
st='python string for'
for x in st:            #문자열도 sequencr자료형이다.
    print(x,end=" ")    #p y t h o n   s t r i n g   f o r  #공백도 문자열.
print()

# 문자열 함수
# -find(str) : 문자열에서 특정 문자열을 찾아서 해당 문자의 index값을 반환
# -count(str) : 문자열에서 특정 문자열을 찾아서 해당 문자열의 수를 반환
# -lower() : 문자열에서 영문 대문자를 소문자로 변경하여 반환 #반환=자체를 바꾸는 것이 아니다. cf)리스트 sort()같은 것들은 자체를 바꿈
# -upper() : 문자열에서 영문 소문자를 대문자로 변경하여 반환
# -strip() : 문자열에서 양쪽 공백 또는 문자를 제거 반환
# -lstrip() : 문자열에서 왼쪽 공백 또는 문자를 제거 반환
# -rstrip() : 문자열에서 오른쪽 공백 똔느 문자를 제거 반환 
# -replace(old,new) : 문자열에서 왼쪽(old)문자열을 찾아 오른쪽(new)문자열로 변경
# -split(str) : 문자열을 특정 문자를 기준으로 분리 =>분리된 내용을 리스트
 
# find 예제 =>인덱스 값 반환
st='python string'
#(+)012345678
print(st.find('string'))  #7 type(7) =>int
# find(str,시작인덱스,끝인덱스)
print(st.find('t'))      #2     #첫번째 t만 찾음 
print(st.find('t',3))    #8 
                      #앞에서 찾은 것 +1값의 위치에서 찾으면 두번째 t찾을 수 있음
#전체 문장열에서 내가 원하는 단어를 찾을 때 =>첫번째, 두번째 = 시작인덱스값 조정, 세번째 = 시작인덱스값 찾아가야함.
#find()가 값을 찾지 못한 경우 반환값 : -1
print(st.find('a'))     #-1  #찾는 것이 끝난 것을 반환값 -1로 확인함

# count()   
st='python string'
print(st.count('t'))    #2
# count(str,시작인덱스,끝인덱스)    #find랑 비슷함
print(st.count('t',6))  #1
# count()가 값을 찾지 못한 경우 반환값 : 0  #Error 안뜬다 // 타입에러뜨는 것들 정리하고 알아두기!

#lower()
st='PYTHON STRING'
print(st.lower())   #python string
print(st)           #PYTHON STRING
st = st.lower()     #원래 있던 변수에 있는 값을 바꿔주는 것이 아니라, 바뀌어진 것을 넘겨줌
print(st)           #python string

#upper()
st='python string'
st2=st.upper()
print(st2)          #PYTHON STRING

# strip() : 양쪽에 인자로 전달 받은 문자열을 제거   *()소괄호 안에 들어가는 값이 인자
#           인자값이 없는 경우, 공백을 제거
st='     python string     '
print("[{}]".format(st))    #[     python string     ]
st1=st.strip()              #.format도 문자열 함수 이다.
print("[{}]".format(st1))   #[python string]

# lstrip()
st2 =st.lstrip()
print("[{}]".format(st2))   #[python string     ]


# rstrip()
st3 =st.rstrip()
print("[{}]".format(st3))   #[     python string]

# replace(old,new)  #old =>찾을 문자 new=>바꿀 문자
st = 'python string'
st1 = st.replace('string','문자열')
print(st1)          #python string => python 문자열

# split(str) 문자열을 str에 있는 문자를 기준으로 분리 => 리스트로 저장
st='python string'      
st1 = st.split()        #st1 = list #공백을 기준으로 분리 =>space tap enter
print(st1)      #['python','string']

'''
# split()을 이용한 입력문자 값 분리 #입력문자도 문자열이다. 
values = input("입력 : ").split()  #unpacking해서 넘긴다 #=> 입력 :I am a student
print(values,type(values))      #['I', 'am', 'a', 'student'] <class 'list'>
'''

#예제1. 결합 및 연산
A = 'Have a'
print(A)
B = " Nice Day"
C = A+B      #병합
print(C)     #'Have a' + 'Nice Day'
print(C*3)   #Have a Nice DayHave a Nice DayHave a Nice Day
A += 'Nice Day!!'   #확장
print(A)    #Have a Nice Day!!

#예제2
str1 ='Python is Easy. Programmming 괜찮죠?...그죠?..아니예요??ㅡㅡ;;'
print(str1)             #Python is Easy. Programmming 괜찮죠?...그죠?..아니예요??ㅡㅡ;;
print(str1.upper())     #PYTHON IS EASY. PROGRAMMMING 괜찮죠?...그죠?..아니예요??ㅡㅡ;;
print(str1.lower())     #python is easy. programmming 괜찮죠?...그죠?..아니예요??ㅡㅡ;;
# swapcase() : 영문 대소문자를 변경. 대문자 => 소문자, 소문자 => 대문자
print(str1.swapcase())  #pYTHON IS eASY. pROGRAMMMING 괜찮죠?...그죠?..아니예요??ㅡㅡ;;
str2 =str1.lower()   #str2 소문자로 전부 바뀜
#str2를 단어의 첫글자를 대문자로 만드는 법 
#1)upper(첫글자 인덱스값)
#2)title()
# title() : 영문 단어의 시작을 대문자로 변경
print(str2.title())     #Python Is Easy. Programmming 괜찮죠?...그죠?..아니예요??ㅡㅡ;;

# 문제1. 1)아래의 문장 주어진 조건에 맞게 변경
# "NevEr-eVer 100gIVe Up" [변경전]
# "Never-Ever 100Give Up" [변경후]
st="NevEr-eVer 100gIVe Up"
st1=st.lower()
st2=st1.title()
print(st2)
#풀이
st="NevEr-eVer 100gIVe Up"
st1=st.title()      #단어 시작은 대문자로 나머지는 소문자로.***캐치하지 못한 부분
print(st1)

# 2)Have a nice day 문자열에서 다음 알아오기 
# 'a', 'day', 'dak'의 갯수 알아오기
h = "Have a nice day"
print(h.count('a'))     #3
print(h.count('day'))   #1
print(h.count('dark'))  #0
#풀이
st2 = "Have a nice day"
print("a의 개수: ",st2.count('a'))
print("day의 개수: ",st2.count('day'))
print("dark의 개수: ",st2.count('dark'))    #**count는 error가 안 뜬다!!

# 문제2. "It is a fun python class" 문자열의 길이, #문자열도 시퀸스 자료형이기 때문에 리스트로 변환할 필요X
# 문자 'a'의 개수, 's'의 개수를 출력하는 코딩 (함수 쓰지마세요... )
i=0;ac=0;sc=0               #*
for x in "It is a fun python class":
    if x=='a':
        ac+=1
    if x=='s':
        sc+=1
    i+=1
print("문자열의 길이 : {}".format(i))       #24
print("문자 'a'의 개수 : {}".format(ac))    #2
print("문자 's'의 개수 : {}".format(sc))    #3
#풀이
str2 = "It is a fun python class"
cnt = cnt_a =cnt_s = 0      #변수3개를 0으로 초기화*
for i in str2:
    cnt += 1    #문자열의 길이
    if i =='a':
        cnt_a += 1
    elif i =='s':     #if elif 둘다 가능
        cnt_s += 1
print("문자열의 길이 : ",cnt)
print("문자 'a\'의 개수 : ",cnt_a)
print("문자 \'s\'의 개수 : ",cnt_s)
#함수 사용시
print("문자열의 길이 : ",len(str2))
print("문자 \'a\'의 개수 : ",str2.count('a'))
print("문자 \'s\'의 개수 : ",str2.count('s'))

# 문제3. "Have a nice day" 문자열을 가지고 다음을 처리하세요.
#  1)각각 find와 index를 사용하여 "day"문자의 위치를 찾으세요.
print(h.find('day')) #12
print(h[12:]) #day
#풀이
str3 = "Have a nice day"     #find()=에러x// index()=에러o 차이는 값이 없을 때 나오는 차이
print("find('day'): ",str3.find('day'))
print("find('day'): ",str3.index('day'))
print("find('day'): ",str3.find('kkk'))
#print("find('day'): ",str3.index('kkk')) #ValueError

#  2)각각 find와 index를 사용하여 "kkk"문자의 위치를 찾으세요.
print(h.find('kkk')) #-1

#  3)find를 사용하여 첫번째, 두번째, 세번째, 네번째 'a'의 위치를 
#   출력하세요.
print(h.find('a'))      #1
print(h.find('a',2))    #5
print(h.find('a',6))    #13
#풀이
idx = str3.find('a')
print("find : 첫번째 a의 위치 : ",idx)
idx = str3.find('a',idx+1)              #while구문 사용가능!
print("find : 두번째 a의 위치 : ",idx)
idx = str3.find('a',idx+1)
print("find : 세번째 a의 위치 : ",idx)
idx = str3.find('a',idx+1)
print("find : 네번째 a의 위치 : ",idx)  # -1 =>즉, 없다는 얘기

#[ Quiz ] : List 정의하여 첨자 위치 저장
# a의 총 개수와 첨자의 위치를 출력 하시오
# st = 'Have a nice day Have a nice day Have a nice day'
#  
#결과 
#a 개수 : 9
#첨자 : [1, 5, 13, 17, 21, 29, 33, 37, 45]
idx=0
lst=[]
st='Have a nice day Have a nice day Have a nice day'
while True:         #무한루프 식에서 빠져나오지 못하면 출력이 안됌
    idx =st.find('a',idx)
    if idx != -1:
        lst.append(idx)
        idx+=1
    if idx ==-1:
        break    
cnt=st.count('a')
print("a 개수: ",cnt)
print("첨자 : ",lst)
#풀이
st = 'Have a nice day Have a nice day Have a nice day'
lst=[]
idx=0
while True:
    idx = st.find('a',idx)
    if idx !=-1:
        lst.append(idx)
        idx+=1  #idx 찾은 값을 +1해준다
    else:
        break       #-1이라면 나가면 된다.
print("a개수 : ",st.count('a'))
print("첨자 : ",lst)