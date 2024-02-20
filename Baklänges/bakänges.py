ord = input("Är ordet palindrom")

output = ""
for x in reversed(ord): 
    output += x
   
if ord == output:
    print("Det är en palindrom") 
else: 
    print("Det är inte en palindrom") 

