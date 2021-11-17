# Name: Woohyuk Kim
#
# Q1. Calendar Problem
# Date: November 16th, 2021

# import calender module which provides useful functions related to the calendar
import calendar


# main function has no return value
def main() -> None:
    num_of_sunday = 0
    # loop through 20th century years
    for year in range(1901, 2001, 1):
        # loop through 12 months of each year
        for month in range(1, 13, 1):
            # count how many sundays fell on the first of the month during the twentieth century
            # calendar.monthrange() considers leap years as well (No extra steps required)
            # 0th index returns weekday of first day of the specified year and month
            if calendar.monthrange(year, month)[0] == 6:
                num_of_sunday += 1
    print(num_of_sunday)


# main function call
if __name__ == "__main__":
    main()
