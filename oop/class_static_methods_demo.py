class Calculator:
    calculation_type = "Arithmetic Operations"

     # This static method named "add" takes two numbers as input and returns their sum.
    @staticmethod
    def add(num1, num2):
        return num1 + num2

    # This Python class method `multiply` takes two numbers as input and returns their product, while also printing the calculation type.
    @classmethod 
    def multiply(cls, num1, num2):
        print(f"Calculation type: {cls.calculation_type}")
        return num1 * num2