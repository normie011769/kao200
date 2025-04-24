# 物件導向
# class template for creating objects
from abc import ABCMeta, abstractmethod


class Robot:
    ingredient = "metal"  # 產生之robot要檢查ingredient 只要來class這 檢查就好
    # 在class 可以定義doctring
    """robot class is for creating robots"""  # doc

    # constructor
    def __init__(self, inputname, inputage):  # self 要加 method 會自動略過
        self.name = inputname  # self.name 是另外的變數跟 上面inputname不同
        self.age = inputage
        # self.ingredient = "metal" #會占用記憶體 每次產生一個 robot 都會自己產生ingregient 占用

    # 定義Method definition
    def walk(self):
        print(f"{self.name} is walking")

    def sleep(self, hours):
        print(f"{self.name} is going to sleep for {hours} hours")

    def greet(self):
        print(
            f"Hi, my name is {self.name}, and my ingredient is {self.__class__.ingredient}")  # 用.__class__是怕以後若class 名字修改 仍可使用


my_robot1 = Robot("Kuo", 26)
my_robot2 = Robot("Daniel", 27)
# print(my_robot1.__doc__) #查看doc那段
print(my_robot1.name)  # kuo
print(my_robot1.age)  # 26
my_robot1.walk()  # Kuo is walking
my_robot1.greet()  # Hi, my name is Kuo, and my ingredient is metal
# print(my_robot1.ingredient) # metal

# 以下三種都可以輸出"metal"
# print(my_robot1.ingredient)
# print(Robot.ingredient)
# print(my_robot1.__class__.ingredient)  #best 作法


# class attribute, static method, class method
# static method
class Robot:
    ingredient = "metal"

    def __init__(self, inputname, inputage):
        self.name = inputname
        self.age = inputage

    @staticmethod  # decorator
    def greet():  # 不需要self
        print("A robot says hi")


my_robot1 = Robot("Kuo", 26)
my_robot2 = Robot("Daniel", 27)

Robot.greet()  # A robot says hi
my_robot1.__class__.greet()  # A robot says hi


# class method  ; cls = stands for class

class Circle:  # 若改circle為circles 這邊會找不到
    pi = 3.14159
    all_circle = []

    def __init__(self, radius):
        self.radius = radius
        self.__class__.all_circle.append(self)

    def area(self):
        return self.__class__.pi * (self.radius ** 2)

    @staticmethod
    def total_area():
        total = 0
        for circle in Circle.all_circle:  # 若改circle為circles 這邊會找不到 也能用__class__
            total += circle.area()
        return total

    @classmethod
    def total_area2(cls):
        total = 0
        for circle in cls.all_circle:
            total += circle.area()
        return total


c1 = Circle(1)
c2 = Circle(10)
# 317.30059  #如果class circle改名為 circles 這個print會出錯
print(c1.__class__.total_area())   # 317.30059
print(c1.__class__.total_area2())  # 317.30059
print(c1.area())  # 3.14159


# inheritance
class People:
    def __init__(self, name, age):  # 設定class的屬性(Attribute)  產生實例後可以操作的函數初始化要加self 方法也是
        self.name = name  # self.name是一個變數 後面的name是給定的屬性
        self.age = age

    def sleep(self):
        print(f"{self.name} is sleeping")

    def eat(self):
        print(f"{self.name} is eating")


class Student(People):  # (People) 表示繼承people裡面的所有屬性
    def __init__(self, name, age, student_id):  # constructor 去執行上面people的name age
        # People.__init__(self, name, age)
        # 要存取父類別的資源 寫上父類別的初始化函數    People -> super()  免去class people改名時 繼承的命名問題
        super().__init__(name, age)
        # super(指父類別)沒有self 繼承
        self.student_id = student_id

    # overwritting 上面的eat method
    def eat(self, food):
        print(f"{self.name} is eating {food}")


student1 = Student("Kuo", 25, 16673)
student1.sleep()  # Kuo is sleeping
student1.eat("chicken")  # Kuo is eating chicken


# multiple inheritance
class C:
    def do(self):
        print("hello from class c")


class D:
    def do_1(self):
        print("hello from class d")


class A(C, D):  # 多重繼承
    pass


a = A()
a.do()  # hello from class c
a.do_1()  # hello from class d


#
class E:
    pass


class F:
    def do_stuff(self):
        print("hello from f")


class G:
    def do_stuff(self):
        print("hello from g")


class B(E, F):
    pass


class C:
    def do_stuff(self):
        print("hello from c")


class D:
    pass


class A(B, C, D):
    pass


a = A()
a.do_stuff()  # hello from f  #method resolution order(MRO) 使用DFS找繼承的Do_stuff
print(A.mro())  # A B E F C D


# 抽象類別
# 父類別不實作函式中的程式碼，由子類別實作
# 抽象類別不能建立實例(instance)
# 如果子類別沒有實作 會有錯誤
# 抽象類別尚未實作的函式 稱為抽象函式

# 抽象:可讓父類別先不實作


class Employee(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def showId():  # 每個子類別有不同的showid方式，由子類別自行實作
        pass


class Teacher(Employee):
    def __init__(self, name, age, tid):
        super().__init__(name, age)
        self.tid = tid

    def showId(self):
        print(f"My Teacher ID is {self.tid}")


tea = Teacher("Mary", "25", "t123")
tea.showId()


# classname.mro() > list
# classname.__mro__ > tuple

# private attribute nad method
class Robot:
    def __init__(self, name):
        self.name = name
        # private property 不能直接用
        self.__age = 25

    def greet(self):
        print(f"Hi  i am {self.__age} years old")

    # getter setter
    def get_age(self):
        return self.__age

    def set_age(self):
        self.__age += 15  # 設定__age


robot1 = Robot("KUO")
robot1.greet()  # Hi  i am 25 years old
robot1.set_age()
print(robot1.get_age())  # 40
# print(robot1.age) #AttributeError: 'Robot' object has no attribute 'age'


# private method
class Robot:
    def __init__(self, name):
        self.name = name
        # private property 不能直接用
        self.__age = 25

    def __this_is_private(self):
        print("hello from private")

    def greet(self):
        print("hi i am a robot")
        self.__this_is_private()  # "hello from private"


robot1 = Robot("KUO")
# robot1.greet()  # hi i am a robot  hello from private

# AttributeError: 'Robot' object has no attribute '__this_is_private'
# robot1.__this_is_private()


robot1._Robot__this_is_private()  # hello from private

print(robot1._Robot__age)  # 25 # 因self.__age = 25

# property decorator


class Employee:
    def __init__(self):
        self.income = 0
        # self.__tax = 0

    def earn_money(self, money):
        self.income += money
        # self.__tax += self.income * 0.05

    # def get_tax(self):
    #     return self.__tax
    @property
    def tax_amount(self):
        return self.income * 0.05

    @tax_amount.setter
    def tax_amount(self, tax_number):
        self.income = tax_number * 20  # 根據稅金倒推薪水


kuo = Employee()
kuo.earn_money(300)
print(kuo.tax_amount)  # 15.0 #tax_amount 是虛擬property
# tax_amount 是read-only
kuo.tax_amount = 500
print(kuo.income)  # 10000


# mighty hash function  hash -> 把一個值換成另一個值
# hashable object = string, ints, bool, float, tuple 不是hashable= list, dict, set

a = 100
b = "this is a string"
c = 1.0
d = True
e = None
print(hash(a), hash(b), hash(c), hash(d), hash(e))
# 100 -2799564455701229302 1 1 -9223363242583198771

print(hash((1, 4, 7, 11)))  # 943204701236206362 set hashable(固定長度的值)

# good hash function hash值不應該儲存，因為每次都會不同
# bcrypt, SHA-256, RSA ALGO
# 1. consistent 兩次hash都是一致性的
print(hash("hello"))  # -5107158841116020759
print("do another")
print(hash("hello"))  # -5107158841116020759
# 2. distributed evenly  小改變就是讓hash結果output完全不一樣
print(hash("look at me!"))  # -6746510592009028322
print(hash("look at me!!"))  # 2916102328196655743
print(hash("look at me!!!"))  # -7024435388606774112
# 會在每次執行新的round時 結果都會不一樣


# 3. not invertible 無法反推至原本的值


# hash and eq
class Robot:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    # define a private method

    def __key(self):
        return (self.name, self.age, self.address)
    # implement __hash__() function

    def __hash__(self):
        return hash(self.__key())

    # eq (equal) method
    def __eq__(self, other):
        if isinstance(other, Robot):  # 判斷 other是不是robot calss
            return self.__key() == other.__key()
        return NotImplemented

    def __len__(self):
        return self.age

    def __str__(self):  # 給user看
        return f"{self.name} is now {self.age} years old"

    def __repr__(self):  # for debugging purpose
        return f"name : {self.name}, age:{self.age}, address:{self.address}"

    def __add__(self, other):
        if isinstance(other, Robot):
            return self.age + other.age
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Robot):
            return self.age > other.age
        return NotImplemented


robot = Robot("Kuo", 26, "Taiwan")
dictionary = {robot: "Kuo"}
print(dictionary[robot])  # Kuo

robot1 = Robot("Kuo", 26, "Taiwan")
robot2 = Robot("Ke", 27, "Taiwan")
print(robot1 == robot2)  # False 因robot1及robot2 記憶體位置不同
# 若eq mtehod 兩者相同則回傳true
print(len(robot1))  # 26
print(robot1)  # Kuo is now 26 years old
print(repr(robot1))  # name : Kuo, age:26, address:Taiwan
print(robot1 + robot2)  # 53
print(robot1 > robot2)  # False

# dunder (magic) method
# double underscore __


class Empolyee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def hello(self):
        print(f"{self.first} say hello")

    def mydeposit(self):
        self.__deposit = 20000
        print(f"i have {self.__deposit}")


tiny = Empolyee("tiny", "mury", 50000)
tiny.hello()
tiny.mydeposit()
tiny.__deposit
