# Python program to Find day of
# the week for a given date
import calendar  # module of python to provide useful fucntions related to calendar
import datetime  # module of python to get the date and time


def findDay(date):
    # this statement returns an integer corresponding to the day of the week
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    # this statement returns the corresponding day name to the integer generated in the previous statement
    return (calendar.day_name[born])


# Driver program
date = '15 10 1996'  # this is the input date
# here we print the final output after calling the function findday
print(findDay(date))
