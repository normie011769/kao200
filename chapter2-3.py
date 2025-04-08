list = [1, 2, 5, 7]
for i in list :
    print(i ** 2) # 1 4 25 49

# a list of tuples  tuple packing
for a, b in [(1, 3), (5, 6), (6, 7)] :
    print(a + b) # 4 11 13

#dic (keys)
dic = {"name": "kuo", "age": 26}
for i in dic.values() :
    print(i) #kuo 26
for j in dic.items() :
    print(j)  #('name', 'kuo') #('age', 26)
for key, value in dic.items() :
    print(f"The key is {key}")  #The key is name #The value is kuo
    print(f"The value is {value}") #The key is age  #The value is 26


#while loop  while(condition)
 
#pass: 略過執行的程式
for i in "how" : #原本會跑三次
    pass
print("hi") #只會跑一次

# break 
for i in "123456" :
    if i == "4":
        break 
    else :
        print(i) #123
# continue 跳過這次
for i in "123456" :
    if i == "4":
        continue
    else :
        print(i) #12356

#for range[start, stop, step ](知道要執行幾次)
for i in range(0, 2) :
    print(i) #0 1

#enumrate
for counter, letter in enumerate("how r u today") :
    if (counter < 10) :
        print(letter) #how r u to


# zip() function  根據長度最短的為主 
x = [1, 2, 3] #只會到第3
y = ['A', 'B', 'C', 'D'] 
for tuple in zip(x, y) :
    print(tuple) #(1, 'A') (2, 'B') (3, 'C')



#COMPREHENSION (list dic set 不含tuple)建立新sequences 
#new_list = [operation for variable in original_list  if condiction]
x = [1, 2, 3, 4]
square_x = [item ** 2 for item in x] # if item > 2 square_x會得到 [9, 16]
print(square_x) #[1, 4, 9, 16]


#dictionary comprehension 
#new_dict = [key:value(operation) for variable in original_dict if condition]
x = [1, 2, 3, 4]
square_x_dict = {item: item ** 2 for item in x} #if item > 2 square_x_dict = {3:9, 4: 16}
print(square_x_dict) #{1: 1, 2: 4, 3: 9, 4: 16}


#set comprehension
#new_set = {operation for variable in original_set if condition}
x = [1, 2, 3, 4]
square_x_set = {item ** 2 for item in x} #if item > 2 square_x_set = {3:9, 4: 16}
print(square_x_set) #{16, 1, 4, 9} 因為是集合 順序不重要


#generator comprehensions
x = [1, 2, 3, 4]
x_square_gene = (item ** 2 for item in x)
for i in x_square_gene :
    print(i) # 1, 4, 9, 16


