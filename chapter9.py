# first class objects
# 1. function 可以指派給一個變數
# 2. 一個function 可以是另一個function的augument
# 3. return另一個function
def hello():
    def greet():
        print("greet")
    return greet
welcome = hello()
welcome() #greet


# -----------------------
def hello(name):
    def greet(another_name):
        print("hello," + another_name)

    def bye(another_name):
        print("bye," + another_name)

    if name == "greet":
        return greet #function
    else:
        return bye
welcome = hello("greet")
goodbye = hello("something")
print(welcome)
welcome("kuo")
goodbye("ke")
# 4. 可以放進list, tuple, dictionary


# decorator
def new_decorator(original_func):
    def wrap_func():
        print("Here is before the original function")
        #print(original_func.__name__)
        original_func()
        print("Here is after the original function")
    return wrap_func


# use decorator improve function
@new_decorator
def func_needs_decorator():
    print("i am a function thats needs decotrator")


func_needs_decorator()
# decorated_function = new_decorator(func_needs_decorator)

# # Here is before the original function
# # i am a function thats needs decotrator
# # Here is after the original function
# decorated_function() 


#generator
# yield
def cube(n):
    result = []
    for x in range(n):
        result.append(x ** 3)
    return result

for i in cube(10):
    print(i) # # 1 8 27 ... 729

###
def cube(n):
    for x in range(n):
        yield x ** 3
for ele in cube(10):
    print(ele) # 1 8 27 ... 729

# yield from
def sub_generator(x):
    for i in range(x):
        yield i ** 2

def gen(y):
    yield from sub_generator(y)

for num in gen(15):
    print(num)# 0 1 4 9 ... 196


# iteration循環:(for...in), iterable, iterator
# iterable - 1. __iter__() method return iterator 2. implements __getitem__()
# ant generator is an iterator


# 1.
class Something:
    def __iter__(self): #implement iter
        yield 5
        for x in range(1, 4):
            yield x

s = Something()
# s is an iterable
# iter(iterable) returns an iterator
print(iter(s)) # <generator object Something.__iter__ at 0x0000018CEA57AD60>
for i in s:
    print(i) # 5 1 2 3


# 2. 
class Building(object):
    def __init__(self, floors):
        self.__floors = [None] * floors # [None, None, None....]


    def __setitem__(self, floor_number, data): # 用index  dictionary設定
        self.__floors[floor_number] = data

    def __getitem__(self, floor_number):
        return self.__floors[floor_number]
    
building1 = Building(4)
building1[0] = 'Reception'  # 在__setitem__那邊帶入 floor_number = 0  data = Reception
building1[1] = 'Corp' 
building1[2] = 'Store' 

for thing in building1:
    print(thing) #Reception, Corp, Store, None


# iterator 滿足 1.__iter__() return self, 2. implement __next__()  檢查是否是iterator 有iter next就是
# iterator is a subset of iterable
x = [1, 2, 3]
#print(dir(x)) # 沒有next 不是iterator
#但是有iter 他是iterable

list_iterator = iter(x)
print(next(list_iterator)) # 1
print(next(list_iterator)) # 2 
print(next(list_iterator)) # 3 就是   for i in x   print(i)


# self made iterator
class MyIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.max_num:
            value = self.index
            self.index += 1
            return value
        else:
            self.index = 0
            raise StopIteration
        
MyIterator = MyIterator(5)
for item in MyIterator:
    print(item) # 0 1 2 3 4



class test():
    def __init__(self,data = 1):
        self.data = data

    def __iter__(self):
        return self
    def __next__(self):
        if self.data > 5:
            raise StopIteration
        else:
            self.data+=1
            return self.data

for item in test():
    print(item)


# stdin, stdout pipe
# > means overwrite
# >> means append
# < means read
