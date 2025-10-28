email = "John.Smith@Gmail.COM"
normalized = email.lower() 
#Normalizes the email to lower case; email is now equal to "john.smith@gmail.com"
username = normalized.split("@")[0] 
#Splits the string where the '@' is and turns the components into a list. The result is: ['john.smith', 'gmail.com'] 
#Then index zero is chosen as the assigned value so username = 'john.smith'
domain = normalized.split("@")[1] 
#Index 1 is then chosen from the list so domain equals 'gmail.com'
print(username, domain) 
#This prints the username and domain so the result is "john.smith" "gmail.com" 



text = "The Quick Brown Fox"
words = text.split() 
#This separates the string into a list of words that are separted by the spaces: ['The', 'Quick', 'Brown', 'Fox']
initials = "" 
# This makes the variable initials equal to an empty string
for word in words:
    initials += word[0].lower() 
#This loops through the list and adds the first letter of each word in lowercase to the initials variable
print(initials) 
#This prints the initials variable which is now equal to "tqbf" 



def extract_domain(email): 
    if email.count('@') != 1: 
        return "invalid email" 
    return email.lower().split('@')[1] 

#Test it
print(extract_domain("john@gmail.com"))        # "gmail.com"
print(extract_domain("JANE@YAHOO.COM"))        # "yahoo.com"
print(extract_domain("missing.at.sign.com"))   # "Invalid email"
print(extract_domain("too@@many@signs.com"))   # "Invalid email"


message = "Hello123World456"
digits = "" 
#This makes the variable digits equal to an empty string
for char in message: 
    if char.isdigit():
        digits += char 
#This loops through every character in the message string, and if it contains a digit, it adds that digit 
#to the empty string 
print(digits)
#This prints all of the digits present in the string which are "123456" 



filename = "my-document.txt"
name_only = filename.replace(".txt", "") 
#This replaces the '.txt' in the string to nothing, so name_only is equal to 'my-document'
safe_name = name_only.replace("-", "_") 
#This replaces the hyphen in the string to an underscore so safe_name is equal to my_document
result = safe_name.upper() 
#This makes the entire string uppercase
print(result) 
#This prints out the result which is 'MY_DOCUMENT' 
 
 
data = "apple, banana, cherry, date"
items = data.split(",") 
#This makes a list out of the data variable string that is seprated by commas: ["apple", "banana", "cherry", "date"]
longest = items[0] 
#This makes the variable longest equal to the first index in the list which is 'apple'
for item in items:
    if len(item) > len(longest):
        longest = item 
#This goes through every item in the list to find the longest item by seeing if the current item is longer than the 
#previous item, and if it is, it sets that item to the longest variable so it is now the current longest item until it 
#is compared to the next item
print(longest) 
#This prints out the item with most characters which is 'banana' 


def filter_numbers(text): 
    result = '' 
    for char in text: 
        if char not in "0123456789": 
            result += char 
    return result
    return "no numbers here!" 


#Test it 
print(filter_numbers("Hello123World456"))       # "HelloWorld"
print(filter_numbers("Test 1 2 3"))             # "Test"
print(filter_numbers("Price: $29.99"))          # "Price: $"
print(filter_numbers("No numbers here!"))      # "No numbers here!" 



url = "https://example.com/users/profile" 
parts = url.split("/") 
#This splits the string into a list by the slashes present so the result is: ['https:', '', 'example.com', 'users', 'profile]
protocol = parts[0] 
#This sets this variable equal to the first item in the list which is "https:"
domain = parts[2] 
#This sets this variable equal to the 2nd index in the list which isn 'example.com'
path = "/".join(parts[3:]) 
# This selects the third index and goes to the end to the list and joins them with a slash so the result is: 
# "users/profile"
print(f"{protocol}//{domain}/{path}")
#This prints the first index in the list, https:, followed by 2 slashes, and then followed with the second index which
#is "example.com", a slash, and then the last two items in the list which are "users" and "profile" 
#The final result is "https://example.com/users/profile" 





def count_character_types(text): 
    letters = 0 
    digits = 0 
    spaces = 0 
    for char in text.lower(): 
        if char in "abcdefghijklmnopqrstuvwxyz": 
            letters += 1 
        if char in "0123456789": 
            digits += 1 
        if char == " ": 
            spaces += 1 
    return {"letters": letters, "digits": digits, "spaces": spaces}



#Test it 
print(count_character_types("Hello 123")) # {"letters": 5, "digits": 3, "spaces": 1}


print(count_character_types("Test2024!")) # {"letters": 4, "digits": 4, "spaces": 0}





