#chapter 4   help() 解釋functio作用
#定義自己的function -> def
def add(a, b) :
    print(a + b)

add(1, 2)

#local variable global varable 
a = 5 #global varable 
def f1():
    x = 2 #f1 local variable
    y = 3 #f1 local variable
    print(x, y, a)
f1() #2 3 5

 #parameter (input) = local variables in function
a = 25
def change(n):
    #n = a (copy by value) => n = 25
    n = 10

change(a)
print(a) #25

#
a = [1, 2, 3, 4]

def change(lst):
    """change the value"""  #輸入help(change)可以查看到這個註解
    #lst = a (copy by reference) lst 指向 a
    lst[0] = 100 # a = [100, 2, 3, 4]

change(a)

print(a)  #[100, 2, 3, 4]

#change copy by value global variables
a = 10
def change(n):
    global a
    a = 25

change(a)
print(a) #25

#keyword argument
def exp(a, b):
    return a ** b
print(exp(a = 2, b = 3))

#list is positional argument
#reverse = False is keyword argument
list = [4, 6, 3, 1, 2]
print(sorted(list, reverse = False))  #[1, 2, 3, 4, 6]
print(sorted(list, reverse = True)) #[6, 4, 3, 2, 1]

#default argument 預設參數
def sum(a = 1, b = 0):
    return a + b
print(sum()) # 1  

# def sum(a = 1, b):
#     return a + b
# print(sum(10)) #non-default argument follows default argument


#arbitrary任意  number of argument
#args kwargs 可以放在一起
def sum(*args):
    print(args) 
    print(type(args)) #tuple
sum(1, 2, 3, 4, 5)   #(1, 2, 3, 4, 5)

#arbitrary *args
def sum(*args):
    result = 0
    for number in range(0, len(args)):
        result += args[number]
        print(f"The result is {result}") #The result is 1 3 6 10 15
    return result
print(sum(1, 2, 3, 4, 5)) # 15

#keyword args  
def function(**kwargs):
    print(kwargs) #dict
    print(type(kwargs))
function(name = "kuo", age = "26", address = "taichung")

#**kwargs
def function(**kwargs):
    print("{} is now {} years old".format(kwargs["name"], kwargs["age"]))
function(name = "kuo", age = 26, address = "taichung") #kuo is now 26 years old


#以上兩者可以放在同一function中
def func(*args, **kwargs):
    print("i like to eat {} {}".format(args[1], kwargs["food"]))
func(1, 2, 3, name = "KUO", food = "eggs") #i like to eat 2 eggs
 
 # 1. normal argument
 # 2. default argument
 # 3. *args
 # 4. **kwargs

def func(p1, p2, p3 = "three", *args, **kwargs):
    print(p1, p2, p3, args, kwargs)
func(1, 2, 3, 4, 5, x = 1, y = 2) # 1 2 3 (4, 5) {'x': 1, 'y': 2}
func(1, 2, 3, 4, x = 4) # 1 2 3 (4,) {'x': 4}
func(1, 2, 3) #1 2 3 () {}
func(1, 2) # 1 2 three () {}

# higher order function
def high(fn):
    fn()

def low():
    print("Hello from low")

high(low)

#map function   map(function, iterables) 必須return值
def square(num):
    return num ** 2
 
list = [-10, 2, 3, 5]
for item in map(square, list):
    print(item) # 100, 4, 9 ,25

# filter function filter(func, iterable) function true return
def even(num):
    if (num % 2 == 0 ):
        return num % 2 == 0
    #     return True
    # else:
    #     return False
list = [2235123, 126123, 765432] 
for item in filter(even, list):
    print(item) #765432 回傳true的數字


#lambda expression = anonymous function 
# lambda input1, input2 , ....: operation
result = (lambda x: x ** 2)(5)
print(result) # 25

myTuple = (lambda x, y: (x + y, x - y))(15, 30)
print(myTuple[0]) #45
print(myTuple[1]) # -15
print(myTuple) # (45, -15)

# lambda x:執行程式1 if 條件1 else 執行程式2 if 條件2 else 執行程式3



#scope
#lEGB local, enclosing, global, bulit-in 

name = "will"

def greet():
    name = "grace"

    def hello():
        print("hello, my name is " + name) #name 由內往外找
    hello()
greet() # hello, my name is grace


############
name = "will"

def greet():
    name = "grace"
def hello():
    print("hello, my name is " + name) #name 由內往外找

greet()
hello() #hello, my name is will


#local
a = "hello"

def change():
    print(a) #create "a" local variable
    a = 25 # a variable assignment
change() #UnboundLocalError 

