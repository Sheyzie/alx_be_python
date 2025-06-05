#!/usr/bin/env python

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formated_date = datetime.strftime(current_date, '%Y-%m-%d %H:%M:%S')
    print('Current date and time:', formated_date)

    return current_date

def calculate_future_date(num_of_days, current_date):
    future_date = current_date + timedelta(days=num_of_days)
    print('Future date:', datetime.strftime(future_date, '%Y-%M-%d'))


current_date = display_current_datetime()

num_days = int(input('Enter the number of days to add to the current date: '))

calculate_future_date(num_days, current_date)
