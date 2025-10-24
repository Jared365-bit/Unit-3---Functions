""" 
Python List Essentials Cheat Sheet:
Create: [1, 2, 3] 
Add: .append(val) 
Remove end: .pop() 
Insert: .insert(index, val) 
Length: len(list) 
Slice: [start:end] 
Index: [0]
""" 

# Creating Lists 
daily_likes = [500, 600, 750, 400] 
usernames = ["@nasa", "@tswift", "@netflix"] 
mixed_data = [500, "likes", "@user123", True] 
#Accessing elements 
first_day = daily_likes[0]  # 500 
last_day = daily_likes[-1]  # 400 (negative indexing!) 
third_day = daily_likes[2]  # 750 
# Slicing (like Javascript slice()) 
first_three = daily_likes[0:3]  # [500, 600, 750] 
last_two = daily_likes[2:]      # [750, 400] 

# Information 
length = len(daily_likes) # 4 
maximum = max(daily_likes) # 750 
minimum = min(daily_likes) # 400 
total = sum(daily_likes)    # 2250 

# Code along - post analyzer 
def analyze_post(likes_list): 
    """ Analyze post likes data.
    This function takes a list of daily likes and returns key statistics.

    Args:
        likes_list (list): A list of integers representing daily likes. 
    Returns: 
        dict: A dictionary with total, average, max, and min likes.
        Example: >>>analyze_post([500, 600, 750, 400]) 
        {'total': 2250, 'average': 562.5, 'max': 750, 'min': 400}
    """ 
    if likes_list:
        total_likes = sum(likes_list) 
        average_likes = total_likes / len(likes_list) 
        best_day = max(likes_list) 
        return(average_likes, best_day)
    return "The list is empty!" 


def format_usernames(usernames): 
    """ Format a list of usernames by adding '@' prefix.
    This function takes a list of usernames and returns a new list with each username
    formatted as a social media handle by adding an '@' symbol at the beginning.

    Args:
        usernames (list): A list of username strings. 
    Returns:
        list: A new list with formatted handles.
        Example: >>>format_usernames(["nasa", "tswift"]) 
        ["@nasa", "@tswift"]
    """ 
    formatted = [] 
    for name in usernames: 
        formatted.append("@" + name) 
    return formatted 
# Test it 
print(format_usernames(["nasa", "tswift", "netflix"]))  # Should print: ['@nasa', '@tswift', '@netflix'] 

def filter_trending_posts(likes_list): 
    """ Filter trending posts based on likes.
    A post is considered trending if it has more than 1000 likes.

    Args:
        likes_list (list): A list of integers representing likes on different posts. 
    Returns: 
        list: A list of likes that are greater than 1000.
        Example: >>>filter_trending_posts([500, 1500, 2500, 800]) 
        [1500, 2500]
    """ 
    trending = [] 
    for likes in likes_list: 
        if likes > 1000: 
            trending.append(likes) 
    return trending 

# Test it 
print(filter_trending_posts([500, 1200, 800, 1500, 600]))  # Should print: [1200, 1500] 

