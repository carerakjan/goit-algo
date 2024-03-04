from typing import Tuple
import math

def total_salary(path: str) -> Tuple[float, float]:
    total = None
    average = None
    
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            salaries = [int(line.strip().split(',')[1]) for line in fh.readlines() if line.strip()]
            total = sum(salaries)
            average  = total // len(salaries)
    except Exception as e:
        print(e)
    finally:
        return total, average
    
        
total, average = total_salary("hw-04/exercise_1/salaries.txt")
print(f"Total amount of salaries: {total}\nAverage salary: {average}")
