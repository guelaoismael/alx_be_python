def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        print(f"The result of the division is {result}")
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.")
    except ValueError as e:
        print("Error: Please enter numeric values only.")