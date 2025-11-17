#Question 5 
def process_order(customer, *items, discount=0.0, **options):
    total = len(items) * 10 
    #This assumes each item costs $10 and calculates total by multiplying the number of items by 10
    total -= total * discount 
    #This applies the discount to the total, if it exists. If it doesn't exist, it defaults to 0.0 
    if options.get("express"):
        total += 5 
    #This adds a $5 express fee if the 'express' option is set to True
    return round(total, 2) 
    #This returns the final total rounded to 2 decimal places
#Question 5: 18.00
print(process_order("A", "book", "pen", discount=0.1)) 
#Question 5: 15.00
print(process_order("B", "laptop", express=True)) 


#Question 6 
def make_notification(user, *messages, urgent=False): 
    if urgent: 
        prefix = "URGENT:" 
    else: 
        prefix = "" 
    message_body = ", ".join(messages) 
    return f"{prefix} {user} - {message_body}".strip() 

print(make_notification("admin", "Server down!", urgent=True)) 
print(make_notification("user", "Welcome", "Check inbox")) 


#Question 7 
def build_query(table, *fields, where="", limit=10):
    field_str = ", ".join(fields) if fields else "*" 
    #This creates a string of fields separated by commas, or "*" if no fields are provided
    query = f"SELECT {field_str} FROM {table}" 
    #This starts building the query string with the SELECT and FROM clauses
    if where:
        query += f" WHERE {where}" 
    #This adds a WHERE clause if a condition is provided
    if limit:
        query += f" LIMIT {limit}" 
    #This adds a LIMIT clause to restrict the number of results 
    return query 
     
#Question 7: SELECT name, email FROM users LIMIT 10
print(build_query("users", "name", "email")) 
#Question 7: SELECT * FROM logs WHERE level='error' LIMIT 5
print(build_query("logs", where="level='error'", limit=5)) 

#Question 8 
def log_action(actor, *actions, timestamp=None, **context):
    action_str = ", ".join(actions) 
    context_str = ", ".join(f"{k}={v}" for k, v in context.items()) 
    log_entry = f"{actor}: {action_str}" 
    if context_str:
        log_entry += f" | {context_str}" 
    if timestamp:
        log_entry += f" @ {timestamp}" 
    return log_entry 


print(log_action("bot", "login", "scan", source="API", ip="1.2.3.4"))