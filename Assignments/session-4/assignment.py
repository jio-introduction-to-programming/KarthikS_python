# Lists in Python
def create_list(n):
    '''
        Task: Create a list of n integers starting from 0.
    '''
    result = list(range(n))
    return result

def find_element_in_list(lst, element):
    '''
        Task: Check if element is in lst and return a boolean result.
    '''
    result = element in lst
    return result

# List comprehensions
def generate_square_list(n):
    '''
        Task: Generate a list of squares of integers from 0 to n using list comprehension.
    '''
    result = [i**2 for i in range(n+1)]
    return result

# List methods
def add_element(lst, element):
    '''
        Task: Add element to the end of lst.
    '''
    result = lst.append(element)
    return result

def remove_element(lst, element):
    '''
        Task: Remove element from lst.
    '''
    result = lst.remove(element)
    return result

# Dictionaries
def create_dict(keys, values):
    '''
        Task: Create a dictionary from keys and values.
    '''
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result

def get_value_from_key(dct, key):
    '''
        Task: Get value of key from dct.
    '''
    result = dct.get(key)
    return result

# Dictionary comprehensions
def generate_dict(n):
    '''
        Task: Generate a dictionary where keys are integers from 0 to n and values are their squares.
    '''
    result = {i: i**2 for i in range(n+1)}
    return result

# Dictionary methods
def get_keys(dct):
    '''
        Task: Get all keys from dct.
    '''
    result = list(dct.keys())
    return result

def get_values(dct):
    '''
        Task: Get all values from dct.
    '''
    result = list(dct.values())
    return result

# Negative indexing
def get_last_element(lst):
    '''
        Task: Get the last element from lst using negative indexing.
    '''
    result = lst[-1]
    return result

# List slicing
def get_slice(lst, start, end):
    '''
        Task: Get a slice from lst from index start to end.
    '''
    result = lst[start:end]
    return result

# For loop
def count_elements(lst):
    '''
        Task: Count the number of elements in lst using a for loop.
    '''
    result = 0
    for _ in lst:
        result += 1 
    return result

# Range function
def create_range(start, end):
    '''
        Task: Create a range of integers from start to end.
    '''
    result = 0
    result = list(range(start, end+1))
    return result

# If else
def check_greater(a, b):
    '''
        Task: Check if a is greater than b.
    '''
    result = a > b
    return result

# If else with logical operators
def check_in_range(n, start, end):
    '''
        Task: Check if n is in the range between start and end.
    '''
    result = start <= n <= end
    return result
