dictionary = {} 

alfabet = input("Skriv ett ord för att få ordet räknat. :") 

for bokstav in alfabet: 
    if bokstav in dictionary: 
        dictionary[bokstav] += 1 

    else: 
        dictionary[bokstav] = 1 

        print(dictionary)