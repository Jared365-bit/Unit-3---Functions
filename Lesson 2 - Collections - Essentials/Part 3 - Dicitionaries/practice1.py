def find_top_players(players, min_score):
    """ Return a list of usernames for players with score >= min_score """
    # YOUR CODE HERE 
    top_player = "" 
    min_score = 0 
    for player in players: 
        if player["score"] > min_score: 
            top_player += player["username"] + ', ' 
            min_score = player["score"] 
    return {top_player[:2-1]} 
            
            
            
    pass
# Test it
players = [
    {"username": "DragonSlayer", "score": 8500},
    {"username": "NinjaWarrior", "score": 6200},
    {"username": "MageKing", "score": 9100},
    {"username": "ShadowAssassin", "score": 5800}
]

result = find_top_players(players, 7000)
print(result)  # Should print: ['DragonSlayer', 'MageKing']