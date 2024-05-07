mynt = [20, 8, 5, 3]

def räkna_mynt (): 
    summa = 0 
    summa += mynt[0] *1 
    summa += mynt[1] *2
    summa += mynt[2] *5
    summa += mynt[3] *10 

    return summa


print(räkna_mynt() )