import random
from typing import List

def get_numbers_ticket(min: int = 1, max: int = 1000, quantity: int = 10) -> List[int]:
    if (min > max) or \
        (min < 1) or \
        (max > 1000) or \
        (quantity > max - min):
        return []
    
    return sorted(random.sample(range(min, max), quantity))

lottery_numbers = get_numbers_ticket(max = 59)
print("Your lotery numbers:", lottery_numbers)
