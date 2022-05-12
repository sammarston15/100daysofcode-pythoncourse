PLACEHOLDER = "[name]"

# read info from names list
with open('./Input/Names/invited_names.txt', 'r') as names_list:
    names = names_list.readlines()

# read lines from the starting letter
with open('./Input/Letters/starting_letter.txt', "r") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt', mode="w") as completed_letter:
            completed_letter.write(new_letter)
