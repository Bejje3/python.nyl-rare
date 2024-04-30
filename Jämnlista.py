list = [1,3,2,7,8] 

list2 = [] 

jämn_summa = 0
ojämn_summa = 0

for tal in list: 

    if tal % 2 == 0:
        jämn_summa += tal
    else: 
        ojämn_summa +=tal 
list2.append (jämn_summa) 
list2.append (ojämn_summa) 

print(list2)