# Global variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):

    celcius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

    print(f"{fahrenheit}°F is {celcius}°C")

def convert_to_fahrenheit(celsius):
    
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {fahrenheit}°F")

if __name__ == "__main__":

    temperature = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):")[0]

    if unit == "F":
        convert_to_celsius(temperature)     
    elif unit == "C":
       convert_to_fahrenheit(temperature)
    else:
        print("Enter a valid unit:")