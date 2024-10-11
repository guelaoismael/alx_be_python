class Calculator:
    calculation_type = "Arithmetic Operations"

     # This static method named "add" takes two numbers as input and returns their sum.
    @staticmethod
    def add(a, b):
        return a + b

    # This Python class method `multiply` takes two numbers as input and returns their product, while also printing the calculation type.
    @classmethod 
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b