import re


def normalize_phone(num: str) -> str:
    normalized_num = re.sub('[^+0-9]', '', num)
    prefixes_map = {
        '^0': '+38', 
        '^80': '+3', 
        '^380': '+',
        '^[1-9]': '+380'
    }

    if normalized_num.startswith('+380'):
        return normalized_num
    
    for search, complement in prefixes_map.items():
        match = re.search(search, normalized_num); 

        if match:
            return complement + normalized_num
        
    # edge case
    return normalized_num


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "8 097 717-2-717",
    "432 11 222 22 22",
    "44-212-22-22",
    "+380 (6565) 33 333 33 ",
    " (6131) 354646",
    "+31-24-3611111" # edge case: NL number
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized numbers for SMS-campaign:", sanitized_numbers)
