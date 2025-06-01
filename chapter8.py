# error handling
# exception

#LBYL approach
def divide_1(x, y):
    if y == 0:
        print("cant divide by 0")
        return None
    else:
        return x / y
    
#EAFP (easier to ask forgiveness than permission) faster than LBYL, reduce race conditions
def divide_2(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("cant divide by 0")
        return None
    

try:
    result = 10 + 10
except:
    print("Error")
finally: #不管如何都會執行
    print(result)


#
def ask_for_int(): #持續問直到user輸入數字
    while True:
        try:
            result = int(input("insert a number"))
        except:
            print("Invalid")
        else: #will run if no exception
            print("OK")
            return result
ask_for_int()


# raise exception
# exception_test, exception_main

#order  of exception
# 如果第一個exception就可以handle錯誤 第二個exception就不會執行到
 
# guard clauses and exception handling
def divide(a, b):
    if type(a) != int or type(b) != int:
        raise ValueError("invalid")
    
    if b == 0:
        raise ZeroDivisionError("cannot be zero")
    
    return a / b

try:
    # print(divide(10, "hello")) # invalid
    # print(divide(10, 0)) # cannot be zero 
    print(divide(6, 3)) #2.0
except Exception as e:
    print(e)


# pylint 找bug錯誤 改善程式
# pip install pylint 
#terminal輸入 pylint programname.py -r y

  
# unit testing 單元測試

