# Practice Problem: Create a function that asks for a user’s birthdate (YYYY-MM-DD) 
# and calculates their exact age today in years, months, and days.


# Given Input: Birthdate: 1995-05-15, Today: 2026-01-02

# Expected Output: Age: 30 years, 7 months, 18 days
# a= 1995-05-15
# b= 2026-01-02

from datetime import datetime
from dateutil.relativedelta import relativedelta

birthdate = datetime.strptime("1995-05-15", "%Y-%m-%d")
today = datetime.strptime("2026-01-02", "%Y-%m-%d")

age = relativedelta(today, birthdate)

print(f"Age: {age.years} years, {age.months} months, {age.days} days")