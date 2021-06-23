print(bool(1))
print(bool(0))
print(bool(-1))
print(bool(''))
print(bool(' '))
print(bool('a'))
print(bool([]))
print(bool([-1]))


x,y,z=10,10.0,"10"
print(type(x))
print(type(y))
print(type(z))
print(x+y,type(x+y))
print(x*y,type(x*y))
#print(x+z,type(x+z))
print(x+int(z),type(x+int(z)))
print(x+float(z),type(x+float(z)))

a,b=0,''
print(bool(a))
print(bool(b))

x,y,z='100',10.5,20
print(float(x)+y)
print(x+str(z))
print(str(y)+str(float(z)))
print(str(float(x)+y)+str(z))

print()

print("|{:_^30,f}|".format(1234))

x,y=3,5
print(bool(x==y))
print(bool(x!=y))
print(bool(x>y))
print(bool(x<y))
x=5
print(bool(x<=y))
print(bool(x>=y))

x,y='a','b'
print(bool(x==y));print(bool(x!=y))
print(bool(x<y));print(bool(x>y))

'''
????????
x,y='a',1
print(bool(x>y))
print(bool(x<y))
'''

x,y,a,b=3,5,'a','b'
print(bool(x<y))
print(bool(a!=b))    #문자열 타입만 같은 거임. a b는 서로 다름
print(bool(x<y and a!=b))
print(bool(x<y and a==b))
print(bool(x>y or a!=b))
print(bool(x>y or a==b))

print(bin(10))
print(bin(5))
print(0b1010)
print(0b101)
print(10&5)
print(10|5)
print(10^5) 
print(10<<2)
print(10>>2)

x,y,z=5,15,27
print(float(y-z))
print(y-z)
print(x*y)
print(pow(x,2))
print(x**2)
print(z/x)
print(y/x)


print(bool(7>8))
print(bool(5<2))
print(bool(6%3>2))
print(bool(5+5!=2*5))
print(bool(True==1))
print(bool(1=='1'))
print(bool(10//3==10%3))
print(bool(15%4 in(0,1,2)))


from random import random
print(random())
print(random()*10)
print(int(random()*10))
print(int(random()*10+1))

from random import randint
print(randint(5,10))

from random import randrange
print(randrange(5,10))
print(randrange(5,10,2))

from random import randint
print(chr(randint(65,90)))
print(chr(randint(97,122)))

from random import random
print(random()*100+1)
print(random()*900+100) 
a=chr(int(random()*26)+65)  #? >>이거랑 상관있는지는 모르겠는데 input()형 자료는 문자형이라 형변환 필요
b=chr(int(random()*26+65))
c=chr(int(random()*26+65))
print(a+b+c)

from random import random
a=int(random()*99+1)
print("{}:{}".format(a, not bool(a%2)))
print("{}:{}".format(a, a%2==0))