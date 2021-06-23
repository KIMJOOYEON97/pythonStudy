'''
# 1개 이상의 정수, 실수 값을 인자로 받아 
# 가장 큰 값 또는 가장 작은 값을 반환하는 pyMax(),pyMin()함수를 만드시오 
def pyMax(*par):    #가변인자 사용
    mx=par[0]
    for x in par[1:]:
        if mx < x:
            mx= x
    return mx

def pyMin(*par):
    mx=par[0]
    for x in par:
        if mx > x:
            mx= x
    return mx
print(pyMax(123,3454,678,1234,4432))
print(pyMin(123,3454,678,1234,4432))

# 0~N까지 또는 M~N까지의 임의 값을 반환하는 함수를 만드시오
# 0은 기본인자. M~N까지임으로 인자가 2개 필요 
from random import random
def myrandom(min,max=0): #M~N까지 해당하는 코드 작성
    if max ==0:         #값을 넣지않고 여전히 기본값으로 사용하고 있는 경우
        min,max=max,min #밑의 두식을 합친것//값 스위칭할때씀//#min=max     #min의 값을 max로 대체
                                                            #max=min      #max의 값을 min으로 대체 
                                                        #근데 두개로 나눠서 쓰면 값이 0 나옴
    return int(random()*(max-min+1))+min  #(max-min+1) 1~5까지 나올 수 있게 작성

# myrandom(5) #->0~5  초기값 min이 5가 될 수 있음
# myrandom(1,5) #->1~5
print(myrandom(5))
print(myrandom(1,5))

#min=max  의 경우 print(myrandom(5))값이 0밖에 안나온다 => 다이어리참조
#max=min

#다음 조건을 보고 회원가입을 위한 프로그램 코드를 작성 하시오
# -아이디는 반드시 10자리 이상
# -패스워드는 반드시 8~16자리 사이
# -패스워드에 아이디가 포함되면 안됨
# -패스워드에는 담음의 특수문자가 반드시 하나 이상 포함(~,!,@,#,$,%,^,&,*,_,?)



# 메뉴를 자동으로 선택하여 출력하는 코드를 작성 하시오.
# menu={'칼국수':6000,'비빔밥':5500,'돼지국밥':7000,'돈까스':7000,'김밥':2000,'라면':2500}  
menu={'칼국수':6000,'비빔밥':5500,'돼지국밥':7000,'돈까스':7000,'김밥':2000,'라면':2500}  
for x in range(len(menu)):
    a=menu.popitem()
    print(a)
    sel=input("계속하시겠습니까?(Y/n)")
    if sel !='n':
        continue
    else:
        break


# menu=[['칼국수',6000],['비빔밥',5500],['돼지국밥',7000],['돈까스',7000],['김밥',2000],['라면',2500]]   
# 사용자 입력으로 메뉴와 가격을 입력받아 menu변수에 자료를 추가 할 때 
# 기존에 동일한 메뉴가 존재하는 경우 가격만 변경되도록 코드를 작성
#TypeError: 'list' object cannot be interpreted as an integer
# 진짜 오지게 시간 들엇음 
menu=[['칼국수',6000],['비빔밥',5500],['돼지국밥',7000],['돈까스',7000],['김밥',2000],['라면',2500]]
s=input("변경할 메뉴 입력 : ")
p=int(input("변경할 가격입력 : "))
flag = 0
for i in range(len(menu)):
    for j in range(1):
        if menu[i][j]==s:
            value = menu[i]
            menu.remove(value)
            menu.append([s,p])
            flag=1  
        j += 1
    i += 1
if flag == 0:
    menu.extend([s,p])
print(menu)    
# 메뉴를 자동으로 선택하여 출력하는 코드를 작성하시오
from random import random
menu=[['칼국수',6000],['비빔밥',5500],['돼지국밥',7000],['돈까스',7000],['김밥',2000],['라면',2500]]
while True:
    rand=int(random()*len(menu))
    print(menu[rand])
    sel=input("계속하시겠습니까?(Y/n)")
    if sel !='n':
        continue
    else:
        break

# 사용자 입력으로 1개 이상의 메뉴를 입력받아 해당 메뉴의 총 가격을 출력하시오.(튜플,리스트, 딕셔너리 ver으로 3개 만들기)
# (exit를 입력하면 더 이상의 입력을 받지 않음)
#튜플
menu=('칼국수',6000),('비빔밥',5500),('돼지국밥',7000),('돈까스',7000),('김밥',2000),('라면',2500)
print("'칼국수',6000\n'비빔밥',5500\n'돼지국밥',7000\n'돈까스',7000\n'김밥',2000\n'라면',2500")
tot =0
while True:
    s=input("메뉴를 입력하세요:")
    for x in range(len(menu)):
        for y in range(len(menu[x])):
            if s==menu[x][y]:
                p=menu[x][1]
                tot = tot + p
            y += 1
        x += 1
    sel=input("계속하시겠습니까?(Y/n)")
    if sel != 'n':
        continue
    else:
        print("총 가격 :",tot,"원")
        break
'''
#리스트
menu=[['칼국수',6000],['비빔밥',5500],['돼지국밥',7000],['돈까스',7000],['김밥',2000],['라면',2500]]
print("'칼국수',6000\n'비빔밥',5500\n'돼지국밥',7000\n'돈까스',7000\n'김밥',2000\n'라면',2500")
tot = 0
while True:
    s=input("메뉴를 입력하세요:")
    for x in range(len(menu)):
        for y in range(len(menu[x])):
            if s ==menu[x][y]:
                p = menu[x][1]
                tot = tot +p
    sel=input("계속하시겠습니까?(Y/n)")
    if sel != 'n':
        continue
    else:
        print("총 가격 :",tot,"원")
        break
              
#딕셔너리
menu={'칼국수':6000,'비빔밥':5500,'돼지국밥':7000,'돈까스':7000,'김밥':2000,'라면':2500}  
print("'칼국수',6000\n'비빔밥',5500\n'돼지국밥',7000\n'돈까스',7000\n'김밥',2000\n'라면',2500")
tot = 0
while True:
    s=input("메뉴를 입력하세요:")       #메뉴를 잘못 입력했을 경우 ex) 칼수국 했을 때 다시입력하세요라고 나오게 하는 방법
    p=menu[s]
    tot=tot +p
    sel=input("계속하시겠습니까?(Y/n)")
    if sel != 'n':
        continue
    else:
        print("총 가격 :",tot,"원")
        break

# 1~20까지의 정수 값을 출력하는 코드 작성 while구문
x=0
while x<21:
    x+=1
    print(x,end=" ")
print()
# 1~100까지의 누적 합을 구하는 코드 작성 while구문
x,tot = 0,0
while x<101:
    tot = tot + x
    x+=1
print(tot)

# 사용자가 입력한 값을 초과하지 않는 한도에서의 누적 합을 구하는 코드를 작성하시오
# (누적합은 랜덤으로 1~10까지 생성)
user =int(input("수를 입력하세요: "))
tot=0
for x in range(user):
    tot = tot + x
    x+=1
print(tot)  


# 사용자가 입력한 정수 값에 대해 2진수로 변환하여 출력하는 코드를 작성하시오  
user =int(input("수를 입력하세요: "))
print(bin(user))
#100~51까지의 정수 값 중 홀수 해당하는 값 만을 출력하는 코드를 작성하시오
lst =[]; x=0
for x in range(51,101):
    if x%2 != 0:
        lst.append(x)
    x +=1
print(lst)

lst =[]; x=0
while x<101 and x>51:       #while x<101 and x>51:  왜 빈 리스트만 뜰까?
    if x%2 != 0:
        lst.append(x)
    x +=1
print(lst)
        
# 1~50까지 정수 값을 출력 할 때 한 줄에 5개의 값이 출력되도록 하시오
for x in range(10):
    for y in range(1,6):
        print(x*5+y,end=" ")
    print()
    
for x in range(1,51):
    if x%5 != 0:
        print(x,end='')
    else:
        print(x)

# 1~100까지의 누적 합을 구하는 코드를 작성하시오
tot=0
for x in range(1,101):
    tot = tot+x
print(tot)
# 다음 문자열 변수에서 공백을 제외한 문자의 수를 구하시오  st='Python basic program language'
st='Python basic program language'
tot =0
for x in st:
    if x !=' ':
        tot += 1
print(tot)
# 'a'~'z'까지 임의의 문자열을 8자리씩 총 10개를 생성하는 코드를 작성하시오. (시리얼 넘버 생성)
from random import randint
for x in range(10):
    for y in range(8):
        print(chr(randint(97,122)),end="")
    print()
# 'a'~'z','A'~'Z','0'~'9'까지 임의의 문자열을 16자리씩 총 10개를 작성하는 코드를 작성하시오.(시리얼 넘버 생성)
from random import randint
for x in range(10):
    for y in range(16):
        z=randint(0,2)
        if z==0:
            print(chr(randint(97,122)),end="")
        if z==1:
            print(chr(randint(65,90)),end="")
        if z==2:
            print(randint(1,9),end="")
    print()


