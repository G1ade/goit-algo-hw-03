import re

def normalize_phone(phone_number: list[str]) -> str:
    """
    Normalize a Ukrainian phone number to the international format +38XXXXXXXXXX.
    
    Extracts the last 10 digits (dropping any leading 0 or 380/38/8 prefixes)
    and prepends the +38 country code. Handles various input formats including
    spaces, dashes, parentheses, tabs, newlines, and other non-digit characters.
    
    Args:
        phone_number: A phone number string in any common format
    
    Returns:
        str: Normalized phone number in +38XXXXXXXXXX format
    """   
    # Remove all non-digit characters (spaces, dashes, parentheses, tabs, etc.)
    just_digit = re.sub(r'\D', '', phone_number)
    # leaves only the clean number without the prefix
    current_number = re.search(r"0\d*", just_digit)
    #returns a number with the prefix +38
    return "+38" + current_number.group()

data_phone = ["067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "]

sanitized_numbers = [normalize_phone(num) for num in data_phone]
print("Normalized phone numbers for SMS distribution:", sanitized_numbers)
