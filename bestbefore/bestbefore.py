import sys
from itertools import permutations

def valid_date(year, month, day):
    days_a_month = (31,29,31,30,31,30,31,31,30,31,30,31)
    
    if month < 1 or month > 12:
        return False
    if day < 1 or day > days_a_month[month-1]:
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
    #date_map = [(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)]
    date_map = permutations([0,1,2]) 
    parts.sort()

    for d in date_map:
        year, month, day = parts[d[0]], parts[d[1]], parts[d[2]]
        if year < 2000: year += 2000
        if valid_date(year, month, day):
            return (year, month, day)

    return None 

if __name__ == "__main__":
    raw_date = raw_input();
    
    date_parts = [int(n) for n in raw_date.split('/')]
    date = min_date(date_parts)

    if date:
        # don't print any additional spaces or newlines
        sys.stdout.write("{0}-{1:02d}-{2:02d}".format(*date))
    else:
        sys.stdout.write(raw_date + " is illegal")
