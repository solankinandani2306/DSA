#write a function to print "hello,world!".
def hello():
    print("Hello, World!")

hello()


#write a function that takes a name and prints a greeting.
def greet(name):
    print("Hello", name)

greet("a")

#write a function to add two numbers.
def add(a, b):
    print(a + b)

add(10, 20)

#write a function to find the square of number.
def square(n):
    print(n * n)

square(5)

#Check whether a number is even or odd
def even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(7)

#Find the maximum of two numbers
def maximum(a, b):
    if a > b:
        print(a)
    else:
        print(b)

maximum(10, 20)

#Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    f = (c * 9 / 5) + 32
    print(f)

celsius_to_fahrenheit(25)

#Calculate area of a circle
def circle_area(r):
    area = 3.14 * r * r
    print(area)

circle_area(5)

#Calculate factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print(fact)

factorial(5)

#Check whether a number is positive, negative, or zero
def check_number(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

check_number(-5)

#Find maximum of three numbers
def maximum(a, b, c):
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)

maximum(10, 25, 15)

#Count vowels in a string
def count_vowels(text):
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
            count += 1

    print(count)

count_vowels("Hello World")

#Reverse a string
def reverse_string(text):
    print(text[::-1])

reverse_string("Hello")

#Check whether a string is palindrome
def palindrome(text):
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome("madam")

#Find sum of all elements in a list
def list_sum(numbers):
    total = 0

    for n in numbers:
        total += n

    print(total)

list_sum([10, 20, 30, 40])

#Find largest element in a list
def largest(numbers):
    max_num = numbers[0]

    for n in numbers:
        if n > max_num:
            max_num = n

    print(max_num)

largest([10, 50, 20, 40])

#Remove duplicate elements from a list
def remove_duplicates(numbers):
    result = []

    for n in numbers:
        if n not in result:
            result.append(n)

    print(result)

remove_duplicates([1, 2, 2, 3, 3, 4])

#Count how many times an element appears in a list
def count_element(numbers, element):
    count = 0

    for n in numbers:
        if n == element:
            count += 1

    print(count)

count_element([1, 2, 2, 3, 2, 4], 2)

#Check whether a number is prime
def prime(n):
    if n < 2:
        print("Not Prime")
        return

    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            return

    print("Prime")

prime(7)

#Return all prime numbers between two numbers
def primes_between(start, end):
    for n in range(start, end + 1):
        if n < 2:
            continue

        prime = True

        for i in range(2, n):
            if n % i == 0:
                prime = False
                break

        if prime:
            print(n)

primes_between(10, 30)

#Calculate Fibonacci numbers
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a)
        a, b = b, a + b

fibonacci(10)

#Find the second-largest number in a list
def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()

    print(unique[-2])

second_largest([10, 20, 5, 30, 15])

#Sort a list without using sort()
def sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    print(numbers)

sort_list([5, 2, 8, 1, 3])

#Merge two lists and remove duplicates
def merge_lists(list1, list2):
    result = []

    for n in list1 + list2:
        if n not in result:
            result.append(n)

    print(result)

merge_lists([1, 2, 3], [3, 4, 5])
