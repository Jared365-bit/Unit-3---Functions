def find_top_players(players, min_score):
    """ Return a list of usernames for players with score >= min_score """
    # YOUR CODE HERE 
    top_player = "" 
    min_score = 0 
    for player in players: 
        if player["score"] > min_score: 
            top_player += player["username"] + ', ' 
            min_score = player["score"] 
    return top_player[:-2]
# Test it
players = [
    {"username": "DragonSlayer", "score": 8500},
    {"username": "NinjaWarrior", "score": 6200},
    {"username": "MageKing", "score": 9100},
    {"username": "ShadowAssassin", "score": 5800}
]

result = find_top_players(players, 7000)
print(result)  # Should print: ['DragonSlayer', 'MageKing'] 






playlists = {
"Workout Mix": ["Eye of the Tiger", "Stronger", "Lose Yourself"],
"Study Vibes": ["Lofi Beat 1", "Chill Piano", "Rain Sounds"],
"Party Hits": ["Uptown Funk", "Levitating", "Blinding Lights"]
}


all_songs = []

for playlist_name, songs in playlists. items(): 
    #Gets each key and value pair in the dictionary
    for song in songs: 
        #Iterates through each song in the list of songs 
        all_songs.append(song.upper()) 
        #Adds the song in uppercase to the all_songs list

print(f"Total songs: {len(all_songs)}") 
#Prints the total number of songs: 9
print(f"First song: {all_songs[0]}") 
#Prints the first song in the all-songs list: EYE OF THE TIGER
print(f"Last song: {all_songs[-1]}") 
#Prints the last song in the all-songs list: BLINDING LIGHTS 





def calculate_cart_total(cart):
    "Calculate the total cost of all items in the cart and returns: total cost (float)"
    # YOUR CODE HERE 
    total = 0.00
    for item in cart: 
        total += item["price"] * item["quantity"] 
    return total 
    


# Test it
cart = [
{"item": "Laptop", "price": 899.99, "quantity": 1},
{"item": "Mouse", "price": 24.99, "quantity": 2},
{"item": "Keyboard", "price": 79.99, "quantity": 1},
{"item": "USB Cable", "price": 9.99, "quantity": 3} 
] 
total = calculate_cart_total(cart) 
print(f"Total: ${total:.2f}") #Should print: Total: $1059.93