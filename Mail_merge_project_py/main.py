PLACEHOLDER = "[name]"  # the text to be changed

# open the invite list and extract content as a list
with open("./Input/Names/invited_names.txt") as names:
    invite_list = names.readlines()

# open the starting letter
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    # loop through names in invite list, create a new letter and replace the placeholder with the name in current iteration
    for name in invite_list:
        new_letter = letter.replace(PLACEHOLDER, name.strip())
        # write contents of new letter to outgoing folder
        with open(
            f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w"
        ) as outgoing_letter:
            outgoing_letter.write(new_letter)
