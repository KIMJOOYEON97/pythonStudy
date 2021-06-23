'''
[ 문제2 ] 
   위 내용을 이용하여 문서 파일에 저장할 입력 내용을 암호화 시켜주세요.
- 문자열을 암호화 하여 파일에 저장 할 수 있도록 코드를 수정
  (문자열을 반복적으로 입력할 수 있게 만들어서 처리 후 암호화)
- 반대로 암호화 된 문자열을 복호화 하여 화면에 출력할 수 있도록 코드를 수정 *복호화 => 암호화 해제
'''
'''
import os
readstr,fileName="",""
key =100    #key 값도 입력받을 수 있다
while True:
    os.system("cls")
    choice = input("1. 파일 저장 \n2. 파일 불러오기\n0. 종료\n번호선택>>>")
    if choice =='1':
        savestr=""
        fileName = input("파일명 입력: ")
        saveFile = open(fileName,'a',encoding="utf-8")
        while True:
            contents = input("문자열 입력 : ")
            for i in contents:
                chNum =ord(i)
                chNum += key
                savestr+=chr(chNum)
            savestr+="\n"
            sel = input("문자열 입력 계속하겠습니까? (Y/n)")
            if sel == 'n':
                saveFile.write(savestr)
                saveFile.close()
                break #choice==1에 대한 반복 구문 종료
    elif choice=='2':
        fileName = input("파일명 입력: ")
        readFile = open(fileName,'r',encoding="utf-8")
        printstr=""
        while True:
            readstr = readFile.readline()
            if readstr == "":
                readFile.close()
                break
            readstr = readstr.strip("\n")   #savestr+="\n"을 했으면 반드시 이 작업을 해야한다. "\n"은 암호화와 아무상관이 없음으로 빼줘야함
            for i in readstr:
                chNum= ord(i)
                chNum -= key
                printstr += chr(chNum)
            printstr += "\n"    #볼 때는 개행이 이루어지게.
        print("\"{}\"파일에 있는 내용\n{}".format(fileName,printstr))
        os.system('pause')
    elif choice =='0':
        print("프로그램 종료!!")
        break
    else:
        print("번호 선택 오류!!")

# open()의 모드에 "+" 옵션 사용하기 
#           =>읽기와 쓰기를 같이한다. 읽을 수도 있고 적어서 다시 쓸 수도 있다.동시에 되도록 할 수 있음
fileName = input("파일명 입력 : ")
file = open(fileName,"r+",encoding="utf-8")
readstr=file.read()
print(readstr,end="")
writestr= input("\n문서에 추가할 내용을 입력 하세요: ")
file.write(writestr+"\n")
file.close()

# 모드 옵션 
# t =>텍스트(문서) => 생략가능
# b =>바이너리(2진데이터) => 생략불가. 
                            # 파일 데이터를 전달할 때 바이너리 값을 사용하는 것이 가장 안전하다.

# 문제] file입출력을 이용하여 "특정 파일"을 복사하는 프로그램 코드를 작성하세요.
# 복사할 대상(원본): test.jpg #한글 파일도 동영상도 가능하다.
# 복사할 위치(복사본): d:\python\test_copy.jpg
 
src = input("복사할 대상(원본) : ")
dst = input("복사할 위치(복사본) : ")
rFile = open(src,"rb")  #encoding은 필요 없다. 데이터를 읽기 위한 것이니까
wFile = open(dst,"wb")
buffer = rFile.read()   #바이너리 값 데이터를 buffer공간에 읽어들인 데이터 저장
i = wFile.write(buffer)
if i != 0 or i != -1:   #복사를 실패하면 0이나 -1을 반환.
    print("복사를 성공적으로 마쳤습니다.크기는 {:,}bytes 입니다.".format(i))
else:
    print("복사가 완료되지 않았습니다.")
rFile.close()
wFile.close()

#python의 예외 처리 
#  예외: 프로그램에서 벌어지는 예외적 상황(Error들) 
#        
# 예)
# -파일을 읽고자 할 때, 그 파일이 존재하지 않는 경우(FileNotFound)
# -어떤 값을 0으로 나누고자 할 때 (ZeroDivision)
# -배열의 인덱스 범위를 벗어났을 경우(Out of range)
# -사용자의 요구대로 진행이 되지 않았을 경우  
    #음수로 나이를 표현할 수 없는데 컴퓨터는 음수로 나올 수 있음. =>예외처리 사항
# 
# (예외처리 형식)
# try:      #예외처리 시작(예외검증)
#       예외처리 검증구문1  #예외가 발생할만한 상황을 입력 
#       예외처리 검증구문2
# except (예외처리 코드-에러코드):
#       예외상황에 따른 진행코드1
#       예외상황에 따른 진행코드2
# ... //여러개의 에러에 대한 것들에 대한 예외상황입력 가능 like: if-elif-else

# 예제1] 검증 내용은 두수를 나누기 할 때
try:
    num1 = int(input("첫번째 정수 : "))
    num2 = int(input("두번째 정수 : "))
    Div = num1/num2
    print("나눗셈 결과 : ",Div)
except ValueError: #정수값이 아닌 다른 값을 입력했을 때
    print("정수 값 입력하세요!!!") #에러가 발생해도 프로그램 종료되지 않음
except ZeroDivisionError:
    print("숫자 0으로 나눌 수 없어요!!")
print("예외처리 이후 프로그램 진행....") 

#예제 2] try: ~ except ~else 구문
# try:      #예외처리 시작(예외검증)
#       예외처리 검증구문1  #예외가 발생할만한 상황을 입력 
#       예외처리 검증구문2
# except (예외코드):    #예외발생시 동작
#       예외발생시 코드1
#       예외발생시 코드2
# ...
# else:             #예외 발생 안한 경우 실행/ except에 있는 모든 코드가 발생하지 않은 경우
#       예외발생하지 않은 경우 코드1
#       예외발생하지 않은 경우 코드2 

try:
    num=int(input("수입력 : "))
except ValueError:
    print("정수만 입력 하세요!!!")
else:
    print("입력 값 출력 {} - 예외 처리 안된 경우 실행".format(num))

# 예제 3] 파일 관련 예외처리(파일이 없는 경우) read일때, 경로상에 디랙토리 내용이 없는 경우 a,w도 Error
fileName =input('파일명 : ')
try:
    file = open(fileName,"r",encoding="utf-8") #file = open("fileName","r",encoding="utf-8") (X)
    buf=file.read()
    print(buf)
except FileNotFoundError:   #FileExistError도 있음
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
#     => raise Exception("예외 사항") /Exception-class
try:
    age=int(input("나이를 입력하세요: "))
except ValueError:
    print("소수점 이하 문자, 문자를 입력")
except Exception:
    if age<0:
        print("나이는 0보다 작을 수 없습니다.")
else:
    print("당신의 나이는",age,"입니다")
'''
#풀이
try:
    age= int(input("당신의 나이를 입력하세요: "))
    if age<=0:
        raise Exception("예외상황발생")   #Exception(*args, **kwargs)- 가변인자 쓴다
except ValueError:
    print("양의 정수를 입력하세요!!!")
except Exception as e:  #as는 예외에 대한 내용<raise Exception("예외상황발생"=>e)>이 e에 저장되게 해줌
    print(e,"0보다 작은 나이는 존재하지 않습니다.")
else:
    print("당신의 나이는 {}살 입니다.".format(age))
finally:    #예외처리 로직의 끝에 실행할 내용  finally: 최종적으로 무조건,반드시!! 실행하는 것
    print("프로그램 종료하겠습니다.")