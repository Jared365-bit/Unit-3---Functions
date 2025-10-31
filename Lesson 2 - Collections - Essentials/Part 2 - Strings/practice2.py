def format_phone_numbers(phone): 
    a = phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    if len(a) == 10: 
        if a.isdigit(): 
            return f"({a[0:3]}) {a[3:6]}-{a[6:10]}" 
    return "Invalid phone number" 

#Test it 
print(format_phone_numbers("555-123-4567"))      # Output: "(555) 123-4567"
print(format_phone_numbers("(555) 123 4567"))    # Output: "(555) 123-4567"
print(format_phone_numbers("5551234567"))        # Output: "(555) 123-4567"
print(format_phone_numbers("123"))               # Output: invaid phone number 


# def sanitize_filename(filename): 
#     a = filename.replace(" ", "_").lower() 
#     for char in a: 
#         if char not in "abcdefghijklmnopqrstuvwxyz0123456789_-.": 
#             a = a.replace(char, "") 
    
#     # Truncate if too long (accounting for .txt extension)
#     if len(a) > 50:
#         if a.endswith('.txt'):
#             # Already has .txt, just truncate the whole thing to 50
#             a = a[:50]
#         else:
#             # Doesn't have .txt, truncate and add it
#             a = a[:50-4] + '.txt'
#     elif not a.endswith('.txt'):
#         # Short enough but missing .txt
#         a = a + '.txt'
    
#     return a




#Alternate Solution 
def sanitize_filename(filename):
    """Clean and format a filename for safe use. """
    # Step 1: To lowercase
    clean = filename.lower()

    # Step 2: Spaces to underscores
    clean = clean.replace(" ", "_")

    # Step 3: Keep only allowed characters
    allowed = ""
    for char in clean:
        if char.isalnum() or char in ".-_":
            allowed += char

    # Step 4: Handle .txt extension
    if allowed.endswith(".txt"):
        result = allowed
    else:
        if "." in allowed:
            dot_pos = allowed.rfind(".")
            allowed = allowed[:dot_pos]
        result = allowed + ".txt"

    # Step 5: Max 50 characters
    if len(result) > 50:
        max_base = 50 - 4 # 50 - 4 for ".txt"
        result = result[:max_base] + ".txt"
    
    return result




#Alternate Solution 2 
def sanitize_filename(filename):
    """Clean and format a filename for safe use."""
    # Lowercase and replace spaces
    clean = filename. lower() .replace(" ", "_")

    # Keep safe characters
    safe = ""
    for char in clean:
        if char.isalnum() or char in ".-_":
         safe += char

# Handle extension
    if not safe.endswith(".txt"):
       if "." in safe:
         safe = safe[: safe.rfind(".")]
       safe += ".txt"

# Truncate
    if len(safe) > 50:
        safe = safe[:46] + ".txt" # 46 + 4 = 50

    return safe




#Test it 
print(sanitize_filename("Ancient Scroll.txt")) # "ancient_scroll.txt"
print(sanitize_filename("Quest 2042! (Epic)")) # "quest_2042_epic.txt"
print(sanitize_filename("notes")) # "notes.txt"
print(sanitize_filename("X"*60)) # Long name (50 char max with .txt)





# 
# 

         
          

    