#!/usr/bin/python3

# ------------ A program to print a calendar of the specified month and year ---------------

import calendar

year = int(input("Enter Year: "))
month = int(input("Enter Month: "))

print(calendar.month(year, month))
