var=2               # global 전역변수- 최상위위치에서 변수를 선언함.
def func(arg):
    var1 = 1        # local 지역변수    
    global var      # global 전역변수를 블럭영역으로 불러옴/ 블럭내에서는 영향을 준다.
    var = 8         # -> 전역변수가 됌
    print(var1,var,arg) #=> 1 3 2//변수에 해당된 이름이 같으면 가장가까운 지역변수를 선택한다.
#메인
func(var)   # 1 2
#print(var1) #지역변수 var1은 블럭을 벗어나면 사라짐. undefined NameError: name 'var1' is not defined
print(var)  # 2
a,b=1,2
var=5
def funcc(arg):
    global a,b
    a,b = 7,8 
    print(a,b,arg)
funcc(var)
print(a,b)