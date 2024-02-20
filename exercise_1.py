from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        converted_date = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        return (converted_date - today).days
    except ValueError:
        print(f'Entered date "{date}" doesn\'t match format: YYYY-MM-DD')


print(get_days_from_today('2023-10-05'))
