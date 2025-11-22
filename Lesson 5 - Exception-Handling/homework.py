#Question 3 
def get_phone_number(contacts, name): 
    try: 
        return contacts[name] 
    except KeyError: 
        return "Contact not found." 
    
contacts = {"Mom": "555-0123", "Dad": "555-0124", "Best Friend": "555-0125"} 
print(get_phone_number(contacts, "Mom"))
print(get_phone_number(contacts, "Boss"))
print(get_phone_number(contacts, "Best Friend")) 
      

#Question 4 
def get_song(playlist, posititon): 
    try: 
        return playlist[posititon]      
    except IndexError: 
        return "Position out of range" 
    except TypeError: 
        return "Position must be an integer" 

playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"] 
print(get_song(playlist, 2))
print(get_song(playlist, 20))
print(get_song(playlist, "first")) 

def calculate_test_average(scores): 
    try: 
        return round(sum(scores) / len(scores), 2) 
    except ZeroDivisionError: 
        return 0 
    except TypeError: 
        return "Invalid score data" 

print(calculate_test_average([88, 92, 76, 95, 84]))
print(calculate_test_average([78.5, 92.0, 85.5])) 
print(calculate_test_average([]))  



