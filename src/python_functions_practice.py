import math

months = {
        1: 'January',2: 'February',3: 'March',4: 'April', 5: 'May',6:  'June', 7: 'July', 8:'August', 9:'September',10:'October',11: 'November',12: 'December'
        }

def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(str):
    return len(str)

def join_string(str1, str2):
    return str1 + str2

def add_string_as_number(str1, str2):
    return int(str1) + int(str2)


def number_to_full_month_name(num):
    return months[num]

def number_to_short_month_name(num):
    month = months[num]
    return month[:3]

def volume_of_cube(length_of_side):
    return length_of_side **3
    
def reverse_string(str):
    return str[::-1]

def fahrenheit_to_celcius(degrees_fahrenheit):
    return math.trunc((degrees_fahrenheit - 32) * (5/9))