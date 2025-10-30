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