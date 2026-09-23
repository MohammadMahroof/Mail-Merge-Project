with open("Input/Names/invited_names.txt") as file:
    names = [name.strip() for name in file.readlines()]
    
with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for name in names:
        personalized_letter = letter.replace("[name]", name)
        with open("Output/ReadyToSend/" + name + ".txt", "w") as file:
            file.write(personalized_letter)











































