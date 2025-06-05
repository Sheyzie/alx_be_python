#!/usr/bin/env python

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  temp = (fahrenheit - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR
  print(f'{fahrenheit}\N{DEGREE SIGN}F is {temp}\N{DEGREE SIGN}C')

def convert_to_fahrenheit(celsius):
  temp = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  print(f'{celsius}\N{DEGREE SIGN}C is {temp}\N{DEGREE SIGN}F')


temp = float(input('Enter temperature to convert:'))
unit = (input('Is this temperature in Celsius or Fahrenheit? (C/F): '))

if unit.upper() == 'C':
  convert_to_fahrenheit(temp)
elif unit.upper() == 'F':
  convert_to_celsius(temp)
else:
  exit(1)

