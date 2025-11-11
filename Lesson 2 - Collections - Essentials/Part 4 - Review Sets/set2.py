#Problem 1 
prices = [58200, 59500, 61000, 59800, 62500, 64000]
gains = [] 
#This sets gains variable to an empty list
i = 1 
#This sets the index variable i to 1
while i < len(prices):
    diff = prices[i] - prices[i-1] 
    #This calculates the difference between the current price and the previous price 
    if diff > 1000:
        gains.append(diff)
    i += 1 
    #This loop iterates through the prices list starting from the second element 
    #If the difference is greater than 1000, it appends the difference to the gains list 
print(len(gains)) 
#This prints the number of gains greater than 1000: 4
print(sum(gains)) 
#This prints the total sum of gains greater than 1000: 7000 


#Problem 2 
wallet = "0x9F1aB3c ... dE8f"
short = "" 
#This sets the short variable to an empty string
i = 0 
#This sets the index variable i to 0
while i < 10:
    short += wallet[i] 
    #This loop iterates through the first 10 characters of the wallet string 
    #It appends each character to the short string 
    i += 1 
    #Increment the index by 1
short += "..." 
#This adds an ellipsis to the end of the short string
print(short) 
#This prints the shortened wallet address: "0x9F1aB3c ..." 



#Problem 3 
def portfolio_value(holdings, prices): 
    total = 0
    for key, value in holdings.items():
       total += value * prices[key]
    return round(total, 2)




holdings = {"BTC": 0.5, "ETH": 8.2, "SOL": 50}
prices = {"BTC": 62400, "ETH": 2480, "SOL": 142} 

print(portfolio_value(holdings, prices))