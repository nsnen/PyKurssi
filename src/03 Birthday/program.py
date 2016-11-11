import datetime


def header():
    print('-------------------------------')
    print('       BIRTHDAY APP')
    print('-------------------------------')
    print('')


def diff():
    bmonth =  int(input('What is ur birth month? (MM): '))
    bday = int(input('What is ur birth day of month? (DD): '))
    today = datetime.date.today()
    bdate = datetime.date(today.year, bmonth, bday)
    days = (today - bdate).days
    return days


def tell(num):
    if num < 0:
        print('ur bday will be in '+ str(num)+ ' days')
    elif num > 0:
        print('ur bday was already ' + str(num) + ' days ago')
    else:
        print('Happy birthday!')


def main():
    header()
    ddays = diff()
    tell(ddays)


main()