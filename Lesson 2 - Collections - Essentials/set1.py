#Problem 1 
viewers = [1240, 1580, 2100, 1890, 2300]
peak = viewers[0] 
#This sets the peak variable equal to the first element in the list which is 1240
i = 1
while i < len(viewers): 
    #This loop iterates through the list starting from the second element
    if viewers[i] > peak: 
        peak = viewers[i]
    i += 1 
    #If the current element is greater than peak, it updates peak to that element 
print(peak) 
#This prints the highest number of viewers which is 2300 

#Problem 2 
message = "WOW POGGERS WOW LFG"
words = message.split() 
#This splits the message between spaces and creates a list of words
filtered = "" 
#This sets the filtered variable to an empty string
for word in words:
    if len(word) <= 5:
        filtered += word + " " 
    #This loop iterates through each word in the list and checks if its length is is less than or equal to 5
    #If it is, it adds the word to the filtered string followed by a space
print(filtered.strip()) 
#This prints the filtered string with leading and trailing spaces removed: "WOW WOW LFG" 


#Problem 3 
def find_top_donor(donations): 
    top_donor = ""
    peak = 0
    for key, value in donations.items(): 
        if value > peak: 
            peak = value
            top_donor = key
    return top_donor
    
    
    
    
    
donations = {
"neon": 250,
"vibe": 180,
"lunar": 400,
"pixel": 150 
} 

print(find_top_donor(donations)) #lunar