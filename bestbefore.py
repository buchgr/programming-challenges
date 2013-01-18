import sys
import re

def valid_date(year, month, day):
    days_a_month = (31,29,31,30,31,30,31,31,30,31,30,31)
    
    if month > 12:
        return False
    if day > days_a_month[month-1]:
        return False
    if month == 2 and day == 29 and not is_leap_year(year):
        return False
    if year < 2000 or year >= 3000:
        return False

    return True

def is_leap_year(year):
    return year%400 == 0 or (year%4 == 0 and year%100 != 0)

def min_date(parts):
    # there are 3*2*1 = 6 possible ways to order the date parts
    date_map = [(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)]
    
    for d in date_map:
        year, month, day = parts[d[0]], parts[d[1]], parts[d[2]]
        if year < 1000: year += 2000
        if valid_date(year, month, day):
            return "{0}-{1:02d}-{2:02d}".format(year, month, day)

    return None 

if __name__ == "__main__":
    raw_date = raw_input();
    
    # if not re.match("(\d|\d{2}|\d{4})/(\d|\d{2}|(?<!\d{4}/)\d{4})/(\d|\d{2}|(?<!\d{4}/\2/)\d{4})$", raw_date):
    date_parts = sorted([int(n) for n in raw_date.split('/')])
    illegal_input = False
    for p in date_parts:
        if p < 0 or p >= 3000 or len(str(p)) == 3:
            illegal_input = True
            sys.stdout.write(raw_date + "is illegal")
            break

    if not illegal_input:
        date = min_date(date_parts)
        if date is not None:
            # don't print any additional spaces or newlines
            sys.stdout.write(date)
        else:
            sys.stdout.write(raw_date + " is illegal")
