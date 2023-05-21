def add_years_to_date (date, year) :
    result = date.replace(year = date.year + year)
    return result