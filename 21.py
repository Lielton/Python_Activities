import isLeapYear as f


def isValidDate(year, month, day):
    if month > 12:
        return False
    if month < 1:
        return False
    if day < 1:
        return False
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            return False
        else:
            return True
    elif month == 2:
        if f.isLeapYear(year):
            if day > 29:
                return False
            else:
                return True
        else:
            if day > 28:
                return False
            else:
                return True
    else:
        if day > 31:
            return False
        else:
            return True

assert isValidDate(1999, 12, 31) == True

assert isValidDate(2000, 2, 29) == True

assert isValidDate(2001, 2, 29) == False

assert isValidDate(2029, 13, 1) == False

assert isValidDate(1000000, 1, 1) == True

assert isValidDate(2015, 4, 31) == False

assert isValidDate(1970, 5, 99) == False

assert isValidDate(1981, 0, 3) == False

assert isValidDate(1666, 4, 0) == False

 

import datetime

d = datetime.date(1970, 1, 1)

oneDay = datetime.timedelta(days=1)

for i in range(1000000):

    assert isValidDate(d.year, d.month, d.day) == True

    d += oneDay
