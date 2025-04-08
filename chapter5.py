# I/O python
#file 語法

file = open("myFile.txt")
print(file.read(5)) #roses 文件前五個字
print("-----------")
print(file.read(5)) # are   (roses後面五個字)



#file.seek(offset) 重置文件讀取的位置
file = open("myFile.txt")
print(file.read()) #read 會回傳一個string
file.seek(0)
print(file.read())

#file.readline() return a list
#read.lines 如果遇到很多行的  ram可能會被占用光
file = open("myFile.txt")
print(file.readlines())  # 讀整行文件['roses are red\n', 'sky is blue\n', 'syntax error in line 32\n']

#可用迴圈 readlines
file = open("myFile.txt")
for line in file.readlines(): 
    print(line) #roses are red sky is blue syntax error in line 32

# encoding
file = open("myFile.txt", encoding = "UTF-8") #cp950 default  or UTF-8

#with statment
with open("myFile.txt") as my_file:
    all_content = my_file.read()
    print(all_content)

#mode()-> read 'r', append 'a', write 'w', create 'c'
with open("myFile.txt", mode = "a") as my_file:
    my_file.write("append test") #txt 檔中會出現


with open("myFile.txt", mode = "w") as my_file: #w 複寫掉txt檔
    my_file.write("write test") #txt 檔會被覆寫成這句 要換行就加\n


#remove 檔案
import os
os.remove("index.html") #刪除

#remove 資料夾
import os
os.rmdir("folder") #刪除資料夾 (裡面不能有其他檔案)
# 1. os.walk() 遍歷整個資料夾
# 2. shutil 直接刪除

#user input
user_input = input("how old r u")
print()


#serialize and deserialize  兩台電腦需要交換資料 serialize轉換成二進位之後 deserialize 轉成需要的資料 
#pickle  & sheleve
import pickle

x = 10
y = [1, 2, 3, 4]

with open("picle_file", "wb") as p_file: # wb = write binary rb = read binary
    pickle.dump(x, p_file) 
    pickle.dump(y, p_file)

import pickle
with open("picle_file", "rb") as p_file:
    print(pickle.load(p_file))# 10
    print(pickle.load(p_file)) # [1, 2, 3, 4] 讀出文件內容



#pickle
import pickle

x = None
y = None
my_list = None 

def restore_data():
    global x, y, my_list
    with open("my_picle_file", "rb") as p_file:
        data = pickle.load(p_file)
        x = data['x']
        y = data['y']
        my_list = data['my_list']

restore_data()
print(x, y, my_list) # 10 100 [1, 2, 3, 4, 5, 6]

# stroe資料
import pickle
x = 10
y = 100
my_list = [1, 2, 3, 4, 5, 6]

def save_data():
    global x, y, my_list
    data = {'x': x, 'y': y, 'my_list': my_list}
    with open("my_picle_file", "wb") as p_file:
        pickle.dump(data, p_file)

save_data()


#shelve
import shelve

integer1 = [1, 2, 3, 4, 5]
integer2 = [6, 7, 8, 9, 10]
integer3 = [11, 12, 13, 14, 15]

with shelve.open("shelf-example", 'c') as shelf:
    shelf['ints1'] = integer1
    shelf['ints2'] = integer2
    shelf['ints3'] = integer3

#讀取shelf
import shelve

with shelve.open("shelf-example", 'r') as shelf:
    for key in shelf.keys():
        print(key)
    print(shelf['ints2']) #ints1
# ints2
# ints3
# [6, 7, 8, 9, 10]
