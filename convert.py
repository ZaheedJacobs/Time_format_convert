# Convert 24-hour format into 12-hour format
import re

def format_convert(time: str):
    # Split the date into 3 substrings
    year: int = int(time[2:4])
    month = time[5:7]
    day = time[8:10]

    # Create lists for month numbers and names
    month_nums = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", 
              "October", "November", "December"]
    
    num: int = 0     # Used to go through the months list

    # Check for the month
    for num_string in month_nums:
        if num_string == month:
            month = months[num]

        else:
            num += 1

    # Create 3 lists for certain day numbers with unique suffixes
    st_days = [1, 21, 31]
    nd_days = [2, 22]
    rd_days = [3, 23]
    
    # Check day integer to make day suffix
    if int(day) in st_days:
        day_suffix = "st"
    elif int(day) in nd_days:
        day_suffix = "nd"
    elif int(day) in rd_days:
        day_suffix = "rd"
    else:
        day_suffix = "th"
    
    # Add the suffix to the day string
    day = day + day_suffix

    # Convert hour string into an integer
    hour: int = int(time[11:13])

    # Check for midnight or midday
    if 0 <= hour < 12:
        time_suffix = "am"
    elif 12 <= hour < 24:
        time_suffix = "pm"

    # Convert to 12-hour format
    if hour == 0:           # If hour is 0, add 12 to it
        hour += 12

    elif 12 < hour < 24:    # If hour is between 12 and 24, subtract 12 from it
        hour -= 12

    # Create variable for the time string
    time_string = str(hour) + time[13:]

    # Return the time in 12-hour format
    print(f"{time_string}{time_suffix} on the {day} of {month} \'{year}")

def main():
    # Ask the user for the date and time in 24-hour format
    # then convert into 12-hour format
    date_and_time = input("Enter the date and time (yyyy-mm-dd hh:mm):\n")
    
    if re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", date_and_time):
        format_convert(date_and_time)
    
    else:
        print("Your input string has the wrong format, try again.")
        date_and_time = input("Enter the date and time (yyyy-mm-dd hh:mm):\n")

if __name__ == "__main__":
    main()
