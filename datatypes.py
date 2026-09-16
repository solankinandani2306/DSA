#1. Demonstrate int, float, str, bool, and complex.
a = 10
b = 10.5
c = "Priyanka"
d = True
e = 2 + 3j
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))

#2. Accept two numbers and display their data types.
a = input("Enter number: ")
b = input("Enter number: ")
print("First number:", a)
print("Data type:", type(a))
print("Second number:", b)
print("Data type:", type(b))

#3. Convert a string number into an integer and float.
num = "25"
a = int(num)
b = float(num)
print("Integer =", a)
print("Type =", type(a))
print("Float =", b)
print("Type =", type(b))

#4. Find the length of a string.
name = input("Enter a string: ")
print("Length of string =", len(name))

#5. Create a list, tuple, set, and dictionary and display their types.
my_list = [10, 20, 30]
my_tuple = (10, 20, 30)
my_set = {10, 20, 30}
my_dict = {"Name": "Priyanka", "Age": 21}
print("List:", my_list)
print("Type:", type(my_list))

print("Tuple:", my_tuple)
print("Type:", type(my_tuple))

print("Set:", my_set)
print("Type:", type(my_set))

print("Dictionary:", my_dict)
print("Type:", type(my_dict))
