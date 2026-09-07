from datetime import datetime, date
import calendar

def calculate_age(dob):
    birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

def days_between_dates(date1, date2):
    first_date = datetime.strptime(date1, "%Y-%m-%d").date()
    second_date = datetime.strptime(date2, "%Y-%m-%d").date()
    return abs((second_date - first_date).days)

def is_leap_year(year):
    return calendar.isleap(year)

def get_day_of_week(date_string):
    input_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    return input_date.strftime("%A")