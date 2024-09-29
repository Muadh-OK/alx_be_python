from datetime import datetime, timedelta

# Function to display the current date and time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()

    # Format the current date and time in a readable format
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted date and time
    print(f"Current date and time: {formatted_date}")

# Function to calculate the future date
def calculate_future_date():
    # Prompt the user for a number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))

    # Calculate the future date by adding the specified number of days to the current date
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)

    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    # Print the future date
    print(f"Future date: {formatted_future_date}")

# Main function to call the display and calculation functions
def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
