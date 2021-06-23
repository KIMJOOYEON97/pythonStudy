'''
# <<아래의 내용을 토대로 프로그램을 작성해보세요.>>
# 1. 다음과 같은 메뉴와 가격을 key와 value로 사용하여
# 사전형 자료를 만들어보세요(변수명은 menu)
#  칼국수(6000원), 비빕밥(5500원), 돼지국밥(7000원),
#  돈까스(7000원), 깁밥(2000원), 라면(2500원) 
menu = {'칼국수':6000, '비빕밥':5500,'돼지국밥':7000,'돈까스':7000,
'김밥':2000,'라면':2500}

# 2. 위에서 만든 사전형 자료 menu 변수에서 가격이 6000원 미만에
# 해당하는 메뉴와 가격을 출력하는 코드를 작성하세요. 
for me in menu: #키값이 변수 me에 저장
    if menu[me] < 6000:
        print("{}:{}원".format(me,menu[me]))

# 3. 사용자 입력으로 메뉴와 가격을 입력 받아  menu 변수에 자료를
# 추가 할 수 있도록 하시오.(동일한 메뉴는 가격만 변경)
add_menu = input("메뉴를 입력하세요 : ")
add_value = int(input("메뉴 가격을 입력하세요 : "))
if add_menu in menu:
    menu[add_menu] = add_value
else:
    menu.update({add_menu:add_value})

# 4. 메뉴를 자동으로 선택하여 출력하게 만들어 보세요.   
sel = input("메뉴를 출력하겠습니까?(Y/n) ")
if sel=='Y' or sel !='n':
    for me in menu:
        print(me,menu[me],'원')
    print()

# python의 문자열
# : 파이썬에서 사용하는 문자열 처리 
# 
# (특징)
# (1) 인덱싱을 이용한 참조 가능
st= 'python string'
#    0123456789... (index값)
print(st[0])    # 'p'
print(st[7])    # 's'
# (2) 슬라이싱을 이용한 참조
print(st[:6])   # 'python'
print(st[7:])   # 'string'
# (3) 문자열의 반복문(for)
st = 'python string for'
for x in st:
    print(x,end=' ')    # p y t h o n   s t r i n g   f o r
print()

# 문자열 함수 
# -find(str) : 문자열에서 특정 문자열을 찾아서 해당 문자의 index값을 반환
# -count(str) : 문자열에서 특정 문자열을 찾아서 해당 문자열의 수를 반환
# -lower() : 문자열에서 영문 대문자를 소문자로 변경하여 반환
# -upper() : 문자열에서 영문 소문자를 대문자로 변경하여 반환
# -strip() : 문자열에서 양쪽 공백 또는 문자를 제거 반환
# -lstrip() : 문자열에서 왼쪽 공백 또는 문자를 제거 반환
# -rstrip() : 문자열에서 오른쪽 공백 또는 문자를 제거 반환
# -replace(old,new) : 문자열에서 왼쪽(old) 문자열을 찾아, 오른쪽(new)문자열로
#                 변경
# -split(str) : 문자열을 특정 문자를 기준으로 분리 => 분리된 내용을 리스트로..    

# find 예제
st = 'python string'
# (+) 0123456789... 
print(st.find('string'))    # 7
# find(str,시작인덱스,끝인덱스)
print(st.find('t'))         # 2
print(st.find('t',3))       # 8
# find()가 값을 찾지 못한 경우 반환값 : -1
print(st.find('a'))         # -1

# count() 
st = 'python string'
print(st.count('t'))    # 2
# count(str,시작인덱스,끝인덱스)
print(st.count('t',6))  # 1

# lower()
st = 'PYTHON STRING'
print(st.lower())
st1 = st.lower()
print(st1)

# upper()
st = 'python string'
st2 = st.upper()
print(st2)

# strip() : 양쪽에 인자로 전달 받은 문자열을 제거.
#         인자값이 없는 경우, 공백을 제거
st = '     python string     '
print("[{}]".format(st))
st1 = st.strip()
print("[{}]".format(st1))

# lstrip() 
st2 = st.lstrip()
print("[{}]".format(st2))

# rstrip()
st3 = st.rstrip()
print("[{}]".format(st3))

# replace(old,new) 
st = 'python string'
st1 = st.replace('string','문자열')
print(st1)              # python string => python 문자열

# split(str) 문자열을 str에 있는 문자를 기준으로 분리 => 리스트로 저장
st = 'python string'
st1 = st.split()    # 공백을 기준으로... 
print(st1)          # ['python','string']

# split()을 이용한 입력문자 값 분리
values = input("입력 : ").split()  # => 입력 : I am a student
print(values,type(values))

# 예제1. 결합 및 연산
A = 'Have a'
print(A)
B = ' Nice Day!'
C = A + B       # 'Have a' + ' Nice Day!'
print(C)        # Have a Nice Day!
print(C*3)
A += ' Nice Day!!!' #확장
print(A)

# 예제2 
str1 = 'Python is Easy. Programming 괜찮죠?.. 그죠?.. 아니예요?? ㅡㅡ;;'
print(str1)
print(str1.upper())
print(str1.lower())
# swapcase() : 영문 대소문자를 변경. 대문자 => 소문자, 소문자 => 대문자
print(str1.swapcase())
str2 = str1.lower()
# title() : 영문 단어의 시작을 대문자로 변경
print(str2.title())
'''
# 문제1. 1)아래의 문장 주어진 조건에 맞게 변경
# "NevEr-eVer 100gIVe Up" [변경전]
# "Never-Ever 100Give Up" [변경후]
st = "NevEr-eVer 100gIVe Up"
st1 = st.title()    # 단어 사작은 대문자로 나머지는 소문자로 변경
print(st1)

# 2)Have a nice day 문자열에서 다음 알아오기 
# 'a', 'day', 'dak'의 갯수 알아오기
st2 = "Have a nic day"
print("a의 개수 : ",st2.count('a'))
print("day의 개수 : ",st2.count('day'))
print("dak의 개수 : ",st2.count('dak'))
# 문제2. "It is a fun python class" 문자열의 길이,
# 문자 'a'의 개수, 's'의 개수를 출력하는 코딩 (함수 쓰지마세요... )
str2 = "It is a fun python class"
cnt = cnt_a = cnt_s = 0
for i in str2:
    cnt += 1  # 문자열의 길이
    if i == 'a':
        cnt_a += 1
    elif i == 's':
        cnt_s += 1
print("문자열의 길이 : ",cnt)
print("문자열에 \'a\'의 개수 : ",cnt_a)
print("문자열에 \'s\'의 개수 : ",cnt_s)
#함수 사용시
print("문자열의 길이 : ",len(str2))
print("문자열에 \'a\'의 개수 : ",str2.count('a'))
print("문자열에 \'s\'의 개수 : ",str2.count('s'))

# 문제3. "Have a nice day" 문자열을 가지고 다음을 처리하세요.
#  1)각각 find와 index를 사용하여 "day"문자의 위치를 찾으세요.
#  2)각각 find와 index를 사용하여 "kkk"문자의 위치를 찾으세요. 
#  3)find를 사용하여 첫번째, 두번째, 세번째, 네번째 'a'의 위치를 
#   출력하세요.
str3 = "Have a nice day"
print("find(\'day\') : ",str3.find('day'))
print("index(\'day\') : ",str3.index('day'))
print("find(\'kkk\') : ",str3.find('kkk'))
#print("index(\'kkk\') : ",str3.index('kkk'))  # ValueError
idx = str3.find('a')
print("find : 첫번째 a의 위치 : ",idx)
idx = str3.find('a',idx+1)
print("find : 두번째 a의 위치 : ",idx)
idx = str3.find('a',idx+1)
print("find : 세번째 a의 위치 : ",idx)
idx = str3.find('a',idx+1)
print("find : 네번째 a의 위치 : ",idx)

#[ Quiz ] : List 정의하여 첨자 위치 저장
# a의 총 개수와 첨자의 위치를 출력 하시오
# st = 'Have a nice day Have a nice day Have a nice day'
#  
#(결과) 
# a 개수 : 9
# 첨자 : [1, 5, 13, 17, 21, 29, 33, 37, 45]
st = 'Have a nice day Have a nice day Have a nice day'
lst =[]
idx = 0
while True:
    idx = st.find('a',idx)
    if idx != -1:
        lst.append(idx)
        idx +=1
    else:
        break
print("a 개수 : ",st.count('a'))
print("첨자 : ",lst)





