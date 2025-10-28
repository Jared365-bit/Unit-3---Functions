announcement = "  BERGEN TECH robotics meeting TODAY!  " 

def format_course_code(code): 
    # spaced_code = code.strip() 
    # upper_code = spaced_code.upper() 
    # return upper_code 
    return code.strip().upper()

#Test it 
print(format_course_code("  webdev101  "))
print(format_course_code("  Python202  "))
print(format_course_code("Java303")) 


def count_hastags(post): 
    # count = 0 
    # for char in post:
    #     if char == '#': 
    #      count +=1 
    # return count 

    words = post.split() 
    
    count = 0 
    
    for word in words: 
        if word.startswith("#"): 
            count += 1 
    return count


#Test it 
post1 = "Great game today! #BergenTech #GoGamrz #Pride" 
post2 = "Meeting tomorrow in room 205" 
post3 = "#Robotics team wins #StateChampionships! #STEM #BergenTech" 

print(count_hastags(post1))
print(count_hastags(post2))
print(count_hastags(post3)) 


#There's also .endswith() 
text = "Bergen tech"
print(text.endswith("tech"))
print(text.endswith("Tech"))
