def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "substract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return -1
            else:
                return num1 / num2
        case _:
            print("Cannot recognize this operation")
            return 0
