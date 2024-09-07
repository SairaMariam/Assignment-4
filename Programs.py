# Even or Odd numbers
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")


# Positive, negative numbers and Zero
if number > 0:
    print(number, "is positive.")
elif number < 0:
    print(number, "is negative.")
else:
    print(number, "is zero.")


# Divisibility by 2 and 3

if number % 2 == 0:
    print(number, "is divisible by 2.")
else:
    print(number, "is not divisible by 2.")


# Voting Eligibility
age = int(input("Enter your age: "))

if age >= 18:
    nationality = input("Are you Pakistani? (yes/no): ")
    if nationality.lower() == "yes":
        print("You are eligible to vote.")
    else:
        print("Please obtain a valid ID to vote.")


# Age Category
if age <= 12:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
elif age <= 59:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


#  Days in a Month
month = int(input("Enter a month (1-12): "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif month == 2:
    print("28 days (assuming a non-leap year)")
else:
    print("Invalid month.")


#  Leap Year Check
year = int(input("Enter a year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

