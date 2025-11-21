def safe_divide(a, b): 
    try: 
        result = a / b 
        return result 
    # except: 
    #     print("Can not divide by zero!") 
    #     return None 
    except ZeroDivisionError: 
        print("Can not divide by zero!") 
        return None 
    except TypeError: 
        print("That's not a valid number!") 
        return None 
    except: 
        print("An error occurred...") 
        
print(safe_divide(10, 2)) #5.0 

print(safe_divide(10, 0)) #Can not divide by zero! Returns None 
print(safe_divide(10, "hello")) 

def safe_operations(a,b,lst,key,d): 
    try: 
        print(f"Division Result: {a/b}") #ZeroDivisionError, 
        #TypeError
        print("Access list element:", lst[2]) #IndexError 
        print("Access Dictionary Key:", d[key]) #KeyError 
        print(f"Add numbers: {a + b}") #TYpeError 
    except ZeroDivisionError: 
        print("Can not divide by zero!") 
    except IndexError: 
        print("List index out of range!") 
    except KeyError: 
        print(f"Key {key} not found in dictionary") 
    # except TypeError: 
    #     print("Invalid types for operation!") 
    except Exception as e: 
        print("Some other error occured", e) 
        
# print(safe_operations(10,2,[1,2],"Tom", {"John":15}))
# print(safe_operations(10,0,[1,2],"Tom", {"John":15}))
print(safe_operations(10,"hello",[1,2],"Tom", {"Tom":15}))


def calculate_price_per_item(total_cost, item_count): 
    try: 
        price_per_item = total_cost / item_count 
        return round(price_per_item, 2) 
    except ZeroDivisionError: 
        return "No items to calculate"
    
print(calculate_price_per_item(100,4))
print(calculate_price_per_item(50,0))
print(calculate_price_per_item(25.50,3))

        
def parse_age(age_str): 
    try: 
        age = int(age_str) 
        return age 
    except ValueError: 
        return None

print(parse_age("25")) 
print(parse_age("twenty-five"))
print(parse_age("007")) 
print(parse_age("25.5"))

