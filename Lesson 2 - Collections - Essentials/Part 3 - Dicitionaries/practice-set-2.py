def calculate_engagement_rate(post): 
    engagement = 0  
    views = post.get('views', 0) 
    if views == 0: 
        return 0 
    for key, value in post.items(): 
        if post.get('likes', 0): 
            engagement += post['likes']
        if post.get('comments', 0): 
            engagement += post['comments']
        if post.get('shares', 0): 
            engagement += post['shares'] 
            rate = (engagement / post['views'])*100
            return round(rate, 2) 

#Test it 
post = {'views': 1000, "likes": 50, "comments": 10, "shares": 5} 
print(calculate_engagement_rate(post)) #6.5

            