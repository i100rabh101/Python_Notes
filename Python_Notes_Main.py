"""
- Synatx means the write way to write a program.

# Pyton Cons
- Simple and Easy
- Free & Open Source 
- High level language


# Best Prac
- Use short and meaningful variable names
- Use appropraite comments
- Simple instructions


# Python Charater Set
- A-Z
- a-z
- 0-9
- All Special Symbols
- Whitespaces

# Data Types
- int
- float     
- string
- boolean
- none



# Pointers
- Cant use reserved words as variable names
- Variable names are case sensitive
- Variable names should not start with a number
- python is implicitly typed language
"""


print("helloworld!", "i am 20.")
# helloworld! i am 20.
print(35+234)
# 269


"""Variable Declaration"""
name = "John"
surname = '''doe'''
age = 20
male = True
address = None
print(f"my name is {name} {surname} and my age is {age}.")
# my name is John doe and my age is 20. 
print(type(name))
# <class 'str'>
print(type(age))
# <class 'int'>
print(type(male))
# <class 'bool'>
print(type(address))
# <class 'NoneType'>


"""Arithmetic Operators"""
a,b = 100,400
c = 130.89
sum = a + b - c
multiply = (a * b) * c
divide = a/b/c
integer_division = a//c
txt = "@"
remainder = 100 % 30
exponent = 2**3
print(sum)
# 369.11
print(type(sum))
# <class 'float'>
print(multiply)
# 5235599.9999999998
print(divide)
# 0.0019100007640003058
print(2*txt*3)
# @@@@@@@
print(integer_division, a/c)
# 0.0 0.7640003056001223
print(remainder)
# 10
print(exponent)
# 8


"""Input Function"""
fullname = str(input("Enter your full name: "))
rollno = int(input("Enter your roll number: "))
print(f"Your name is {fullname} and your roll number is {rollno}.")
# Your name is John Doe and your roll number is 123456.



food = input("Enter your food: ")
print("sweet") if (food == "cake") or (food == "jalebi") else print("sour")
# Enter your food: cake
# sweet


salary = float(input("Enter your salary: "))
tax = salary*(0.1,0.2) [salary <= 50000]
print(tax)
# Enter your salary: 60000
# 12000.0


"""Relational Operators"""
a = 5
b = 2
print(a == b) # False
print(a != b) # True
print(a > b) # True
print(a >= b) # True


"""Assignment Operators"""
num = 10
num += 5
print(num) # 15
num %= 5
print(num) # 0
num += 5
print(num) # 5
num **= 2
print(num) # 25


""""Logical Operators"""
a = 5
b = 2
print(not(a == b)) # True
print(( a==b ) and (a > b)) # False
print((a == b) or (a > b)) # True


"""Type Conversion"""
a = 5
b = "2"
print(type(b)) # <class 'str'>
b = int(b)
print(type(b)) # <class 'int'> 
sum = a + b
print(sum) # 7


"""Strings"""
# Strings are immutable in python.
str1 = "This is First Line.\nThis is Second Line."
print(str1)
# This is First Line.
# This is Second Line.
str2 = "This is First Line.\tThis is Second Line."
print(str2)
# This is First Line.     This is Second Line.   
len(str1) # 40
len(str2) # 40


"""String Functions""" 
str = "hello World!"
print(str.endswith("ld!")) # True
print(str.endswith("Hello")) # False
print(str.capitalize()) # Hello world! 
print(str) # hello world!   
print(str.find("o")) # 4
print(str.find("s")) # -1
print(str.count("o")) # 2


""""Indexing"""
str = "I am studying at apna college."
choose = str[5]
print(choose) # s
str[5] = "S"
# TypeError: 'str' object does not support item assignment
str = str.replace("s", "S")
print(str) # I am StUdying at apna college.


"""Slicing"""
str = "I am studying at apna college."
print(str[0:2]) # I 
print(str[0:5]) # I am
print(str[0:len(str)])
print(str[:5]) # I am
print(str[-5:-1]) # lege



"""If Else Statement"""
light = str(input("Enter the light color: "))
if (light == "red"):
    print("Stop")
elif (light == "green"):
    print("Go")
elif (light == "yellow"):
    print("Wait")
elif (light == "blue" and light == "orange"):
    print("Malfunctioned")
else:
    print("Light Broken")
# Enter the light color: green      
# Go


"""If Else Statement"""
A = int(input("A: "))
G = input("M/F: ")
if((A == 1 or A == 2) and (G == "M")):
    print("fee is 100")
elif((A == 3 or A == 4) or (G == "F")):
    print("fee is 200")
elif((A == 5) and (G == "M")):
    print("fee is 300")
else:
    print("no fee")
# A=2 & G=F
# fee is 200


"""Nested If Else Statement"""
age = int(input("Enter your age: "))
if (age >= 18):
    if (age >= 80):
        print("Cannot Drive")
    else:
        print("Can Drive")
else:
    print("Cannot Drive")
# Enter your age: 81
# Cannot Drive


"""Largest Number"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
if (num1 >= num2) and (num1 >= num3) and (num1 >= num4):
    print("Largest number is: ", num1)
elif (num2 >= num1) and (num2 >= num3) and (num2 >= num4):
    print("Largest number is: ", num2)
elif (num3 >= num1) and (num3 >= num2) and (num3 >= num4):
    print("Largest number is: ", num3)
else:
    print("Largest number is: ", num4)
# Enter first number: 5
# Enter second number: 5
# Enter third number: 15
# Enter fourth number: 20
# Largest number is:  20


"""Lists"""
# A single list can store different data types whereas an array can only store a single data type.
# Lists are mutable in python.
marks = [10, 20, 30, 40, 50]
print(marks) # [10, 20, 30, 40, 50]
print(marks[0]) # 10
print(marks[1:3]) # [20, 30]
print(marks[-3:-1]) # [30, 40]
print(len(marks)) # 5


"""List Methods"""
marks = [10, 50, 40, 20, 30]
print(type(marks)) # <class 'list'>
marks.append(60) 
print(marks) # [10, 50, 40, 20, 30, 60]
marks.insert(2, 70) 
print(marks) # [10, 50, 70, 40, 20, 30, 60]
marks.reverse()
print(marks) # [60, 30, 20, 40, 70, 50, 10]
marks.sort()
print(marks) # [10, 20, 30, 40, 50, 60, 70]
marks.sort(reverse=True)
print(marks) # [70, 60, 50, 40, 30, 20, 10]
list.remove(70)
print(marks) # [60, 50, 40, 30, 20, 10]
marks.pop(3)
print(marks) # [60, 50, 40, 20, 10]


"""List Question"""
# Write a program to take 3 movies as input from the user and store them in a list.
print("Enter your 3 favourite movies")
movies = []
movies.append(input("Enter your first movie: "))
movies.append(input("Enter your second movie: "))
movies.append(input("Enter your third movie: "))
print("Your favourite movies are: ", movies)
# Your favourite movies are:  ['Movie1', 'Movie2', 'Movie3']


"""List Question"""
# Write a program to check if a list is palindrome or not.
list = [10, 20, 30, 20, 10]
list2 = list.copy()
list2.reverse()
if list == list2:
    print("List is palindrome")
else:
    print("List is not palindrome")




"""Tuples"""
# Tuples are immutable in python.
# Tuples can store different data types.
marks = (20, 30, 50, 40, 10)
print(type(marks)) # <class 'tuple'>
print(marks[1]) # 30
marks[2] = 100
# TypeError: 'tuple' object does not support item assignment
print(marks[0:2]) # (20, 30)


"""Tuple Methods"""
marks = (20, 30, 50, 40, 10, 40)
marks.index(40) # 3  
marks.count(40) # 2


"""Dictionaries"""
# Dictionaries are mutable in python.
# Dictionaries store values in key-value pairs.
# They are unordered and key must be unique.
info = {
    "name": "myself",
    "age": 200,
    "subject": ["python", "java", "c++"],
    "marks": (20, 30, 40, 50),
    "ismale": True,
    12: 35.5
}
print(info) # {'name': 'myself', 'age': 200, 'subject': ['python', 'java', 'c++'], 'marks': (20, 30, 40, 50), 'ismale': True, 12: 35.5}
print(type(info)) # <class 'dict'>
print(info["name"]) # myself
print(info["marks"]) # (20, 30, 40, 50) 
info["name"] = "myself2"
info["surname"] = "itsme"
print(info) # {'name': 'myself2', 'age': 200, 'subject': ['python', 'java', 'c++'], 'marks': (20, 30, 40, 50), 'ismale': True, 12: 35.5, 'surname': 'itsme'}


"""Nested Dictionary"""
student = {
    "name": "John",
    "age": 20,
    "marks": {
        "python": 80,
        "java": 90,
        "c++": 85
    }
}
print(student["subject"]["python"]) # 80


"""Dictionaries Methods"""
student = {
    "name": "John",
    "age": 20,
    "marks": {
        "python": 80,
        "java": 90,
        "c++": 85
    }
}
print(student.keys()) # dict_keys(['name', 'age', 'marks'])
print(list(student.keys())) # ['name', 'age', 'marks']
print(list(student.values())) # ['John', 20, {'python': 80, 'java': 90, 'c++': 85}]
print(list(student.items())) # [('name', 'John'), ('age', 20), ('marks', {'python': 80, 'java': 90, 'c++': 85})]
print(student.get("name")) # John  ## preferred way to access value as doesn't give error if key not found
student.update({"surname": "Doe"})
print(student) # {'name': 'John', 'age': 20, 'marks': {'python': 80, 'java': 90, 'c++': 85}, 'surname': 'Doe'}


"""Dictionary Question"""
marks = {}
x = int(input("Enter your marks in physics"))
marks.update({"physics": x})
y = int(input("Enter your marks in chemistry"))
marks.update({"chemistry": y})
z = int(input("Enter your marks in maths"))
marks.update({"maths": z})
print(marks) # {'physics': 50, 'chemistry': 60, 'maths': 70}


"""Set"""
# Sets are unordered and unindexed.
# Each element is unique and immutable.
collection = {1, 2, 3, 4, 5, "hello", 2, "hello"}
print(collection) # {1, 2, 3, 4, 5, 'hello'}
print(type(collection)) # <class 'set'>
print(len(collection)) # 6
empty_set = set()
print(type(empty_set)) # <class 'set'>


"""Set Methods"""
collection = {1, 2, 3, 4, 5, "hello", 2, "hello"}
collection2 = {1, 3, 7, 5, "hello"}
collection.add(6)
collection.remove(2)
collection.add((7, "World", 8))
print(collection) # {1, 3, 4, 5, 6, 'hello', (7, 'World', 8)}
collection.pop() ## removes a random element from the set
print(collection) # {3, 4, 5, 6, 'hello', (7, 'World', 8)}
print(collection.union(collection2)) # {1, 3, 4, 5, 6, 7, (7, 'World', 8), 'hello'} ## combines two sets
collection.intersection(collection2) # {'hello', 3, 5} ## returns common elements in both sets
collection.clear()
print(collection) # set()


"""Loops"""
# Loops are used to repeat a block of code multiple times.
# There are two types of loops in python: while and for loop


"""While Loop"""
# A while loop is used to execute a block of code as long as the condition is true.
# Break statement is used to exit the loop.
# Continue statement is used to skip the current iteration and move to the next iteration.
i = 1
while i <= 5:
    print("hello", i)
    i += 1
print(i) 


"""Multiplication Table"""
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{num} * {i} = {num*i}")
    i += 1


"""While Question"""
i = 1
while i <= 10:
    print(i*i)
    i += 1


"""While loop Traverse Question"""
nums = [1, 2, 3, 4, 5]
i = 0
while i < len(nums):
    if (i == 2):
        i += 1
        continue
    print(nums[i])
    i += 1


"""While loop linear search"""
heroes = ["batman", "superman", "spiderman", "ironman"]
i = 0
x = "spiderman"
while i < len(heroes):
    if heroes[i] == x:
        print(f"found {x} at index {i}")
        break
    else:
        i += 1

    
"""While loop question"""
# Write a program to print the sum of first natural numbers.
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(f"The sum of first {n} natural numbers is: {sum}")


"""For Loop"""
# A for loop is used to iterate over a sequence (list, tuple, dictionary, set, or string).
# It is used when the number of iterations is known.
# The range() function is used to generate a sequence of numbers.


"""For loop traverse question"""
nums = [1, 2, 3, 4, 5]
for i in nums:
    print(i)


"""For loop question"""
str = "hello world!"
for i in str:
    print(i)
else:
    print("End of string")


"""For loop linear search"""
heroes = ["batman", "superman", "spiderman", "ironman"]
x = "spiderman"
for i in heroes:
    if i == x:
        print(f"found {x}")
        break 


""""Range()"""
for i in range(5):
    print(i) # 0 1 2 3 4
for i in range(5, 10):
    print(i) # 5 6 7 8 9
for i in range(5, 10, 2):
    print(i) # 5 7 9
for i in range(10, 0, -1):
    print(i) # 10 9 8 7 6 5 4 3 2 1


"""For and Range multiplication table"""
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num*i}")


"""Pass Statement"""
# The pass statement is a null statement in Python.
# It is used when a statement is required syntactically but no action is required.
# It is a placeholder for future code.
for i in range(5):
    pass ## do nothing
print("hello") # hello


"""For loop Factorial question"""
# Find the factorial of first natural numbers.
n = int(input("Enter a number: "))
fac = 1
for i in range(1, n+1):
    fac *= i
print(f"The factorial of {n} is: {fac}") 


"""Functions"""
# A function is a block of code that only runs when it is called.
def hello():
    print("hello world!")
hello() # hello world!

def SumCalculator(a, b):
    sum = a + b
    print(sum)
    return sum
SumCalculator(21, 10) # 31

def Product(a, b=5):
    product = a * b
    print(product)
Product(10) # 50
Product(10, 20) # 200

"""Fuction Questions"""
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def len_calculator(list):
    print(len(list))
len_calculator(list1) # 5
len_calculator(list2) # 9

def print_list(list):
    for i in list:
        print(i, end=" ")
print_list(list1) # 1 2 3 4 5

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
factorial(4) # 24

def odd_even(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
odd_even(5) # Odd
odd_even(10) # Even 


"""Recursion"""
# Recursion is a process in which a function calls itself as a subroutine.
def fact(n):
    if ( n == 0 or n == 1):
        return 1
    else:
        return fact(n-1) * n
print(fact(5)) # 120

def calc_sum(n):
    if n == 0:
        return 0
    return calc_sum(n-1) + n
calc_sum(5) # 15

def print_list(list, idx=0):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list, idx+1)
heroes = ["batman", "superman", "spiderman", "ironman"]
print_list(heroes, 1) # superman spiderman ironman


"""File I/O"""
# File I/O is used to read and write files in python.
f = open("Files/File.txt", "r")
line1 = f.readline()
print(line1) # Data Here
line2 = f.readline()
print(line2) # More Data Here..
data = f.read()
print(data)
f.close()

g = open("Files/File1.txt", "w")
g.write("New Data") # New Data
g.close()

h = open("Files/File1.txt", "a")
h.write("\nMore Data") # More Data
h.close()

i = open("Files/File1.txt", "r+")
i.write("\nNew Data") 
print(i.read()) # New DataMore Data
i.close()

j = open("Files/File1.txt", "w+")
j.write("Totally New Data")
print(j.read()) 
j.close()

with open("Files/File.txt", "r") as f:
    data = f.read()
    print(data)

with open("Files/File.txt", "w") as f:
    f.write("Totally New Data")

# Create a new file and write data to it
with open("Files/NewFile.txt", "w") as f:
    f.write("New File Data for I/O\nMore Data")

# Replace Data with Value in new file
with open("Files/NewFile.txt", "r") as f:
    data = f.read()
    new = data.replace("Data", "Value")
with open("Files/NewFile.txt", "w") as f:
    f.write(new)

# Find Word in line and print its line number
def check_for_line(word):
    data = True
    line_no = 1
    with open("Files/NewFile.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(f"Word found in line {line_no}")
                return
            line_no += 1
    return -1

# From a file containing numbers separated by commas, find the even numbers and print them
with open("Files/StringFile.txt", "r") as f:
    data = f.read()
    print(data)
    nums = data.split(",")
    print(nums) 
    even_nums = []
    for num in nums:
        if int(num) % 2 == 0:
            even_nums.append(num)
        print(even_nums) 



print(check_for_line("Value")) 

"""Module"""
# A module is a file containing Python code.
# It can define functions, classes, and variables.


import os
os.remove("files/File1.txt") # remove file

import os
os.rename("Files/File.txt", "Files/ModifiedFile.txt") # rename file
os.rename("Files/ModifiedFile.txt", "Files/File.txt") # rename file back to original name

