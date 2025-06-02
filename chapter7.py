#Mmodules and packages
#自建自己的 modules
from another_module import one_func, two_func

one_func() #This is my custom module
two_func() #This is my second custom module

#import package裡面的東西
from myPackage import some_code
from myPackage.sub_Package import sub

some_code.some_code() #This is some code
sub.sub_code() #This is sub code



#different way of import
# 1. import moduleName
# 2. import moduleName as sdomething
# 3. form moduleName import *(所有)   -> 容易忘記是不是ˇ同一個module
# 4. from moduleName import oneFunction, anotherFunction

import random as rd #會導致程式碼混雜  (as 方法最為推薦)

print(rd.randint(0, 5))
#modules in python are objects

# from mod import hello
# from mod2 import hello   若執行hello 後面hello會覆蓋前面 因此需使用as去別名更好



#module searching
# 1. 放在統一路徑 sys.path
# 2. 放在main program裡
# 3. 修改sys.path
    # 3.1 user sys.path.append()
import sys
sys.path.append("c:/....")
    # 3.2 修改環境變數 修改sys.path
    # 3.3 sys.path裡任一資料夾 產生 sitecustomize.py
import sys
print(sys.path) # 到'C:\\Python39\\lib\\site-packages' 產生
#sitecustomize.py 內容:

##import site
##site.addsiterdir('C:\\Python39\\lib\\site-packages\\test)
#print(sys.path) 可以看到產生的檔案路徑


# Nmaespace 命名空間
# LEGB Rules : Local, Enclosing, Global, Built-in
#遵循此規則進行變數搜尋，只要變數被找到搜尋行動就會停止，如果沒有找到就會出現Error。

# 1. built-in namespace
# 2. global namespace
# 3. local namespace  globals(), locals() -> return doctionaries
import sys
x = 10

#以上都會改變global namespace 
#如果定義str = 10 or int = 20 之類的， python會把之後的str()都等於10 會複寫builtin裡面的值
print(globals()) #return global namespace as a dictionary


# if __name__ =="__main__"   如果有one.py 和 two.py one.py 輸出function this is one  two.py則import one.py的function
#此時 在two.py裡面會出現 this is one 和 this is two

#if __name__ =="__main__"  如果在one.py 只有在one.py執行才會跑 如果在two.py跑 one.py裡面的if __name__ =="__main__" 這段就不會執行



#PyPI(python package網站) and Pip(package management software) 做爬蟲or AI常用到
# pip install -upgrade numpy 升級
# pip install numpy ==1.22.2
# pip install numpy >=1.22.2
# # pip freeze 檢查版本



