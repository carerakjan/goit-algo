import math
from typing import Tuple


def read_file_safe(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            return [el.strip() for el in fh.readlines() if el.strip()]
    except Exception as e:
        print(e)
        return []


def total_salary(path: str) -> Tuple[int, int]:
    total_s = 0
    average_s = 0

    lines = read_file_safe(path)

    if lines:
        salaries = [int(line.strip().split(',')[1]) for line in lines]
        total_s = sum(salaries)
        average_s = total // len(salaries)

    return total_s, average_s

    # try:
    #     with open(path, 'r', encoding='utf-8') as fh:
    #         salaries = [int(line.strip().split(',')[1]) for line in fh.readlines() if line.strip()]
    #         total = sum(salaries)
    #         average  = total // len(salaries)
    # except Exception as e:
    #     print(e)
    # finally:
    #     return total, average


total, average = total_salary("hw-04/exercise_1/salaries.txt")
print(f"Total amount of salaries: {total}\nAverage salary: {average}")
