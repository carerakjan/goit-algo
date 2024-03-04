import math
from typing import Tuple


def read_file_save(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            return [el.strip() for el in fh.readlines() if el.strip()]
    except Exception as e:
        print(e)
        return []


def total_salary(path: str) -> Tuple[float, float]:
    total = None
    average = None

    lines = read_file_save(path)

    if lines:
        salaries = [int(line.strip().split(',')[1]) for line in lines]
        total = sum(salaries)
        average  = total // len(salaries)

    return total, average
    
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
