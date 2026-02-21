from datetime import datetime
import re

# def input_date() -> str:
#     """
#     Prompts the user to enter a valid date (year, month, and day separately).

#     The function validates:
#     - Year must be 4 digits (YYYY format)
#     - Month must be between 1 and 12
#     - Day must be valid for the given month and year (including leap years)

#     Returns: str: A validated date string formatted as "YYYY-MM-DD".
#     """
    
#     # Loop until a valid year is entered
#     while True:
#         year = input('Input year "YYYY" - ')
#         if year.isdigit() and len(year) == 4:
#             year = str(year)
#             break
#         print('Year must be 4 digits (for example: 2026)')

#     # Loop until a valid month is entered
#     while True:
#         month = input('Input month "MM" - ')
#         if month.isdigit() and 1 <= int(month) <= 12:
#             month = str(month)
#             break
#         print('Month must be 2 digits and in range from 01 to 12, (for example: 02)')  
 
#     # Loop until a valid day is entered
#     while True:
#         day = input('Input day "DD" - ')
#         if day.isdigit():
#             day = str(day)
#             try:
#                  # Validate the full date (also checks leap years)
#                  date_check = datetime(int(year), int(month), int(day)).date()
#                  break
#             except ValueError:
#                  print('Invalid day number for this monts')
#         else:        
#             print('Day must be a number')

#     return f'{year}-{month}-{day}'

def get_days_from_today(date: str) -> int | None:
    """
    Calculate the number of days between a given date and today.
    
    Accepts dates in 'YYYY-MM-DD' or 'DD-MM-YYYY' formats (with any non-digit separators).
    Returns the difference in days (positive for future dates, negative for past dates).
    Returns None if the input format is invalid or the date doesn't exist.
    
    Args:
        date: A date string with any separator (e.g., '2020-12-13', '13.12.2020', '13/12/2020')
    
    Returns:
        int: Number of days from today to the given date, or
        None: If the date is invalid or parsing fails
    """
    format = ('%Y%m%d', '%d%m%Y')
    # Remove all non-digit characters from input (dots, dashes, slashes, etc.)
    modified_date = re.sub(r'\D', '', date)
    # Validate that we have exactly 8 digits after cleaning
    if not modified_date.isdigit() or len(modified_date) != 8:
        print('Enter the date in the correct format "YYYY-MM-DD or DD-MMYYYY".')
        return None
    # Try each format in order until one succeeds
    for el in format:
        try:
            formatted_date = datetime.strptime(modified_date, el).date()
            break
        except ValueError:
            continue            
    else:
        # This else clause executes only if the loop completed without break
        print('Invalid date. Please check the day/month/year.')
        return None

    today = datetime.today().date()
    # Calculate and return the difference in days
    return (formatted_date - today).days

# date_string = input_date()
# print(f'You entered: {date_string}')
date_string = input('Please enter your date "YYYY-MM-DD or DD-MM-YYYY" - ')
result = get_days_from_today(date_string)
if result is not None:
    print(f'Days from today - {result}')