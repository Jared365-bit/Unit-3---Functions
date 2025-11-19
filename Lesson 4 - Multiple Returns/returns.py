def search_data(query): 
    if query == "": 
        return None 
    if query == "empty": 
        return 0 
    if query == "error": 
        return False 
    return len(query) 

#1 Return Type - None - "No Value" 
#Meaning: Absence of value, not set, not found 
#Use for: Misssing Data, search failure, optional parameters
result = None
print(result is None)               #True - identity check
print(result == None)               #True- equality check
print(not result)                   #True - falsy check

#2 Return Type - False = Boolean False 
#Meaning: Explicit false condition, validation failure, negative result 
#Use for: Validation result, boolean operations, success/failure status
result = False 
print(result is False)              #True - identity check
print(not result)                   #True - boolean negation
print(result == 0)                  #True - falsy check 

#3 Return Zero - A Valid Number  
#Zero is VALID numeric value, not absence of value
result = 0 
print(result == 0)          #True - numerical equality 
print(not result)           #True - (falsy in boolean context) 
print(result is None)       #False - different objects 
print(result is False)      #False - different types 


#Multiple Returns - python packs multiple returns into a tuple! 
def calculate_room(length, width): 
    area = length * width 
    perimeter = 2 * (length + width) 
    return area, perimeter #Turns into a tuple (area, perimeter) 

result = calculate_room(10, 5) 
print(result)
print(type(result)) 

print(type((42))) #int
print(type((42,))) #tuple for single item  
no_parentheses = 1,2,3
print(type((no_parentheses))) 

#unpacking tuple 
area_result, perimeter_result = calculate_room(20, 6) 
print(f"Area: {area_result}")
print(f"Perimeter: {perimeter_result}") 

def multiple_grades(grades): 
   if not grades: 
       return 0,0,0,False
   highest = max(grades) 
   lowest = min(grades) 
   average = sum(grades) / len(grades) 
   Pass = average >= 60
   return average, highest, lowest, Pass 

#Test it 
print(multiple_grades([85,92,78,90]))  
print(multiple_grades([]))  
print(multiple_grades([80, 80, 80])) 
