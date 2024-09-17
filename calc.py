# Arithmetic Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Riddles to Unlock Functions
def unlock_add():
    answer = input("What has keys but can't open locks? ")
    if answer.lower() == "piano" or answer.lower() == "keyboard":
        return add
    else:
        print("Incorrect answer. Try again!")
        return None

def unlock_subtract():
    answer = input("What starts with an E, ends with an E, but only contains one letter? ")
    if answer.lower() == "envelope":
        return subtract
    else:
        print("Incorrect answer. Try again!")
        return None

def unlock_multiply():
    answer = input("What is always coming but never arrives? ")
    if answer.lower() == "tomorrow":
        return multiply
    else:
        print("Incorrect answer. Try again!")
        return None

def unlock_divide():
    answer = input("What has a face and two hands but no arms or legs? ")
    if answer.lower() == "clock":
        return divide
    else:
        print("Incorrect answer. Try again!")
        return None

# Main Program
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Choose an operation: ")

    if choice == '1':
        add_func = unlock_add()
        if add_func:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", add_func(num1, num2))

    elif choice == '2':
        sub_func = unlock_subtract()
        if sub_func:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", sub_func(num1, num2))

    elif choice == '3':
        mul_func = unlock_multiply()
        if mul_func:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", mul_func(num1, num2))

    elif choice == '4':
        div_func = unlock_divide()
        if div_func:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result:", div_func(num1, num2))
    else:
        print("Invalid choice. Try again!")
