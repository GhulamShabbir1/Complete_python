
# a. Create a variable name and assign your name to it.
name = "John"
print(name)

# b. Create variables num1 and num2, assign them integer values, calculate and print their sum.
num1 = 10
num2 = 20
sum_of_nums = num1 + num2
print("Sum:", sum_of_nums)

# a. Create a string variable sentence with the value "Hello, World!".
sentence = "Hello, World!"

# b. Print the length of the string.
print("Length of the string:", len(sentence))

# c. Print the first three characters of the string.
print("First three characters:", sentence[:3])

# a. Create a list fruits with three fruit names.
fruits = ["apple", "banana", "cherry"]

# b. Add a new fruit to the list.
fruits.append("orange")

# c. Print the second item in the list.
print("Second fruit:", fruits[1])


# a. Write a program that takes a number as input and prints whether it's positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# b. Write a program to check if a number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# a. Use a loop to print numbers from 1 to 5.
for i in range(1, 6):
    print(i)

# b. Use a loop to iterate through a list of colors and print each color.
colors = ["red", "blue", "green", "yellow"]
for color in colors:
    print(color)


# a. Write a function square that takes a number as input and returns its square.
def square(num):
    return num ** 2

print("Square of 4:", square(4))

# b. Write a function greet that takes a name as input and prints a greeting.
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


# a. Create a dictionary student with keys 'name' and 'age'.
student = {
    'name': 'John',
    'age': 20
}

# b. Add a new key-value pair to the dictionary.
student['grade'] = 'A'

# c. Print the value associated with the 'age' key.
print("Student's age:", student['age'])


#a. Create a text file and write a few lines of text to it using Python.


import math
num = 16
print("Square root:", math.sqrt(num))


from my_medule import my_function
print(my_function())


