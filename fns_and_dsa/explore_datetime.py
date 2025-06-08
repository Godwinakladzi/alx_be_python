from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add: "))
        future_date = datetime.now() + timedelta(days=days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Main program
def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
