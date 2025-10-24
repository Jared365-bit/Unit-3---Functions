print("======Problem 1=====")
def remove_duplicates(items):  
    # keep occurance of first item 
    result = [] 
    for item in items: 
        if item not in result: 
            result.append(item) 
    return result 
    
  
        
# Test it 
print(remove_duplicates([1, 2, 2, 3, 1, 4])) # [1, 2, 3, 4]
print(remove_duplicates(["a", "b", "a", "c"])) # ["a", "b", "c"]
print(remove_duplicates([5, 5, 5])) # [5]
print(remove_duplicates([])) # [] 

print("======Problem 2=====")
def find_common(list1, list2): 
  result = [] 
  for item in list1: 
      if item in list2 and item not in result: 
          result.append(item) 
  return result 

#Test it 
print(find_common([1, 2, 3], [2, 3, 4])) # [2, 3]
print(find_common(["a","b"], ["c","d"])) # []
print(find_common([1, 1, 2], [2, 2, 3])) # [2]
print(find_common([], [1, 2])) # [] 


print("======Problem 3=====") 
def reverse_sublists(data, size): 
    result = [] 
    for i in range(0, len(data), size): 
        chunk = data[i:i + size] 
        result.extend(chunk[::-1]) 
    return result 

#Test it 
print(reverse_sublists([1, 2, 3, 4, 5, 6], 2)) # [2, 1, 4, 3, 6, 5]
print(reverse_sublists([1, 2, 3, 4, 5], 3)) # [3, 2, 1, 5, 4]
print(reverse_sublists([1, 2, 3, 4], 1)) # [1, 2, 3, 4]
print(reverse_sublists([1, 2, 3], 5)) # [3, 2, 1] 


print("======Problem 4=====")  
def rotate_list(items, positions): 
    if not items: 
        return [] 
    n = len(items) 
    positions = positions % n 
    return items[-positions:] + items[:-positions] 

#Test it 
print(rotate_list([1, 2, 3, 4, 5], 2))     # [4, 5, 1, 2, 3]
print(rotate_list([1, 2, 3, 4, 5], -2))    # [3, 4, 5, 1, 2]
print(rotate_list([1, 2, 3], 0))           # [1, 2, 3] 
print(rotate_list([1, 2, 3], 5))           # [2, 3, 1]