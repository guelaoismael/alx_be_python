from datetime import datetime, timedelta

def display_current_datetime():
    # get current date
    current_date = datetime.now()

    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    day_number = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=day_number)

    formatted_futur_date = future_date.strftime("%Y-%m-%d")
    
    print(f"Future date: {formatted_futur_date}")