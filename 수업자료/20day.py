'''
[ 문제2 ] 
   위 내용을 이용하여 문서 파일에 저장할 입력 내용을 암호화 시켜주세요.
- 문자열을 암호화 하여 파일에 저장 할 수 있도록 코드를 수정
  (문자열을 반복적으로 입력할 수 있게 만들어서 처리 후 암호화)
- 반대로 암호화 된 문자열을 복호화 하여 화면에 출력할 수 있도록 코드를 수정

import os
readstr,fileName ="",""
key = 100
while True:
    os.system("cls")
    choice = input("1.파일 저장\n2.파일 불러오기\n0.종료\n번호선택>>>")
    if choice=="1":
        savestr =""
        fileName = input("파일명 입력 : ")
        saveFile = open(fileName,"a",encoding="utf-8")
        while True:
            contents = input("문자열 입력 : ")
            for i in contents:
                chNum = ord(i)
                chNum += key
                savestr += chr(chNum)
            savestr+="\n"
            sel = input("문자열 입력 계속하겠습니까?(Y/n")
            if sel == 'n':
                saveFile.write(savestr)
                saveFile.close()
                break
        
    elif choice=='2':
        fileName = input("파일명 입력 : ")
        readFile = open(fileName,"r",encoding="utf-8")
        printstr=""
        while True:
            readstr = readFile.readline()
            if readstr == "":
                readFile.close()
                break
            readstr = readstr.strip("\n")
            for i in readstr:
                chNum = ord(i)
                chNum -= key
                printstr += chr(chNum)
            printstr+="\n"
        print("\"{}\" 파일에 있는 내용\n{}".format(fileName,printstr))
        os.system("pause")
    elif choice=="0":
        print("프로그램 종료!!")
        break
    else:
        print("번호 선택 오류!!")

# open()의 모드에 "+" 옵션 사용하기]
fileName = input("파일명 입력 : ")
file = open(fileName,"r+",encoding="utf-8")
readstr = file.read()
print(readstr,end="")
writestr = input("\n문서에 추가할 내용을 입력 하세요 : ")
file.write(writestr+"\n")
file.close()

# 모드 옵션 
# t => 텍스트(문서)=> 생략 가능
# b => 바이너리(2진데이터)  

# 문제] file입출력을 이용하여 "특정 파일"을 복사하는 프로그램 코드를 작성하세요.
# 복사할 대상(원본) : test.jpg
# 복사할 위치(복사본) : f:\python\test_copy.jpg
#
src = input("복사할 대상(원본) : ")
dst = input("복사할 위치(복사본) : ")
rFile = open(src,"rb")
wFile = open(dst,"wb")
buffer = rFile.read()
i = wFile.write(buffer)
if i != 0 or i != -1:
    print("복사를 성공적으로 마쳤습니다. 크기는 {:,}bytes 입니다.".format(i))
else:
    print("복사가 완료되지 않았습니다.")
rFile.close()
wFile.close()
 
# python 예외 처리
#  예외 : 프로그램에서 벌어지는 예외적 상황(Error들)
# 
#  예)
#  -파일을 읽고자 할 때, 그 파일이 존재하지 않는 경우(FileNotFound)
#  -어떤 값을 0으로 나누고자 할 때(ZeroDivision)
#  -배열의 인덱스 범위를 벗어났을 경우 
#  -사용자의 요구대로 진행이 되지 않았을 경우
# 
# (예외처리 형식)
# try:      # 예외처리 시작(예외검증)
#     예외처리 검증 구문1
#     예외처리 검증 구문2
# except (예외처리 코드-에러코드):
#     예외상황에 따른 진행 코드1
#     예외상황에 따른 진행 코드2
#   ...  

# 예제1] 검증 내용은 두수를 나누기 할 때
try:
    num1 = int(input("첫번째 정수 : "))
    num2 = int(input("두번째 정수 : "))
    Div = num1/num2
    print("나눗셈 결과 : ",Div)
except ValueError:
    print("정수 값 입력하세요!!!")
except ZeroDivisionError:
    print("숫자 0으로 나눌 수 없어요!!")
print("예외처리 이후 프로그램 진행... ")

# 예제2] try: ~ except ~ else 구문
# try:      # 예외 검증
#     예외검증문장1
#     예외검증문장2
# except (예외코드):   #예외발생시 동작
#     예외발생시 코드1
#     예외발생시 코드2
# ...
# else:             # 예외 발생 안한 경우 실행
#     예외 발생하지 않은 경우 코드1
#     예외 발생하지 않은 경우 코드2 

try:
    num = int(input("수입력 : "))
except ValueError:
    print("정수만 입력 하세요!!!")
else:
    print("입력 값 출력 {} - 예외처리 안된 경우 실행".format(num))
'''
# 예제3] 파일 관련 예외처리(파일이 없는 경우)
fileName = input('파일명 : ')
try:
    file = open(fileName,"r",encoding="utf-8")
    buf = file.read()
    print(buf)
except FileNotFoundError:
    print("지정한 파일이나 디렉터리가 존재하지 않습니다.")
else:
    file.close()
    print("문제없이 잘 실행했습니다.")

#문제] 나이를 입력받는 프로그램을 만들 때에 잘못된 값을 입력시 
# 예외처리를 만들어보세요. 
#
#  - 입력값 에러 : ValueError => 소수점 이하 문자, 문자를 입력
#  - 입력값이 0보다 작은 경우, 
#     강제로 Exception작업을 해야 함. 
#     => raise Exception("예외 사항") 
try:
    age = int(input("당신의 나이를 입력하세요 : "))
    if age < 0:
        raise Exception("예외상황발생")
except ValueError:
    print("양의 정수를 입력 하세요!!!")
except Exception as e:
    print(e,"0보다 작은 나이는 존재하지 않습니다.")
else:
    print("당신의 나이는 {}살 입니다.".format(age))
finally:                # 예외처리 로직의 끝에 실행할 내용
    print("프로그램 종료 하겠습니다.")


