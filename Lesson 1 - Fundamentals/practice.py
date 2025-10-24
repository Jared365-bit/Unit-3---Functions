#If member_status is "premium"; return price with 30% discount 
#If member_status is "standard"; return price with 15% discount 
#Otherwise: return original price 

def get_discounted_price(price, member_status): 
    """ Calculate discounted price based on membership status.

    Args:
        price (float): Original price of the item.
        member_status (str): Membership status ("premium", "standard", or other).

    Returns:
        float: Discounted price based on membership status.
        Example: >>>get_discounted_price(100, "premium") 
        70.0
    """
    if member_status == "premium": 
        return price * 0.7
    elif member_status == "standard": 
        return price * 0.85
    return price 
# Test it 
print(get_discounted_price(100, "premium"))  # Should return 70.0 
print(get_discounted_price(100, "standard")) # Should return 85.0 
print(get_discounted_price(100, "guest"))     # Should return 100.0 


def count_vowels(text): 
    """ Count the number of vowels in a given text. 
    Args:
        text (str): The input text to analyze. 
    Returns:
        int: The number of vowels in the text. 
        Example: >>>count_vowels("Hello World") 
        3
    """ 
    count = 0
    for char in text: 
        if char in "aeiouAEIOU": 
            count += 1 
    return count 

# Test it 
print(count_vowels("Hello World"))  # Should print: 3 
print(count_vowels("Python"))       # Should print: 1
print(count_vowels("AEIOU"))        # Should print: 5

def validate_password(password): 
    """ Validate password strength.
    A valid password must be at least 8 characters long and contain at least one digit.

    Args:
        password (str): The password to validate. 
    Returns: 
        boolean: True if password is valid, else False 
        Example: >>>validate_password("pass1234") 
        True
    """ 
    if len(password) < 8: 
        return False; '(too short)'
    for char in password: 
        if char.isdigit(): 
            return True 
    return False; "(no digits)"

# Test it 
print(validate_password("abc12345"))  # Should print: True 
print(validate_password("short"))   # Should print: False (too short) 
print(validate_password("nonumbers"))  # Should print: False (no digits)