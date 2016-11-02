# my_tuple = (1, 2, "kitten", 4, "five")
# print my_tuple[2]



def letter_count():
    name_count = {}
    name = raw_input("what's your name?").lower()


# string into letters
# loop over letters
    for letter in name: 

# check whether letter is already counted
        if letter not in name_count:
# if no, add letter and set equal to 1
            name_count[letter] = 1
# letter is key, number is value
# if yes, add +1 to value
        else: 
            name_count[letter] += 1 
    
    return name_count

print letter_count()
