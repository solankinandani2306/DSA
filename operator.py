#1. Perform addition, subtraction, multiplication, and division.
def operation(a,b):
    return a+b,a-b,a/b,a*b

x=int(input("enter x="))
y=int(input("enter y="))
sum,sub,div,mul=operation(x,y)
print("sum=",sum)
print("sub=",sub)
print("div=",div)
print("mul=",mul)

#2. Find the remainder and quotient of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Quotient =", a // b)
print("Remainder =", a % b)

#3. Check whether a number is even or odd.
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

#4. Compare two numbers using relational operators.
a = int(input("Enter number: "))
b = int(input("Enter number: "))
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

#5. Demonstrate logical operators (and, or, not).
a = int(input("Enter number: "))
b = int(input("Enter number: "))
print("a > 0 and b > 0 :", a > 0 and b > 0)
print("a > 0 or b > 0  :", a > 0 or b > 0)
print("not(a > 0)      :", not(a > 0))

#6. Demonstrate assignment operators (+=, -=, *=, /=).
a = int(input("Enter a number: "))
a += 5
print("After += 5 :", a)
a -= 2
print("After -= 2 :", a)
a *= 3
print("After *= 3 :", a)
a /= 2
print("After /= 2 :", a)

#7. Find the largest of two numbers using comparison operators.
a = int(input("Enter number: "))
b = int(input("Enter number: "))
if a > b:
    print("Largest number =", a)
elif b > a:
    print("Largest number =", b)
else:
    print("Both numbers are equal")
