#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
with open('./Input/Names/invited_names.txt',mode='r') as f:
    name = f.readlines()
    for n in name:
        names.append(n.strip())

letter = ""
with open('./Input/Letters/starting_letter.txt', mode='r') as f:
    letter = f.read()

for name in names:
    n_letter = letter.replace("[name]", name)
    with open(f'./Output/ReadyToSend/{name}_invitation.txt', mode='w') as f:
        f.write(n_letter)
