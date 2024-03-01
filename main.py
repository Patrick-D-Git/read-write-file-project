
# Getting each name in the invited_names.txt

with open("./Input/Names/Invited_names.txt", "r") as name_file:
    invited_names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    starting_letter_content = letter_file.read()

for name in invited_names:

    # Replace the [name] placeholder with the actual name.
    new_name = name.strip()
    invitation_letter = starting_letter_content.replace("[name]", new_name)

    # Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/letter_to_{new_name}.txt", "w") as invitation_file:
        invitation_file.write(invitation_letter)


# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
