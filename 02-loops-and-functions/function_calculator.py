# Guided training project: function-based calculator
# Personal change: added modulus (%) as a fifth operation.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("1) Addition")
print("2) Multiplication")
print("3) Subtraction")
print("4) Division")
print("5) Modulus")

choice = input("Enter your choice: ")


def add(a, b):
    print("Result is:", a + b)


def multiply(a, b):
    print("Result is:", a * b)


def subtract(a, b):
    print("Result is:", a - b)


def divide(a, b):
    print("Result is:", a / b)


def modulus(a, b):
    print("Result is:", a % b)


if choice == "1":
    add(num1, num2)
elif choice == "2":
    multiply(num1, num2)
elif choice == "3":
    subtract(num1, num2)
elif choice == "4":
    divide(num1, num2)
elif choice == "5":
    modulus(num1, num2)
else:
    print("Choice was invalid")
