# Hello! Welcome to the final version of my Mail Merge Project!

# In this project, I learned a lot of file management skills.

# P.S: If you have any questions or suggestions about this code, feel free to reach out to me!


# Opening the invited names file
with open(file="./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    stripped_names = []

# Stripping all names and appending them to a new list
    for name in names:
        stripped_name = name.strip()
        stripped_names.append(stripped_name)

# Opening the starting letter file
with open(file="./Input/Letters/starting_letter.txt") as file:
    base_letter = file.read()
    for name in stripped_names:

        # Replacing the placeholder "[name]" with the stripped invited names
        new_letter = base_letter.replace("[name]", f"{name}")

        # For last, creating files .txt for these new letters (it could also be .docx)
        with open(file=f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)