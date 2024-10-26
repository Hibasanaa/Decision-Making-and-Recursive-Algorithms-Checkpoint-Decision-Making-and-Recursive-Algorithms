def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Testing the function
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
def ticket_price(age):
    if age <= 12:
        return "$10"
    elif 13 <= age <= 17:
        return "$15"
    else:
        return "$20"

# Getting age input and displaying ticket price
age = int(input("Enter your age: "))
print(f"The ticket price is: {ticket_price(age)}")
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get input from the user
n = int(input("Enter the position in Fibonacci sequence: "))
print(f"The Fibonacci number at position {n} is: {fibonacci(n)}")
import re

def is_palindrome(s):
    # Remove spaces, punctuation, and make lowercase
    s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    
    # Recursive check
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

# Testing the function
string = input("Enter a string: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
