import re


def normalize_phone(num: str) -> str:
    normalized_num = re.sub('[^+0-9]', '', num)

    if normalized_num.startswith('0'):
        return f'+38{normalized_num}'

    if normalized_num.startswith('80'):
        return f'+3{normalized_num}'

    if normalized_num.startswith('380'):
        return f'+{normalized_num}'

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
    "8 097 717-2-717"
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized numbers for SMS-campaign:", sanitized_numbers)
