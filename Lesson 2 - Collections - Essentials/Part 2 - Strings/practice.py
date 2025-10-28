# Question 3 
def create_username(first_name, last_name): 
    username = (first_name + '_' + last_name).lower() 
    return username 

#Alternate solution 
def create_username(first_name, last_name): 
    return f"{first_name}_{last_name}".lower()

#Test it 
print(create_username("John", "Smith"))     #john_smith
print(create_username("MARY", "Jones"))     #mary_jones
print(create_username("Alex", "TAYLOR"))    #alex_taylor 


def check_email(email): 
    if "@" in email: 
        if email.lower().endswith(".com"): 
            return True 
    return False 


#Alternate Solution 
def check_email(email): 
    email_lower = email.lower() 
    return '@' in email_lower and email_lower.endswith(".com")

#Test it 
print(check_email("test@gmail.com"))     #True
print(check_email("user@yahoo.COM"))     #True
print(check_email("invalid.com"))        #False
print(check_email("test@school.edu"))    #False 


def create_slug(title): 
    return title.strip().lower().replace(' ', '-') 

#Test it 
print(create_slug("My First Blog Post"))    #my-first-blog-post
print(create_slug("  Python Tutorial  "))   #python-tutorial
print(create_slug("Web Development 101"))   #web-development-101