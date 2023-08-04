with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
with open("Input/Letters/starting_letter.txt") as letter:
    lines = letter.readlines()

for name in names_list:
    name = name.strip()
    new_file = name
    with open(f"Output/ReadyToSend/letter_for_{new_file}.txt", "w") as new_file:
        for line in lines:
            line = line.replace("[name]", name)
            new_file.write(line)