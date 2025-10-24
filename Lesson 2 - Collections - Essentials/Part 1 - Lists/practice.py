def filter_evens(numbers): 
    """ Filter even numbers from a list.
    This function takes a list of integers and returns a new list containing only the even numbers.

    Args:
        numbers (list): A list of integers. 
    Returns: 
        list: A new list with only even numbers.
        Example: >>>filter_evens([1, 2, 3, 4, 5, 6]) 
        [2, 4, 6]
    """ 
    evens = [] 
    for num in numbers: 
        if num % 2 == 0: 
            evens.append(num) 
    return evens

# Test it 
print(filter_evens([1, 2, 3, 4, 5, ])) # Should print: [2, 4, 6]
print(filter_evens([10, 15, 20, 25])) # Should print: [10, 20]
print(filter_evens([1, 3, 5]))      # Should print: []  

def list_stats(numbers): 
    """ Calculate basic statistics from a list of numbers.
    This function takes a list of numbers and returns a dictionary containing the total, average, maximum, and minimum values.

    Args:
        numbers (list): A list of numbers. 
    Returns: 
        dict: A dictionary with total, average, max, and min values. 
        Example: >>>list_stats([10, 20, 30]) 
        {'total': 60, 'average': 20.0, 'max': 30, 'min': 10} 
    """  
    
    if not numbers: 
        return None
    maximum = max(numbers) 
    minimum = min(numbers) 
    average = round(sum(numbers) //  len(numbers), 2) 
    return {'total': sum(numbers), 'average': average, 'max': maximum, 'min': minimum}

# Test it 
print(list_stats([10, 20, 30]))  # Should print: {'total': 60, 'average': 20.0, 'max': 30, 'min': 10}
print(list_stats([5, 5, 5.0])) # Should print: {'total': 15.0, 'average': 5.0, 'max': 5.0, 'min': 5} 
print(list_stats([]))           # Should print: None