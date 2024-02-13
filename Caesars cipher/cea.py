sentence = input("skriv en mening \n")
steps = int(input("Hur mycket vill du kryptera \n"))

alphabet = "abcdefghijklmnopqrsvuvwxyzöäå"
output = ""

for letter in sentence:
    index = alphabet.index(letter)

    new_index = index + steps

    new_letter = alphabet[new_index]

    output += new_letter


print(output)