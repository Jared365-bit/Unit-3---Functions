#Problem 1 
def combine_values(*nums): 
    if not nums: 
        return 1 
    product = 1 
    for num in nums:
        product *= num
    return product 

#Test it 
print(combine_values(2, 3, 4)) # → 24
print(combine_values(5)) # → 5
print(combine_values()) # → 1 


#Problem 2 
def merge_details(label, **kwargs): 
    details = {"label": label} 
    details.update(kwargs) 
    return details

print(merge_details("ItemA", size="Large", cost=12.50))  
# → {"label": "ItemA", "size": "Large", "cost": 12.50}
print(merge_details("UserX")) 
# → {"label": "UserX"} 


#Problem 3 
def process_data(*values, rate=2):
    if not values:
        return 0 
    #This makes the output 0 if there are no values 
    total = 0 
    #This makes the total variable equal to 0
    for v in values:
        total += v * rate 
    #This adds the product of every value and rate to the total
    return total 
    #This returns the total variable as an output

print(process_data(3, 1)) 
#This makes the value equal to 4 because 3 + 1 equals 4 and you are multiplying this value by 
#the rate which is the default value of 2: 8
print(process_data(2, rate=5)) 
#This makes total equal to 0 = 2 * 5: 10
print(process_data()) 
#This makes the total equal to 0 since there no values: 0 


#Problem 4 
def build_record(name, **info):
    record = {"name": name} 
    #This makes the record variable equal to a dictionary with the positional arg
    record.update(info) 
    #This makes the kwargs get added into the dictionary 
    record["count"] = len(info) 
    #This adds a new key called "count" into the dictionary that is equal to the number of kwargs
    return record 
    #This returns the complete dictionary

print(build_record("Alpha", x=1, y=2)) 
#This prints: {"name": "Alpha", "x": 1, "y": 2, "count": 2}
print(build_record("Beta")) 
#This prints {"name": Beta, "count: 0"}