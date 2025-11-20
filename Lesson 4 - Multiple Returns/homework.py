#Question 1
def search_user_database(query): 
    if query == "": 
        return None, "No search query", False 
    if query == " ": 
        return None, "No search query", False  
    if not query.isalpha(): 
        return False, "Invalid characters", False 
    if query.lower() not in ["john", "jane", "max", "joe"]:       
        return 0, "No users found", True
    return 3, "Found 3 users", True
    
print(search_user_database("")) 
print(search_user_database(" ")) 
print(search_user_database("user123")) 
print(search_user_database("user@email"))  
print(search_user_database("admin"))  
print(search_user_database("jane"))  
print(search_user_database("john"))  

#Question 2 
def analyze_book_pages(pages): 
    if not pages: 
        return 0, 0, 0.0, False 
    count = len(pages)
    total_pages = sum(pages) 
    max_pages = max(pages) 
    avg_pages = sum(pages) / count 
    has_long = max_pages > 500
    return count, total_pages, round(avg_pages, 2), has_long 

print(analyze_book_pages([250, 180, 620, 310]))
print(analyze_book_pages([200, 150, 300])) 
print(analyze_book_pages([])) 
print(analyze_book_pages([500, 400, 300])) 
print(analyze_book_pages([501, 400, 300])) 

    
    