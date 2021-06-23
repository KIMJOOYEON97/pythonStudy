# 파일에 내용을 쓰기 
'''
# 1.open()로 파일 작업할 정보를 생성
file =open("test.txt","w",encoding="utf-8") #접근하는 순간 싹 지움
# file-변수명   파일명, 모드, 
# 2.open()으로 얻어진 정보를 가지고 작업
str1=input("파일에 저장할 내용 입력 : ")
i = file.write(str1) #.write - str의 길이  #파일에 저장하는 내용 쓰는 것.
print(i)
# 3.close() 작업한 파일 내용을 끝냄
file.close()

# 파일의 내용을 읽어들이기
# 1.open()
file2 = open("test.txt","r",encoding="utf-8")
# 2. 파일에 대한 작업
readstr=file2.read()    #파일을 readstr에 저장
print(readstr)
# 3. close()
file2.close()
'''
'''
[quiz] 파일명 : quiz1.txt
1. 본인의 인적사항을 파일에 저장 후에 출력하세요. 
(이름, 나이, 주소)
- 당신의 이름: 홍길동
- 홍길동 님의 나이는 : 20살
- 홍길동 님의 주소는 : 산골짜기

[출력결과] => 파일에 저장된 결과를 출력
홍길동
20살
산골짜기
'''
'''
file3=open("quiz1.txt","a",encoding='utf-8')
str3=input("당신의 이름 : \n홍길동 님의 나이는 : \n홍길동 님의 주소는 : ")
x = file3.write(str3) #반환값이 없도 됌
file3.close

file3=open("quiz1.txt","r",encoding='utf-8') #읽기는 따로 만들어야 읽을 수 있음
readstr1=file3.read()
print(readstr1)
file3.close

#파일입력
file = open("quiz1.txt","w",encoding="utf-8")
name=input("당신의 이름: ")
age=input("{}님의 나이는 : ".format(name))
addr=input("{}님의 주소는: ".format(name))
file.write(name+"\n"+age+"\n"+addr)
file.close()

#파일읽기
file = open("quiz1.txt","r",encoding="utf-8")
readstr= file.read() #read() 처음부터 끝까지 읽어들임
print(readstr)          #()안에 숫자를 입력하면 그 숫자만큼 읽어들임

file.close()

#예제2] readline()  //-file함수
#       =>데이터를 읽어들일때에 "\n"을 기준으로 데이터를 읽어들이는 함수
file2= open("quiz1.txt","r",encoding='utf-8')
while True:
    readfile2=file2.readline()  #변수에 저장이 됌 이때 변수를 '버퍼'라고 함
    if readfile2 == "": #"(NULL)"은 문자열의 마지막을 의미함..
        print("\n더 이상 값이 존재하지 않습니다.")
        file2.close()
        break
    print(readfile2,end='')         #문자열이 없다는 의미// 공백이 나온다는 것은 넘길 것이 없다
print("결국",type(readfile2))

#예제3] readlines() 
#      =>"\n"을 기준으로 데이터를 읽어들이는 함수, 읽어들인 문장들은
#         리스트에 저장하는 함수. 
file3=open("quiz1.txt","r",encoding="utf-8")

buf = file3.readlines() #반복구문 사용하지 않고 \n을 기준으로 전체를 리스트에 저장해서 출력
print(buf,type(buf))
file3.close()

for i in range(len(buf)):
    buf[i] = buf[i].strip("\n")
    print(buf[i])
print(buf,type(buf))

#예제4] ord()=>문자를 인코딩 값(정수)으로 출력, #10진수 값을 출력
#       chr()=>인코딩 값을 문자로 출력
print(ord('안'))    #50504      #한글은 2bite를 씀(0~6만5천35 범위) /영어는 1bite
print(ord('녕'))    #45397      #글자 하나가 인코딩 값으로 들어감.=>패턴이 없음
print(ord('하'))    #54616
print(ord('세'))    #49464
print(ord('여'))    #50668
print(ord('1'))     #49 
print(ord('a'))     #97

print(hex(ord('안')))    #0xc548
print(hex(ord('녕')))    #0xb155
print(hex(ord('하')))    #0xd558
print(hex(ord('세')))    #0xc138
print(hex(ord('여')))    #0xc5ec

print(chr(49))
print(chr(97))

print(chr(0xc548))
print(chr(0xb155))
print(chr(0xd558))
print(chr(0xc138))
print(chr(0xc5ec))
print(chr(0x31))
print(chr(0x61))

# 예제5] 문자의 암호화(한글자)
readstr, content= "","" #비어있는 문자열 변수 선언
key=100
choice = input("1. 파일 저장 \n2. 파일 불러오기 \n 번호선택>>>")
fileName =input("파일명 입력 : ") 
if choice =='1':
    content=input("단일문자 입력 : ")
    filesave = open(fileName,"w",encoding="utf-8")
    chNum =ord(content) #chNum 정수가 됌
    chNum =chNum + key
    content = chr(chNum)
    filesave.write(content) #저장
    filesave.close()
elif choice =='2':
    fileread =open(fileName,"r",encoding="utf-8")
    readstr = fileread.read()
    chNum = ord(readstr)
    chNum = chNum - key
    readstr =chr(chNum)
    print("파일에 저장된 값: ",readstr)
    fileread.close()

'''
'''
[ 문제1 ] 
   위 예제를 이용하여 문자열을 암호화 시켜주세요.
- 현재 단일 문자만 저장이 가능
- 문자열을 암호화 하여 파일에 저장 할 수 있도록 코드를 수정
- 반대로 암호화 된 문자열을 복호화 하여 화면에 출력할 수 있도록 코드를 수정
'''
'''
readstr , contents = "" , "" 
key = 100
choice = input("1. 파일 저장 \n2. 파일 불러오기 \n 번호선택>>>")
fileName =input("파일명 입력 : ")
if choice =='1':
    contents=input("문자열 입력 : ")
    filesave = open(fileName,"w",encoding="utf-8")
    for x in contents:
        chNum =ord(x) 
        chNum =chNum + key
        contents = chr(chNum)
        filesave.write(contents) 
    filesave.close()
elif choice =='2':
    fileread =open(fileName,"r",encoding="utf-8")
    readstr = fileread.read()
    readstrs=""
    for y in readstr:
        chNum = ord(y)
        chNum = chNum - key
        readstr =chr(chNum)
        readstrs += readstr
    print("파일에 저장된 값: ",readstrs)
    fileread.close()
'''
'''
#풀이
import os
readstr,savestr,printstr="","",""
key=100
while True:
    os.system("cls")
    choice =input("1. 파일 저장 \n2. 파일 불러오기\n0. 종료\n번호선택>>>")
    if choice =='1':
        fileName = input("파일명 입력 : ")
        filewrite = open(fileName,"w",encoding="utf-8")
        contents =input("문자열 입력 : ")
        for i in contents: #한문자씩 불러와짐
            chNum = ord(i)
            chNum +=key
            savestr += chr(chNum)
        filewrite.write(savestr)
        filewrite.close()
    elif choice =='2':
        fileName = input("파일명 입력 : ")
        fileread =open(fileName,"r",encoding="utf-8")
        readstr = fileread.read()
        for i in readstr:
            chNum = ord(i)
            chNum -= key
            printstr +=chr(chNum)
        print("파일에 저장된 값: ",printstr)
        fileread.close()
        os.system('pause')
    elif choice=='0':
        print("프로그램을 종료합니다.")
        break
'''

'''
[ 문제2 ] 
   위 내용을 이용하여 문서 파일에 저장할 입력 내용을 암호화 시켜주세요.
- 문자열을 암호화 하여 파일에 저장 할 수 있도록 코드를 수정
  (문자열을 반복적으로 입력할 수 있게 만들어서 처리 후 암호화)
- 반대로 암호화 된 문자열을 복호화 하여 화면에 출력할 수 있도록 코드를 수정 *복호화 => 암호화 해제
'''

import os

key=int(input("키값을 입력하세요.:"))
while True:
    os.system("cls")
    choice =input("1. 파일 저장 \n2. 파일 불러오기\n0. 종료\n번호선택>>>")
    if choice =='1':
        savestr=""
        fileName = input("파일명 입력 : ")
        filewrite = open(fileName,"w",encoding="utf-8")
        while True:
            num = input("입력을 하시겠습니까? (0입력시:종료)")
            contents =input("문자열 입력 : ")
            for i in contents: 
                chNum = ord(i)
                chNum +=key
                savestr += chr(chNum)
            savestr+="\n"
            if num=='0':
                print("입력을 종료합니다.")
                filewrite.write(savestr)
                filewrite.close() 
                break             
    elif choice =='2':
        fileName = input("파일명 입력 : ")
        fileread =open(fileName,"r",encoding="utf-8")
        printstr=""
        while True:    
            readstr = fileread.readline() #readkines(x) 리스트는 strip()결과 가져오지 않음
            readstr = readstr.strip("\n")
            if readstr =="":
                fileread.close()
                break            
            for i in readstr:
                chNum = ord(i)
                chNum -= key
                printstr +=chr(chNum)   #ValueError: chr() arg not in range(0x110000)

            printstr+="\n"
        print("파일에 저장된 값:\n ",printstr)
        os.system('pause')
    elif choice=='0':
        print("프로그램을 종료합니다.")
        break
