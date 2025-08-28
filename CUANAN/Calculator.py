def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Simple Calculator")
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Add Binary Numbers")
print("6. Sum of Odd Numbers (0–100)")
print("7. Sum of Even Numbers (0–100)")

choice = input("Enter choice (1/2/3/4/5/6/7): ")

if choice == '5':
    # Binary addition
    b1 = input("Enter first binary number: ")
    b2 = input("Enter second binary number: ")

    # Convert binary → decimal, add, then back to binary
    result = bin(int(b1, 2) + int(b2, 2))[2:]
    print("Result (binary):", result)

elif choice == '6':
    # Sum odd numbers 0–100
    total = sum(i for i in range(101) if i % 2 != 0)
    print("Sum of odd numbers from 0 to 100:", total)

elif choice == '7':
    # Sum even numbers 0–100
    total = sum(i for i in range(101) if i % 2 == 0)
    print("Sum of even numbers from 0 to 100:", total)

else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid input")
