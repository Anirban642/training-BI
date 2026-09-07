from utils import DateUtils

date_utils = DateUtils()

try:
    dob = input("Enter DOB: ")
    print(f"Age: {date_utils.calculate_age(dob)}")
    print(f"Day: {date_utils.get_day_of_week(dob)}")

    date1 = input("Enter first date: ")
    date2 = input("Enter second date: ")
    print(f"Days between dates: {date_utils.days_between_dates(date1, date2)}")

    year = int(input("Enter year: "))
    print(f"Leap year: {date_utils.is_leap_year(year)}")

except ValueError:
    print("Invalid date format. Use YYYY-MM-DD")