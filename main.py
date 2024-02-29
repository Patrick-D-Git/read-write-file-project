
# Getting each name in the invited_names.txt

with open("./Input/Names/Invited_names.txt", "r") as name_file:
    invited_names = name_file.readlines()

invited_names_list = []
for name in invited_names:
    new_name = name.strip()
    invited_names_list.append(new_name)


with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    starting_letter_content = letter_file.read()

for name in invited_names_list:

    # Replace the [name] placeholder with the actual name.
    invitation_letter = starting_letter_content.replace("[name]", name)

    # Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", "w") as invitation_file:
        invitation_file.write(invitation_letter)


# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
