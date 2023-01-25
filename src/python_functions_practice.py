def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(string):
    return len(string)

def join_string(str_1, str_2):
    return str_1 + str_2

def add_string_as_number(str_1, str_2):
    return int(str_1) + int(str_2)

def number_to_full_month_name(number):
    months = {
        "January" : 1,
        'February' : 2,
        'March' : 3,
        'April' : 4,
        'May' : 5,
        'June' : 6,
        'July' : 7,
        'August' : 8,
        'September' : 9,
        'October' : 10,
        'November' : 11,
        'December' : 12
    }
    month = list (months.keys())[list (months.values()).index(number)]
    
    return month

def number_to_short_month_name(number):
    months = {
        "Jan" : 1,
        'Feb' : 2,
        'Mar' : 3,
        'Apr' : 4,
        'May' : 5,
        'Jun' : 6,
        'Jul' : 7,
        'Aug' : 8,
        'Sep' : 9,
        'Oct' : 10,
        'Nov' : 11,
        'Dec' : 12
    }
    month = list (months.keys())[list (months.values()).index(number)]
    
    return month

def volume_of_cube(len):
    return len**3

def reverse_string(string):
    return string [::-1]


def far_to_cel(temp): 
    return ((temp-32)*5)/9


   

