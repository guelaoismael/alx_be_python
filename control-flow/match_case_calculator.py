num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

result = 0

match operation:
    case "+":
       print(f"The result is {num1 + num2}")
    case "-":
        print(f"The result is {num1 - num2}")
    case "*":
        print(f"The result is {num1 * num2}")
    case "/":
        if num2 == 0 :
            print("Cannont divide by zero")
        else:
            print(f"The result is {num1 / num2}")
    case _:
        print("Invalid operation")
    