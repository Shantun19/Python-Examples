# check year is leap year or not 

year = int(input('Enter year '))

if (year%4 == 0):
    if (year%100 == 0):
        if(year%400 == 0):
            print('{} is a leap Year '.format(year))
        else :
            print('{} is not a leap Year'.format(year))
    else:
        print('{} is a leap year'.format(year))
else:
    print('{} is not a leap Year'.format(year))
    
# or 

if (year%4 == 0) and (year%100) or (year%400 == 0):
    print('{} is a leap year'.format(year))
else:
    print('{} is not a leap year'.format(year))
