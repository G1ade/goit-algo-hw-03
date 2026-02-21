import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Generates a set of unique random numbers for a lottery.

    Parameters:
    min (int): the minimum possible number (no less than 1)
    max (int): the maximum possible number (no more than 1000)
    quantity (int): the number of numbers to select

    Returns:
    list: a sorted list of unique random numbers
    or an empty list if the parameters are incorrect
    """
    # Validation of input parameters
    if not (1 <= min <= 1000):
        return []
    if not (1 <= max <= 1000):
        return []
    if min >= max:
        return []
    
    # Check if it is possible to select a quantity of unique numbers from a range
    available_numbers = max - min + 1
    if quantity > available_numbers:
        return []
    
    # Generation of unique random numbers
    numbers = random.sample(range(min, max + 1), quantity)
    
    # Return of the sorted list
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(10, 20, 5)
print('Your lottery numbers:', lottery_numbers)