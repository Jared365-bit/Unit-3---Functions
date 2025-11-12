#Problem 1 
kills = [3, 0, 5, 2, 8, 1, 7]
streaks = [] 
#This sets the streaks variable to an empty list
current = 0 
#This sets the current variable to 0
for k in kills:
    if k > 0:
        current += k 
        #This loop iterates through each element in the kills list 
        #If the element is greater than 0, it adds the element to the current variable 
    else:
        if current >= 5:
            streaks.append(current)
        current = 0 
        #If the element is 0, it checks if current is greater than or equal to 5 
        #If so, it appends current to the streaks list and resets current to 0 
if current >= 5:
        streaks.append(current) 
    #After the loop, it checks if current is greater than or equal to 5 
    #If so, it appends current to the streaks list 
print(streaks) 
#output: 23
#This prints the list of the sum of kill streaks greater than or equal to 5: [23]


#Problem 2 
player = "[NEXUS] ShadowViper"
tag = "" 
#This sets the tag variable to an empty string 
i = 1 
#This sets the index variable i to 1
while player[i] != "]":
    tag += player[i]
    i += 1 
    #This loop iterates through the player string starting from index 1 
    #It appends each character to the tag string until it reaches the closing bracket "]"
print(tag) 
#This prints the extracted tag: "NEXUS" 


#Problem 3 
def match_mvp(players):  
    kd = 0 
    
    for player, stats in players.items(): 
        if stats["kills"] / stats["deaths"] > kd: 
            kd = stats["kills"] / stats["deaths"] 
            mvp = player 
        return mvp




players = {
"phoenix": {"kills": 28, "deaths": 12},
"cipher": {"kills": 35, "deaths": 15},
"blaze": {"kills": 22, "deaths": 18}
} 

print(match_mvp(players)) #phoenix
