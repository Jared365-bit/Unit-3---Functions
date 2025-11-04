#Problem 1
data = {"key_a": "value1", "key_b": 100, "key_c": False} 
data["key_d"] = 50 
#This adds a new key-value pair to the dictionary 
data["key_b"] = 150 
#This updates the value for key_b to 150
x = data.pop("key_c") 
#This removes the key-value pair with key "key_c" and stores the value (False) in x

print(data) 
#This prints the updated dictionary: {'key_a': 'value1', 'key_b': 150, 'key_d':50}
print(x) 
#This prints the removed value: False 


#Problem 2
data = {"val_x": 100, "val_y": 20}
total = 0

for key, value in data.items() :
    total += value
     #This adds each value in the dictionary to the total variable
data["val_z"] = total / 2 
#This adds a new key value pair with key "val_z" and value equal to half of the total variable

print(total) 
#This prints the total value: 120
print(data["val_z"]) 
#This prints the value of "val_z": 60.0 


#Problem 3 
def get_user_bio(user): 
    for key, value in user.items(): 
        if key == "bio": 
            return value 
    return "No bio available" 

       

#Test it
print(get_user_bio({"username": "coder", "bio": "Python enthusiast"})) # "Python enthusiast"
print(get_user_bio({"username": "newbie"})) # "No bio available" 


#Problem 4 
users = [
{"id": 1, "score": 100},
{"id": 2, "score": 50},
{"id": 3, "score": 150}

]

for user in users:
    user["score"] += 10 
    #This increases each user's score by 10 

print(users[1]["score"]) 
#This prints the score of the user with id 2: 60
print(users[2]["score"]) 
#This prints the score of the user with id 3: 160 


#Problem 5 
records = [
{"id": "A", "status": True},
{"id": "B", "status": True},
{"id": "C"}
]
count = 0
for item in records:
    if item.get("status", False):
        count += 1 
        #This increments the count if the status key exists and is True
print(count) 
#This prints the count of items with status True: 2 


#Problem 6 
def get_total_engagement(post): 
    total = 0 
    for key, value in post.items(): 
        if post.get("likes", 0): 
            total += post["likes"] 
        if post.get("comments", 0): 
            total += post["comments"] 
        if post.get("shares", 0): 
            total += post["shares"] 
        return total 

#Test it 
print(get_total_engagement({"likes": 100, "comments": 20, "shares": 10})) # 130
print(get_total_engagement({"likes": 50, "comments": 5})) # 55
print(get_total_engagement({"views": 1000})) # 0 


#Problem 7 
counter = {}
items = ["alpha", "beta", "alpha", "gamma", "alpha"]

for element in items:
    if element in counter:
        counter[element] += 1 
        #This checks if each element in the items list is also present in the counter dictionary and if it is 
        #increments its value by 1 
    else :
        counter[element] = 1 
        #If the element is not present in the counter dictionary, it adds it with an inital value of 1

print(counter["alpha"]) 
#This prints the count of "alpha": 3
print(len(counter)) 
#This prints the number of unique elements in the counter dictionary: 3 



#Problem 8 
dict_a = {"key1": "value1", "key2": 100}
dict_b = dict_a 
#This creates a reference to dict_a, so both dict_a and dict_b point to the same dictionary
dict_c = dict_a.copy() 
#This creates a shallow copy of dict_a, so dict_c is a separate dictionary with the same key-value pairs

dict_a["key2"] = 200 
#This updates the value for key2 in dict_a to 200
dict_b["key3"] = 50 
#This adds a new key-value pair to dict_b, which also affects dict_a since they reference the same dictionary
dict_c["key4"] = True 
#This adds a new key-value pair to dict_c, which does not affect dict_a

print(dict_a) 
#This prints the updated dict_a: {'key1': 'value1', 'key2': 200, 'key3': 50}
print(dict_c) 
#This prints dict_c: {'key1': 'value1', 'key2': 100, 'key4': True} 


#Problem 9 
def find_most_followers(users): 
    most_followers = 0 
    top_user = "" 
    if not users: 
        return None
    for user in users: 
        if user["followers"] > most_followers: 
            most_followers = user["followers"] 
            top_user = user["username"] 
    return top_user 
    
    
    


#Test it 
users = [  

    {"username": "alex","followers": 1000},

    {"username": "sam","followers": 5000},

    {"username": "jordan","followers": 3000} 
] 

print(find_most_followers(users)) # "sam"




        