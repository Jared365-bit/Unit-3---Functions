# def calculate_score(points, bonus): 
#     total = points + bonus 
#     print("Score calculated!") 
#     return total   

"""
Python Functions - Unit 3 Lesson 1 Starter Code
"""

# =============================================================================
# CODE ALONG 1: SOCIAL MEDIA ENGAGEMENT
# =============================================================================

# TODO: Create calculate_engagement function
# Parameters: likes, shares, comments
# Return: total engagement (sum of all three)
def calculate_engagement(likes, shares, comments): 
    """Calculate the total media engagement. 
    This functions takes the number of likes, shares, and comments on a post and 
    returns the total engagement count. 
    Args:
        likes (int): The number of likes
        shares (int): The number of shares
        comments (int): The number of comments

    Returns:
        int: The total engagement, calculated as the sum of likes, shares, and comments 
        Example: >>>>calculate_engagement(120, 45, 30)  
        195
    """
    total_engagement = likes + shares + comments 
    return total_engagement 

# Test it
print(calculate_engagement(500, 50, 200))  # Should print: 750


# =============================================================================
# PRACTICE 1: FORMAT HANDLE
# =============================================================================

# TODO: Create format_handle function
# Parameter: username (string)
# Return: username with @ prefix
# Example: format_handle("nasa") returns "@nasa"
def format_handle(username): 
    """Format a social media handle by adding an '@' prefix.
    This function takes a username string and returns it formatted as a social media handle
    by adding an '@' symbol at the beginning.

    Args:
        username (str): The username to format

    Returns:
        str: The formatted handle with '@' prefix
        Example: >>>>format_handle("nasa")  
        "@nasa"
    """ 
    return "@" + username 
    



# Test it
print(format_handle("nasa"))    # Should print: @nasa
print(format_handle("tswift"))  # Should print: @tswift


# =============================================================================
# PRACTICE 2: IS TRENDING
# =============================================================================

# TODO: Create is_trending function
# Parameter: likes (number)
# Return: True if likes > 1000, else False
def is_trending(likes): 
    """ Determine if a post is trending based on the number of likes.
    A post is considered trending if it has more than 1000 likes.

    Args:
        likes (int): The number of likes on the post

    Returns:
        boolean: True if likes > 1000, else False 
        Example: >>>>is_trending(1500) 
        True
    """
    if likes > 1000: 
        return True 
    return False

def is_trending_v2(likes): 
    """Check if post is viral (over 1000 likes)."""
    return likes > 1000
# Test it
print(is_trending(500))   # Should print: False
print(is_trending(2500))  # Should print: True


# =============================================================================
# CODE ALONG 2: MUSIC TIER SYSTEM
# =============================================================================

# TODO: Create get_tier_perks function
# Parameter: subscription_type (string)
# Return: daily skips based on tier
#   - "premium" -> 999
#   - "student" -> 10
#   - "free" -> 3
#   - anything else -> 0


# Test it
# print(get_tier_perks("premium"))  # Should print: 999
# print(get_tier_perks("student"))  # Should print: 10
# print(get_tier_perks("free"))     # Should print: 3


# =============================================================================
# PRACTICE 3: VIDEO QUALITY
# =============================================================================

# TODO: Create get_video_quality function
# Parameter: bandwidth (number in Mbps)
# Return: video quality based on speed
#   - Over 5 Mbps -> "1080p"
#   - 2-5 Mbps -> "720p"
#   - Under 2 Mbps -> "480p"


# Test it
# print(get_video_quality(1))   # Should print: 480p
# print(get_video_quality(3))   # Should print: 720p
# print(get_video_quality(10))  # Should print: 1080p
