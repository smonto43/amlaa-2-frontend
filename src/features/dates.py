from datetime import date

def extract_info_date(date_input):
    if date_input is None:
        return print('')
    dt = date_input
    year = dt.year
    month = dt.month
    month_day = dt.day
    day_of_week = dt.weekday()
    is_weekend = 1 if day_of_week >=5 else 0
    return year, month, month_day,day_of_week, is_weekend