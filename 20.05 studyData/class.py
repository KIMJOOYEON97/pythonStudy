animals=['lion','tiger','cat','dog']
mountains=['Everest','Eiger','Baekdu','Halla']
animals.sort()
mountains.sort(reverse=True)
print(animals);print(mountains)


class INT:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def Add(self):
        print(self.x+self.y)

Int = INT(3,4)
Int.Add()

class Cat:
    def meow(self):
        print("야옹 야옹~~~")
    def info(self):
        self.name = "나비"
        self.color = "검정색"
        print("고양이 이름은",self.name,"색깔은",self.color)
cat1=Cat()
cat2=Cat()
cat1.meow()
cat2.info()

class Cat:
    def __init__(self,name='나비',color='흰색'):
        self.name = name
        self.color = color
    def info(self):
        print("고양이 이름은",self.name,"색깔은",self.color)

cat1=Cat("네로","검정색")
cat2=Cat("미미","갈색")
cat3=Cat()

cat1.info()
cat2.info()
cat3.info()

class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("이름은",self.name,"나이는",self.age)
    def call(self):
        print(self.name,"를 호출합니다.")
    def __str__(self):
        return "{}나이 {}세" .format(self.name,self.age)

person=Human("영희",25)
person.info();person.call();print(person)
guy=Human("홍길동",27)
guy.info();guy.call();print(guy)

lst1=[1,2,3]
lst2=[1,2,3,4]

if lst1 is lst1:
    print("lst1,lst1은 같은 인스턴스입니다.")
if lst1 == lst2:
    print("lst1,lst2의 데이터 값은 동일하며")
    if lst1 is lst2:
        print('lst1과 lst2는 같은 인스턴스입니다.')
    else:
        print("하지만 lst1과 lst2는 다른 인스턴스입니다.")

class Vector2D:
    def __init__(self,x,y):
        self.x =x
        self.y =y
    
    def __add__(self,other_vec):
        return Vector2D(self.x+self.y,other_vec.y+other_vec.x)

    def __sub__(self,other_vec):
        return Vector2D(self.x-self.y,other_vec.x-other_vec.y)
    
    def __neg__(self):
        return "({},{})" .format(-self.x,-self.y)

    def __str__(self):
        return "({},{})" .format(self.x,self.y)

v1=Vector2D(30,40)
v2=Vector2D(10,20)
print("v1=",v1,"v2=",v2)
v3 =v1+v2
print('v1+v2=',v3)
v4=v1-v2
print('v1-v2=',v4)
print('-v1=',-v1,'-v2=',-v2)


class Circle:
    PI=3.14
    def __init__(self,name,radius):
        self.name=name
        self.radius=radius
    def area(self):
        return Circle.PI*self.radius**2

c1=Circle("C1",4)
c2=Circle("C2",6)
c3=Circle("C3",5)
print(c1.area(),c2.area(),c3.area())
print(c1,c2,c3)
print("c1의  속성들:" ,c1.__dict__)
print("c1의 name 변수 값:" ,c1.__dict__['name'])
print("c1의 radius 변수 값:" ,c1.__dict__['radius'])



class Circle:
    def __init__(self,PI,name,radius):
        self.PI=PI
        self.name=name
        self.radius=radius
    def area(self):
        return self.PI*self.radius**2

c1=Circle(3.14,"C1",4)
c2=Circle(3.14,"C2",6)
c3=Circle(3.1415,"C3",5)
print("두번째",c1.area(),c2.area(),c3.area())


class Circle:
    def __init__(self,PI,name,radius):
        self.PI=3.14
        self.name=name
        self.radius=radius
    def area(self):
        return self.PI*self.radius**2

c1=Circle(3.14,"C1",4)
c2=Circle(3.14,"C2",6)
c3.PI=3.1415
c3=Circle(3.1415,"C3",5)
print("3번째",c1.area(),c2.area(),c3.area())

class Circle:
    def __init__(self,PI,name,radius):
        self.PI=3.14
        self.name=name
        self.radius=radius
    def area(self):
        return self.PI*self.radius**2

c1=Circle(3.14,"C1",4)
c2=Circle(3.14,"C2",6)
c3=Circle(3.14,"C3",5)
c3.PI=3.1415
print("4번째",c1.area(),c3.area())

class Circle:
    def __init__(self,PI,name,radius):
        self.PI=3.14
        self.name=name
        self.radius=radius
    def area(self):
        return self.PI*self.radius**2

c1=Circle(3.14,"C1",4)
c2=Circle(3.14,"C2",6)
c3.PI=3.1415
c3=Circle(3.14,"C3",5)

print("4번째",c1.area(),c3.area())

class Person:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    def name(self):
        return self.firstname +" "+self.lastname

class Employee(Person):
    def __init__(self,firstname,lastname,staffID):
        Person.__init__(self,firstname,lastname)
        self.staffID=staffID
    def info(self):
        return "Employee: " +self.name()+","+str(self.staffID)

class Employor(Person):
    def __init__(self,firstname,lastname,position):
        super().__init__(firstname,lastname)
        self.position=position
    def info(self):
        return "Employor: "+self.name()+","+ self.position

worker=Employee("Sherlock",'Gmones',1111)
cfo=Employor('Juju','Kim',"CFO")

print(worker.info())
print(cfo.info())

class Person:
    def __init__(self,firstname,lastname):
        self.firstname =firstname
        self.lastname = lastname
    def __str__(self):
        return self.firstname+self.lastname

class Employee(Person):
    def __init__(self,firstname,lastname,staffID):
        super().__init__(firstname,lastname)
        self.staffID =staffID
    def __str__(self):
        return "Employee: "+super().__str__()+","+str(self.staffID)

worker=Employee("Sherlock",'Gmones',1111)
print(worker)

class UndefinedVehicle(Exception):
    def __str__(self):
        return "정의되지 않은 탈 것입니다."
while True:    
    try:
        vehicle =input("자전거,오토바이,자동차 중 하나를 선택하시오 : ")
        if vehicle not in ['자전거','오토바이','자동차']:
            raise UndefinedVehicle
    except UndefinedVehicle as e:
        print(e)
    sel=input("종료는 n")
    if sel =='n':
        break
#비교 연산자에 해당하는 특수 메소드르르 이용하여 두 벡터의 크기를 비교하는 프로그램을 작성하시오
#v1이 (30,40)이고 v2가 (10,20)이라고 가정하면 다음과 같은 결과가 나타나도록 출력문을 작성하여라
# v1 > v2 =True
# V1 >= v2 =True
# v1 < v2 =False
# v1 <= v2 =False

class Better:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "({},{})" .format(self.x,self.y)
    def __gt__(self,other_vec):
        return self.x>other_vec.x and self.y>other_vec.y
    def __ge__(self,other_vec):
        return self.x>=other_vec.x and self.y>=other_vec.y
    def __lt__(self,other_vec):
        return (self.x<self.y and other_vec.x<other_vec.y)
    def __le__(self,other):
        return (self.x<=other.x and self.y<=other.y)
    def eq(self,other):
        return (self.x == other.x and self.y ==other.y)

v1 =Better(30,40)
v2 =Better(10,20)
print("v1 > v2 =",v1>v2)
print("v1 >= v2 =",v1>=v2)
print("v1 < v2 =",v1 <v2)
print("v1 <= v2 =",v1.__le__(v2))
print("v1 == v2 =",v1.__eq__(v2))
print("v1 == v2 =",v1.eq(v2))
print("v1 == v2 =",v1==v2)




class uv:
    def __init__(self,x,y):
        self.x =x
        self.y= y
    def __eq__(self,other_vec):
        return self.x == other_vec.x or self.y ==other_vec.y
    def __str__(self):
        return "({},{})" .format(self.x,self.y)
    def __add__(self,other_vec):
        return uv(self.x+other_vec.x,self.y+other_vec.y)
u=uv(0,0)
v=uv(1,0)

print("u==v(or)",u==v)
print("u+v=",u.__add__(v))


class Rect:
    def __init__(self,width,height):
        self.width =width
        self.height =height

r1 = Rect(100,200)
print(r1.__dict__)
print(r1.__dict__['width'])