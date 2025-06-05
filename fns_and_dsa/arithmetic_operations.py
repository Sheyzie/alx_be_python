#!/usr/bin/env python

def perform_operation(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                return 'Cannot divide by zero'
            elif num2 > 0: 
                return num1 / num2
            else:
                return num1 / num2
        case _:
            return 'unknown operation'

