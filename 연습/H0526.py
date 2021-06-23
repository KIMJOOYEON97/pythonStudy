# 4)범위 내에 숫자를 구할 때 
    # 어떤 값을 넣어도 1~6 사이의 값을 출력 
    # => (x%6)+1 
    #     x%6=>(0,1,2,3,4,5)+1
print("{}%{}={}".format(20,7,20%7))

# 예제6] for문 - List, tuple, dictionary... 
i=0
for x in [1,4,78,'test','A',1.80,100]:
    print(x,end=" ")
    i += 1
print("\n",i,"번 반복함")

#문제 2] 중첩 For문을 이용하여 구구단 표를 작성 #기준점에 따라 달라짐 ?다시보기
# 2 x 1 = 2   3 x 1 = 3   4 x 1 = 4   5 x 1 = 5   6 x 1 = 6   ...
# 2 x 2 = 4   3 x 2 = 6   4 x 2 = 8   5 x 2 = 10  6 x 2 = 12  ...
# 2 x 3 = 6   3 x 3 = 9   4 x 3 = 12  5 x 3 = 15  6 x 3 = 18  ...
# ....        ...         ...         ...         ...         
for x in range(1,10):
    for y in range(2,10):
        print("{} x {} = {}".format(y,x,x*7),end="\t")
    print()
print()

#문제 3] 다음과 같이 출력되게 For구문을 작성하세요...!
# 상위 For문이 0일때, 하위 For문 : 0 0 0 0 0   
# 상위 For문이 1일때, 하위 For문 : 0 1 2 3 4   
# 상위 For문이 2일때, 하위 For문 : 0 2 4 6 8   
# 상위 For문이 3일때, 하위 For문 : 0 3 6 9 12  
# 상위 For문이 4일때, 하위 For문 : 0 4 8 12 16 
for x in range(5):
    print("상위 For문이 {}일때, 하위 For문: ".format(x),end="")
    for y in range(5):
        print(x*y,end=" ")
    print()
print()
# 문제 4) 이중 For문을 사용하여 다음과 같이 출력되게 ????
# 만들어 보세요. 
#  1) 1   2   3   4   5
#     6   7   8   9   10
#     11  12  13  14  15
#     16  17  18  19  20
#     21  22  23  24  25
Sum=0
for x in range(5):
    for y in range(5):
        Sum+=1
        print(Sum,end='\t')
    print()
print()

for x in range(5):
    for y in range(1,6):
        print(x*5+y,end="\t")
    print()
print()

for x in range(6):
    for y in range(1,6):
        print(x*5+y,end="\t")
    print()
print()
#   1   2   3   4   5   
#   6   7   8   9   10
for x in range(2):
    for y in range(1,6):
        print(x*5+y, end=" ")
    print()
print()
#   1   2   3   4   5   6   7   8   9   10
#   11  12  13  14  15  16  17  18  19  20
#   21  22  23  24  25  26  27  28  29  30
for x in range(3):
    for y in range(1,11):
        print(x*10+y,end='\t')
    print()
print()
Sum=0
for x in range(3):
    for y in range(10):
        Sum += 1
        print(Sum, end="\t")
    print()
print()

#2)
# 25  24  23  22  21  
# 20  19  18  17  16  
# 15  14  13  12  11  
# 10  9   8   7   6   
# 5   4   3   2   1
Sum = 26
for x in range(5):
    for y in range(5):
        Sum -= 1
        print(Sum,end='\t')
    print()
print()

for x in range(5,0,-1):
    for y in range(5):
        print(x*5-y,end="\t")
    print()
print()
# 30  34  33  32  31
# 25  24  23  22  21  
# 20  19  18  17  16  
# 15  14  13  12  11  
# 10  9   8   7   6   
# 5   4   3   2   1
for x in range(6,0,-1):
    for y in range(5):
        print(x*5-y,end="\t")
    print()
print()

Sum=31
for x in range(6):
    for y in range(5):
        Sum -= 1
        print(Sum, end='\t')
    print()
print()
#3)
# 1   2   3   4   5     
# 2   3   4   5   1   
# 3   4   5   1   2   
# 4   5   1   2   3   
# 5   1   2   3   4
#  if 사용가능한 것과 다른 것 2개

for x in range(5):
    for y in range(5):
        print((x+y)%5+1, end='\t')
    print()
print()

for x in range(5):
    for y in range(5):
        if x==0:
            s=1
        elif x==1:
            s=2
        elif x==2:
            s=3
        elif x==3:
            s=4           
        elif x==4:
            s=5
        print(s+y,end="\t")
    print()
print()

Sum=4
for x in range(5):
    for y in range(5):
        Sum+=1
        print(Sum%5+1, end='\t')
    print()
print()

Sum=4
for x in range(5):
    for y in range(5):
        Sum+=1
        print("{}".format(Sum%5+1),end="\t")
    print()
print()