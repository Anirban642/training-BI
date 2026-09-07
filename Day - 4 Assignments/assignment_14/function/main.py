from utils import calculate_age, days_between_dates, is_leap_year, get_day_of_week

try:
    dob = input("Enter DOB: ")
    print(f"Age: {calculate_age(dob)}")
    print(f"Day: {get_day_of_week(dob)}")

    date1 = input("Enter first date: ")
    date2 = input("Enter second date: ")
    print(f"Days between dates: {days_between_dates(date1, date2)}")

    year = int(input("Enter year: "))
    print(f"Leap year: {is_leap_year(year)}")

except ValueError:
    print("Invalid date format. Use YYYY-MM-DD")